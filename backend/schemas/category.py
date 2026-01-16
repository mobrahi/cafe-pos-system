"""
Pydantic schemas for category validation and serialization
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CategoryBase(BaseModel):
    category_name: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    category_name: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None

class Category(CategoryBase):
    category_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True