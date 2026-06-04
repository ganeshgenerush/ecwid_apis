from fastapi import FastAPI
from routers.catalog import router as catalog_router
from routers.orders import router as order_router

app = FastAPI()

app.include_router(catalog_router)
app.include_router(order_router)
