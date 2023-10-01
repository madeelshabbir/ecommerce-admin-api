from app.models import Category
from app.utils.database import SessionLocal
from fastapi import APIRouter, HTTPException, Path

categories_router = APIRouter()

@categories_router.get('/')
async def get_categories():
  db = SessionLocal()
  query = db.query(Category)
  categories = query.all()
  db.close()
  return categories

@categories_router.get('/{id}')
async def get_category(
  id: int = Path(..., description='Category ID for retrieving the category')
):
  db = SessionLocal()
  category = db.query(Category).filter(Category.id == id).first()
  db.close()

  if category is None:
    raise HTTPException(status_code=404, detail=f"Category with ID {id} not found")

  return category
