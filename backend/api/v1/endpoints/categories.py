"""
FastAPI endpoints for categories
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.database import get_db
from backend.schemas.category import Category, CategoryCreate, CategoryUpdate
from backend.crud import category as crud

router = APIRouter()

@router.get("/", response_model=List[Category])
def read_categories(db: Session = Depends(get_db)):
    """
    Retrieve all categories
    """
    categories = crud.get_categories(db)
    return categories

@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific category by ID
    """
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found"
        )
    return db_category

@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    """
    Create a new category
    """
    # Check if category name already exists
    existing = crud.get_category_by_name(db, category_name=category.category_name)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category '{category.category_name}' already exists"
        )
    return crud.create_category(db=db, category=category)

@router.put("/{category_id}", response_model=Category)
def update_category(
    category_id: int, 
    category: CategoryUpdate, 
    db: Session = Depends(get_db)
):
    """
    Update an existing category
    """
    db_category = crud.update_category(db, category_id=category_id, category=category)
    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found"
        )
    return db_category

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    """
    Delete a category (only if it has no menu items)
    """
    success = crud.delete_category(db, category_id=category_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Cannot delete category with id {category_id}. It may not exist or has menu items."
        )
    return None