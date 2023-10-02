from app.routers.v1.categories import categories_router
from app.routers.v1.inventories import inventories_router
from app.routers.v1.products import products_router
from app.routers.v1.sales import sales_router
from fastapi import APIRouter

v1_router = APIRouter()

v1_router.include_router(categories_router, prefix='/categories')
v1_router.include_router(inventories_router, prefix='/inventories')
v1_router.include_router(products_router, prefix='/products')
v1_router.include_router(sales_router, prefix='/sales')
