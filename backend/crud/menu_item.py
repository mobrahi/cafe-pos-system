"""
CRUD operations for menu items
"""
from sqlalchemy.orm import Session, joinedload
from backend.models.menu_item import MenuItem
from backend.schemas.menu_item import MenuItemCreate, MenuItemUpdate
from typing import List, Optional

def get_menu_items(db: Session, skip: int = 0, limit: int = 100) -> List[MenuItem]:
    """Get all menu items with pagination"""
    return db.query(MenuItem).offset(skip).limit(limit).all()

def get_menu_item(db: Session, item_id: int) -> Optional[MenuItem]:
    """Get a single menu item by ID"""
    return db.query(MenuItem).filter(MenuItem.item_id == item_id).first()

def get_menu_items_by_category(db: Session, category_id: int) -> List[MenuItem]:
    """Get all menu items in a specific category"""
    return db.query(MenuItem).filter(MenuItem.category_id == category_id).all()

def get_available_menu_items(db: Session) -> List[MenuItem]:
    """Get only available menu items"""
    return db.query(MenuItem).filter(MenuItem.is_available == True).all()

def create_menu_item(db: Session, menu_item: MenuItemCreate) -> MenuItem:
    """Create a new menu item"""
    db_item = MenuItem(**menu_item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_menu_item(db: Session, item_id: int, menu_item: MenuItemUpdate) -> Optional[MenuItem]:
    """Update an existing menu item"""
    db_item = get_menu_item(db, item_id)
    if db_item is None:
        return None
    
    # Update only provided fields
    update_data = menu_item.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_menu_item(db: Session, item_id: int) -> bool:
    """Delete a menu item"""
    db_item = get_menu_item(db, item_id)
    if db_item is None:
        return False
    
    db.delete(db_item)
    db.commit()
    return True

def update_stock(db: Session, item_id: int, quantity_change: int) -> Optional[MenuItem]:
    """Update stock quantity (positive to add, negative to subtract)"""
    db_item = get_menu_item(db, item_id)
    if db_item is None:
        return None
    
    db_item.stock_quantity += quantity_change
    
    # Prevent negative stock
    if db_item.stock_quantity < 0:
        db_item.stock_quantity = 0
    
    db.commit()
    db.refresh(db_item)
    return db_item