"""
CRUD operations for categories
"""
from sqlalchemy.orm import Session
from backend.models.category import Category
from backend.schemas.category import CategoryCreate, CategoryUpdate
from typing import List, Optional

def get_categories(db: Session) -> List[Category]:
    """Get all categories"""
    return db.query(Category).all()

def get_category(db: Session, category_id: int) -> Optional[Category]:
    """Get a single category by ID"""
    return db.query(Category).filter(Category.category_id == category_id).first()

def get_category_by_name(db: Session, category_name: str) -> Optional[Category]:
    """Get a category by name"""
    return db.query(Category).filter(Category.category_name == category_name).first()

def create_category(db: Session, category: CategoryCreate) -> Category:
    """Create a new category"""
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, category: CategoryUpdate) -> Optional[Category]:
    """Update an existing category"""
    db_category = get_category(db, category_id)
    if db_category is None:
        return None
    
    update_data = category.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_category, key, value)
    
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int) -> bool:
    """Delete a category (only if no menu items exist)"""
    db_category = get_category(db, category_id)
    if db_category is None:
        return False
    
    # Check if category has menu items
    if db_category.menu_items:
        return False  # Cannot delete category with items
    
    db.delete(db_category)
    db.commit()
    return True