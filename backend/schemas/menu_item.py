"""
Pydantic schemas for menu item validation and serialization
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Base schema with common fields
class MenuItemBase(BaseModel):
    item_name: str = Field(..., min_length=1, max_length=100)
    category_id: int = Field(..., gt=0)
    price: float = Field(..., gt=0)
    description: Optional[str] = None
    stock_quantity: int = Field(default=0, ge=0)
    is_available: bool = True

# Schema for creating a new menu item
class MenuItemCreate(MenuItemBase):
    pass

# Schema for updating a menu item
class MenuItemUpdate(BaseModel):
    item_name: Optional[str] = Field(None, min_length=1, max_length=100)
    category_id: Optional[int] = Field(None, gt=0)
    price: Optional[float] = Field(None, gt=0)
    description: Optional[str] = None
    stock_quantity: Optional[int] = Field(None, ge=0)
    is_available: Optional[bool] = None

# Schema for returning menu item (includes database fields)
class MenuItem(MenuItemBase):
    item_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True  # Allows converting SQLAlchemy models to Pydantic

# Schema with category information included
class MenuItemWithCategory(MenuItem):
    category_name: str
    
    class Config:
        from_attributes = True