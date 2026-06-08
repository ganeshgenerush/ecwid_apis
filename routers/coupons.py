from fastapi import APIRouter, Body
from services.ecwid import ecwid
from pydantic import BaseModel
from typing import Literal


class CouponCreate(BaseModel):
    name: str
    code: str
    enabled: bool = True
    discountType: Literal[
        "ABS",
        "PERCENT"
    ]
    discount: float


router = APIRouter(
    prefix="/coupons",
    tags=["Coupons"]
)


@router.get("")
async def get_coupons(
        limit: int = 100,
        offset: int = 0
):
    return await ecwid.get(
        "/discount_coupons",
        {
            "limit": limit,
            "offset": offset
        }
    )


@router.get("/{coupon_id}")
async def get_coupon(
        coupon_id: int
):
    return await ecwid.get(
        f"/discount_coupons/{coupon_id}"
    )


@router.get("/search/code")
async def search_coupon(
        code: str
):
    return await ecwid.get(
        "/discount_coupons",
        {
            "couponCode": code
        }
    )


@router.post("")
async def create_coupon(
        payload: dict = Body(...)
):
    return await ecwid.post(
        "/discount_coupons",
        payload
    )


@router.put("/{coupon_id}")
async def update_coupon(
        coupon_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/discount_coupons/{coupon_id}",
        payload
    )


@router.get("/active/list")
async def active_coupons():
    return await ecwid.get(
        "/discount_coupons",
        {
            "enabled": True
        }
    )


@router.get("/expired/list")
async def expired_coupons():
    return await ecwid.get(
        "/discount_coupons",
        {
            "status": "EXPIRED"
        }
    )


@router.get("/stats/count")
async def coupon_count():
    data = await ecwid.get(
        "/discount_coupons",
        {
            "limit": 1
        }
    )

    return {
        "total": data.get("total", 0)
    }
