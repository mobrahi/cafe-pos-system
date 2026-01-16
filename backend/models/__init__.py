"""
Import all models here so SQLAlchemy can find them
"""
from backend.models.category import Category
#from backend.models.order import Order, OrderItem
from backend.models.menu_item import MenuItem

# This ensures all models are registered with SQLAlchemy
__all__ = ["Category", "MenuItem", "Order", "OrderItem"]

