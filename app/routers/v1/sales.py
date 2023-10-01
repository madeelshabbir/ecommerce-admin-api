from app.models import Product, Sale
from app.utils.database import SessionLocal
from fastapi import APIRouter, Query
from typing import Optional
from sqlalchemy import func

sales_router = APIRouter()

@sales_router.get('/')
async def get_sales(
  start_date: Optional[str] = Query(None, description='Start date for filtering sales data'),
  end_date: Optional[str] = Query(None, description='End date for filtering sales data'),
  product_id: Optional[str] = Query(None, description='Product ID for filtering sales data'),
  min_quantity: Optional[str] = Query(None, description='Minimum quantity for filtering sales data'),
  max_quantity: Optional[str] = Query(None, description='Maximum quantity for filtering sales data'),
  category_id: Optional[str] = Query(None, description='Category ID for filtering sales data')
):
  db = SessionLocal()
  query = (
    db.query(Sale.product_id,
             Product.title,
             Product.price,
             func.sum(Sale.quantity).label('total_quantity'),
             func.sum(Sale.quantity * Product.price).label('revenue'))
    .join(Product, Sale.product_id == Product.id)
  )

  if start_date:
    query = query.filter(Sale.created_at >= start_date)
  if end_date:
    query = query.filter(Sale.created_at <= end_date)
  if product_id:
    query = query.filter(Sale.product_id == product_id)
  if min_quantity:
    query = query.filter(Sale.quantity >= min_quantity)
  if max_quantity:
    query = query.filter(Sale.quantity <= max_quantity)
  if category_id:
    query = query.join(Sale.product).filter(Product.category_id == category_id)

  sales = query.group_by(Sale.product_id, Product.price).all()
  db.close()

  response_data = [
    {
      'product_id': sale.product_id,
      'product_title': sale.title,
      'price': sale.price,
      'total_quantity': sale.total_quantity,
      'revenue': sale.revenue
    }
    for sale in sales
  ]

  return response_data
