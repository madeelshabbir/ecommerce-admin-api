from app.utils.database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Sale(Base):
  __tablename__ = 'sales'

  id = Column(Integer, primary_key=True, index=True)
  quantity = Column(Integer)
  created_at = Column(DateTime, default=datetime.utcnow)
  product_id = Column(Integer, ForeignKey('products.id'))

  product = relationship('Product', back_populates='sales')
