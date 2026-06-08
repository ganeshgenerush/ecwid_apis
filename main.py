import os
from fastapi import Depends, FastAPI, Request, HTTPException, Security, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyHeader
from dependency.ecwid import use_environment
from models.environment import Environment
from routers.catalog import router as catalog_router
from routers.orders import router as order_router
from routers.customers import router as customer_router
from services.ecwid import set_selected_environment
# from routers.promotions import router as promotions_router
from routers.coupons import router as coupon_router
# from routers.reviews import router as review_router
from routers.subscriptions import router as subscription_router
from routers.staff import router as staff_router
from routers.payment_options import router as payment_options_router
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY", "secret-api-key")
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)


async def get_api_key(api_key: str | None = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
    return api_key


#app = FastAPI(dependencies=[Depends(get_api_key)])

app = FastAPI(dependencies=[Depends(use_environment), Depends(get_api_key)])


@app.middleware("http")
async def select_environment_from_header(request: Request, call_next):
    environment = request.headers.get("environment")
    if environment in Environment._value2member_map_:
        set_selected_environment(Environment(environment))
    else:
        set_selected_environment(Environment.production)

    return await call_next(request)


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
# app.include_router(promotions_router)
app.include_router(coupon_router)
# app.include_router(review_router)
app.include_router(subscription_router)
app.include_router(staff_router)
app.include_router(payment_options_router)
