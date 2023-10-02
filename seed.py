from datetime import datetime
from app.utils.database import SessionLocal
from app.models.product import Product
from app.models.category import Category
from app.models.inventory import Inventory
from app.models.sale import Sale

category_data = [
  {'name': 'Food and beverage'},
  {'name': 'Accessories'},
  {'name': 'Health care'},
]

product_data = [
  {'title': 'Coke', 'description': 'Soft drink', 'price': 12.99, 'category_id': 1},
  {'title': 'Panadol', 'description': 'Pain Killer Medicine', 'price': 3.99, 'category_id': 3},
  {'title': 'Pepsi', 'description': 'Soft drink', 'price': 10.99, 'category_id': 1},
]

sale_data = [
  {'quantity': 5, 'created_at': datetime.utcnow(), 'product_id': 1},
  {'quantity': 10, 'created_at': datetime.utcnow(), 'product_id': 2},
  {'quantity': 8, 'created_at': datetime.utcnow(), 'product_id': 3},
]

def seed_data():
  try:
    db = SessionLocal()

    for data in category_data:
      category = Category(**data)
      db.add(category)

    for data in product_data:
      product = Product(**data)
      db.add(product)

    for data in sale_data:
      sale = Sale(**data)
      db.add(sale)

    db.commit()
    print('Seed data inserted successfully!')

  except Exception as e:
    print(f"Error: {e}")
    db.rollback()
  finally:
    db.close()

seed_data()
