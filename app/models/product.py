from app.models.inventory import Inventory
from app.utils.database import Base, SessionLocal
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, event
from sqlalchemy.orm import relationship

class Product(Base):
  __tablename__ = 'products'

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(String)
  price = Column(Float)
  created_at = Column(DateTime, default=datetime.utcnow)
  category_id = Column(Integer, ForeignKey('categories.id'))

  sales = relationship('Sale', back_populates='product')
  inventory = relationship('Inventory', back_populates='product')
  category = relationship('Category', back_populates='products')

@event.listens_for(Product, 'after_insert')
def create_inventory(_, connection, target):
  session = SessionLocal(bind=connection)
  inventory = Inventory(
    quantity=0,
    product_id=target.id
  )
  session.add(inventory)
  session.commit()
