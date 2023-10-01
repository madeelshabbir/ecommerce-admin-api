from app.utils.database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
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
