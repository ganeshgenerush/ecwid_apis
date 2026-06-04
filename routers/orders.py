from fastapi import APIRouter, Body
from services.ecwid import ecwid

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/")
async def get_orders(offset: int = 0):
    return await ecwid.get(
        "/orders",
        {
            "offset": offset
        })


@router.get("/{order_id}")
async def get_order(
        order_id: int
):
    return await ecwid.get(
        f"/orders/{order_id}"
    )


@router.get("/search/")
async def search_orders(
        email: str | None = None,
        customer_id: int | None = None,
        payment_status: str | None = None,
        fulfillment_status: str | None = None,
        offset: int = 0,
        limit: int = 100
):
    params = {
        "offset": offset,
        "limit": limit
    }

    if email:
        params["email"] = email

    if customer_id:
        params["customerId"] = customer_id

    if payment_status:
        params["paymentStatus"] = payment_status

    if fulfillment_status:
        params["fulfillmentStatus"] = fulfillment_status

    return await ecwid.get(
        "/orders",
        params
    )


@router.put("/{order_id}")
async def update_order(
        order_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/orders/{order_id}",
        payload
    )


@router.put("/{order_id}/payment-status")
async def update_payment_status(
        order_id: int,
        payment_status: str
):
    return await ecwid.put(
        f"/orders/{order_id}",
        {
            "paymentStatus": payment_status
        }
    )


@router.put("/{order_id}/fulfillment-status")
async def update_fulfillment_status(
        order_id: int,
        fulfillment_status: str
):
    return await ecwid.put(
        f"/orders/{order_id}",
        {
            "fulfillmentStatus": fulfillment_status
        }
    )


@router.put("/{order_id}/tracking")
async def update_tracking(
        order_id: int,
        tracking_number: str,
        tracking_url: str | None = None
):
    payload = {
        "trackingNumber": tracking_number
    }

    if tracking_url:
        payload["trackingUrl"] = tracking_url

    return await ecwid.put(
        f"/orders/{order_id}",
        payload
    )


@router.put("/{order_id}/notes")
async def update_notes(
        order_id: int,
        notes: str
):
    return await ecwid.put(
        f"/orders/{order_id}",
        {
            "internalNotes": notes
        }
    )


@router.put("/{order_id}/shipping")
async def update_shipping(
        order_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/orders/{order_id}",
        payload
    )


@router.put("/{order_id}/customer")
async def update_customer(
        order_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/orders/{order_id}",
        payload
    )


@router.get("/stats/count")
async def order_count():
    data = await ecwid.get(
        "/orders",
        {
            "limit": 1
        }
    )

    return {
        "total": data.get("total", 0)
    }


@router.get("/recent/list")
async def recent_orders(
        limit: int = 10
):
    return await ecwid.get(
        "/orders",
        {
            "limit": limit,
            "offset": 0
        }
    )


@router.get("/customer/{customer_id}")
async def customer_orders(
        customer_id: int
):
    return await ecwid.get(
        "/orders",
        {
            "customerId": customer_id
        }
    )


@router.get("/customer/email/{email}")
async def orders_by_email(
        email: str
):
    return await ecwid.get(
        "/orders",
        {
            "email": email
        }
    )
