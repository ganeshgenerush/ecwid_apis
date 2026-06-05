from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.catalog import router as catalog_router
from routers.orders import router as order_router
from routers.customers import router as customer_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(catalog_router)
app.include_router(order_router)
app.include_router(customer_router)
