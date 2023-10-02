from fastapi import APIRouter
from pydantic import BaseModel
from app.models.category import Category
from app.utils.database import SessionLocal
from app.models import Product

products_router = APIRouter()

class CreateProductRequestModel(BaseModel):
  title: str
  description: str
  price: float

@products_router.post('/')
async def create_product(body: CreateProductRequestModel = ...):
  db = SessionLocal()
  product = Product(
    title=body.title,
    description=body.description,
    price=body.price
  )

  db.add(product)
  db.commit()
  db.refresh(product)

  return product
