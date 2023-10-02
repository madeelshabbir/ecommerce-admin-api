from app.models import Product, Inventory
from app.utils.database import SessionLocal
from fastapi import APIRouter, HTTPException, Path, Query
from pydantic import BaseModel
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

@inventories_router.get('/{id}')
async def get_inventory(
  id: int = Path(..., description='Inventory ID for retrieving the inventory')
):
  db = SessionLocal()
  inventory = db.query(Inventory).filter(Inventory.id == id).first()

  if inventory is None:
    raise HTTPException(status_code=404, detail=f"Inventory with ID {id} not found")

  product = inventory.product

  return {
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

class UpdateInventoryRequestModel(BaseModel):
  quantity: int

@inventories_router.patch('/{id}')
async def update_inventory(
  id: int = Path(..., description='Inventory ID of the inventory resource'),
  body: UpdateInventoryRequestModel = ...
):
  db = SessionLocal()
  inventory = db.query(Inventory).filter(Inventory.id == id).first()

  if inventory is None:
    db.close()
    raise HTTPException(status_code=404, detail=f"Inventory with ID {id} not found")

  inventory.quantity = body.quantity
  db.commit()
  db.refresh(inventory)
  db.close()

  return inventory
