from datetime import datetime
from app.models.inventory_snap import InventorySnap
from app.utils.database import Base, SessionLocal
from sqlalchemy import Column, Integer, DateTime, ForeignKey, event
from sqlalchemy.orm import relationship

class Inventory(Base):
  __tablename__ = 'inventories'

  id = Column(Integer, primary_key=True, index=True)
  quantity = Column(Integer)
  updated_at = Column(DateTime, default=datetime.utcnow)
  product_id = Column(Integer, ForeignKey('products.id'))

  product = relationship('Product', back_populates='inventory')
  inventory_snaps = relationship('InventorySnap', back_populates='inventory')

@event.listens_for(Inventory, 'before_update')
def before_update_listener(_, __, target):
  target.updated_at = datetime.utcnow()

@event.listens_for(Inventory, 'after_insert')
@event.listens_for(Inventory, 'after_update')
def create_inventory_snap(_, connection, target):
  session = SessionLocal(bind=connection)
  inventory_snap = InventorySnap(
    quantity=target.quantity,
    created_at=datetime.utcnow(),
    inventory_id=target.id
  )
  session.add(inventory_snap)
  session.commit()
