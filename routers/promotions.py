from fastapi import APIRouter, Body, Query
from services.ecwid import ecwid
from pydantic import BaseModel
from typing import Literal


class PromotionCreate(BaseModel):
    name: str
    enabled: bool = True
    discountBase: Literal[
        "ITEM",
        "SUBTOTAL",
        "SHIPPING"
    ]
    discountType: Literal[
        "PERCENT",
        "ABSOLUTE",
        "FIXED_PRICE"
    ]
    amount: float
    triggers: dict
    targets: dict | None = None


router = APIRouter(
    prefix="/promotions",
    tags=["Promotions"]
)


@router.get("")
async def get_promotions():
    return await ecwid.get("/promotions")


@router.get("/{promotion_id}")
async def get_promotion(
        promotion_id: int
):
    promotions = await ecwid.get("/promotions")

    for promotion in promotions.get("items", []):
        if promotion.get("id") == promotion_id:
            return promotion

    return {
        "success": False,
        "message": "Promotion not found"
    }


@router.post("")
async def create_promotion(
        payload: dict = Body(...)
):
    return await ecwid.post(
        "/promotions",
        payload
    )


@router.put("/{promotion_id}")
async def update_promotion(
        promotion_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/promotions/{promotion_id}",
        payload
    )


@router.post("")
async def create_promotion(
        payload: PromotionCreate
):
    return await ecwid.post(
        "/promotions",
        payload.model_dump(exclude_none=True)
    )
