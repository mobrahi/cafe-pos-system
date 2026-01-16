"""
FastAPI endpoints for menu items
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.database import get_db
from backend.schemas.menu_item import MenuItem, MenuItemCreate, MenuItemUpdate
from backend.crud import menu_item as crud

router = APIRouter()

@router.get("/", response_model=List[MenuItem])
def read_menu_items(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    Retrieve all menu items with pagination
    """
    items = crud.get_menu_items(db, skip=skip, limit=limit)
    return items

@router.get("/available", response_model=List[MenuItem])
def read_available_menu_items(db: Session = Depends(get_db)):
    """
    Retrieve only available menu items
    """
    items = crud.get_available_menu_items(db)
    return items

@router.get("/{item_id}", response_model=MenuItem)
def read_menu_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific menu item by ID
    """
    db_item = crud.get_menu_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Menu item with id {item_id} not found"
        )
    return db_item

@router.get("/category/{category_id}", response_model=List[MenuItem])
def read_menu_items_by_category(category_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all menu items in a specific category
    """
    items = crud.get_menu_items_by_category(db, category_id=category_id)
    return items

@router.post("/", response_model=MenuItem, status_code=status.HTTP_201_CREATED)
def create_menu_item(menu_item: MenuItemCreate, db: Session = Depends(get_db)):
    """
    Create a new menu item
    """
    return crud.create_menu_item(db=db, menu_item=menu_item)

@router.put("/{item_id}", response_model=MenuItem)
def update_menu_item(
    item_id: int, 
    menu_item: MenuItemUpdate, 
    db: Session = Depends(get_db)
):
    """
    Update an existing menu item
    """
    db_item = crud.update_menu_item(db, item_id=item_id, menu_item=menu_item)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Menu item with id {item_id} not found"
        )
    return db_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete a menu item
    """
    success = crud.delete_menu_item(db, item_id=item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Menu item with id {item_id} not found"
        )
    return None

@router.patch("/{item_id}/stock", response_model=MenuItem)
def update_item_stock(
    item_id: int, 
    quantity_change: int, 
    db: Session = Depends(get_db)
):
    """
    Update stock quantity for a menu item
    quantity_change: positive to add stock, negative to subtract
    """
    db_item = crud.update_stock(db, item_id=item_id, quantity_change=quantity_change)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Menu item with id {item_id} not found"
        )
    return db_item