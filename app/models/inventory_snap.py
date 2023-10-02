from datetime import datetime
from app.utils.database import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class InventorySnap(Base):
  __tablename__ = 'inventory_snaps'

  id = Column(Integer, primary_key=True, index=True)
  quantity = Column(Integer)
  created_at = Column(DateTime, default=datetime.utcnow)
  inventory_id = Column(Integer, ForeignKey('inventories.id'))

  inventory = relationship('Inventory', back_populates='inventory_snaps')
