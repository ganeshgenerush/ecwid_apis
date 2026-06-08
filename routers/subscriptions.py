from fastapi import APIRouter, Body
from services.ecwid import ecwid

router = APIRouter(
    prefix="/subscriptions",
    tags=["Subscriptions"]
)


@router.get("")
async def get_subscriptions(
        offset: int = 0,
        limit: int = 100
):
    return await ecwid.get(
        "/subscriptions",
        {
            "offset": offset,
            "limit": limit
        }
    )


@router.get("/{subscription_id}")
async def get_subscription(
        subscription_id: int
):
    return await ecwid.get(
        f"/subscriptions/{subscription_id}"
    )


@router.get("/search/email")
async def get_subscriptions_by_email(
        email: str
):
    return await ecwid.get(
        "/subscriptions",
        {
            "email": email
        }
    )


@router.get("/active/list")
async def get_active_subscriptions():
    return await ecwid.get(
        "/subscriptions",
        {
            "status": "ACTIVE"
        }
    )


@router.get("/paused/list")
async def get_paused_subscriptions():
    return await ecwid.get(
        "/subscriptions",
        {
            "status": "PAUSED"
        }
    )


@router.get("/cancelled/list")
async def get_cancelled_subscriptions():
    return await ecwid.get(
        "/subscriptions",
        {
            "status": "CANCELLED"
        }
    )


@router.put("/{subscription_id}")
async def update_subscription(
        subscription_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/subscriptions/{subscription_id}",
        payload
    )


@router.put("/{subscription_id}/pause")
async def pause_subscription(
        subscription_id: int
):
    return await ecwid.put(
        f"/subscriptions/{subscription_id}",
        {
            "status": "PAUSED"
        }
    )


@router.put("/{subscription_id}/billing-date")
async def update_billing_date(
        subscription_id: int,
        next_billing_date: str
):
    return await ecwid.put(
        f"/subscriptions/{subscription_id}",
        {
            "nextBillingDate": next_billing_date
        }
    )


@router.get("/stats/count")
async def subscription_stats():
    data = await ecwid.get(
        "/subscriptions",
        {
            "limit": 1
        }
    )

    return {
        "total": data.get("total", 0)
    }
