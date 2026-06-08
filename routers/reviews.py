from fastapi import APIRouter, Body
from services.ecwid import ecwid

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.get("")
async def get_reviews(
        offset: int = 0,
        limit: int = 100
):
    return await ecwid.get(
        "/reviews",
        {
            "offset": offset,
            "limit": limit
        }
    )


@router.get("/product/{product_id}")
async def get_product_reviews(
        product_id: int,
        offset: int = 0,
        limit: int = 100
):
    return await ecwid.get(
        "/reviews",
        {
            "productId": product_id,
            "offset": offset,
            "limit": limit
        }
    )


@router.get("/customer")
async def get_customer_reviews(
        email: str
):
    return await ecwid.get(
        "/reviews",
        {
            "email": email
        }
    )


@router.get("/{review_id}")
async def get_review(
        review_id: int
):
    reviews = await ecwid.get(
        "/reviews",
        {
            "limit": 100
        }
    )

    for review in reviews.get("items", []):
        if review.get("id") == review_id:
            return review

    return {
        "success": False,
        "message": "Review not found"
    }


@router.put("/{review_id}")
async def update_review(
        review_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/reviews/{review_id}",
        payload
    )


@router.put("/{review_id}/approve")
async def approve_review(
        review_id: int
):
    return await ecwid.put(
        f"/reviews/{review_id}",
        {
            "status": "APPROVED"
        }
    )


@router.get("/stats/count")
async def review_stats():
    reviews = await ecwid.get(
        "/reviews",
        {
            "limit": 1
        }
    )

    return {
        "total": reviews.get("total", 0)
    }
