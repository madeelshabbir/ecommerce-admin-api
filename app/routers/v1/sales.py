from app.models import Product, Sale
from app.utils.database import SessionLocal
from fastapi import APIRouter, Query
from typing import Optional

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
  query = db.query(Sale)

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

  sales = query.all()
  db.close()
  return sales
