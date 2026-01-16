"""
Main API router that aggregates all endpoint routers
"""
from fastapi import APIRouter
from backend.api.v1.endpoints import categories, menu_items

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(
    categories.router,
    prefix="/categories",
    tags=["categories"]
)

api_router.include_router(
    menu_items.router,
    prefix="/menu-items",
    tags=["menu-items"]
)

# Add more routers here as you build them:
# api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
# api_router.include_router(reports.router, prefix="/reports", tags=["reports"])