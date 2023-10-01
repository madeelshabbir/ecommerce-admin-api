from app.utils.database import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Inventory(Base):
  __tablename__ = 'inventories'

  id = Column(Integer, primary_key=True, index=True)
  quantity = Column(Integer)
  updated_at = Column(DateTime)
  product_id = Column(Integer, ForeignKey('products.id'))

  product = relationship('Product', back_populates='inventory')
