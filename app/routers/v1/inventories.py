from app.models import Product, Inventory
from app.utils.database import SessionLocal
from fastapi import APIRouter, Query
from typing import Optional

inventories_router = APIRouter()

@inventories_router.get('/')
async def get_inventories(
  low_stock_threshold: Optional[str] = Query(None, description='Low stock threshold for filtering inventory data')
):
  db = SessionLocal()
  query = db.query(Inventory, Product).join(Product, Inventory.product_id == Product.id)

  if low_stock_threshold:
    query = query.filter(Inventory.quantity < low_stock_threshold)

  inventories = query.all()
  db.close()

  response_data = [
    {
      'id': inventory.id,
      'quantity': inventory.quantity,
      'updated_at': inventory.updated_at,
      'product': {
        'id': product.id,
        'title': product.title,
        'description': product.description,
        'price': product.price,
        'created_at': product.created_at,
        'category_id': product.category_id,
      }
    }
    for inventory, product in inventories
  ]

  return response_data
