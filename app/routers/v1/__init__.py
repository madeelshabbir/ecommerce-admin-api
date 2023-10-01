from app.routers.v1.sales import sales_router
from fastapi import APIRouter

v1_router = APIRouter()

v1_router.include_router(sales_router, prefix='/sales')
