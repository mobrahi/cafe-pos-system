"""
SQLAlchemy model for menu items
"""
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"
    
    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)
    stock_quantity = Column(Integer, default=0)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    category = relationship("Category", back_populates="menu_items")
    # order_items = relationship("OrderItem", back_populates="menu_item")