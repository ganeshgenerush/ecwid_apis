from fastapi import APIRouter, Body
from services.ecwid import ecwid

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("")
async def get_customers(
        offset: int = 0,
        limit: int = 100
):
    return await ecwid.get(
        "/customers",
        {
            "offset": offset,
            "limit": limit
        }
    )


@router.get("/search/email")
async def search_customer_by_email(
        email: str
):
    return await ecwid.get(
        "/customers",
        {
            "email": email
        }
    )


@router.get("/stats/count")
async def customer_count():
    data = await ecwid.get(
        "/customers",
        {
            "limit": 1
        }
    )

    return {
        "total": data.get("total", 0)
    }


@router.get("/recent/list")
async def recent_customers(
        limit: int = 10
):
    return await ecwid.get(
        "/customers",
        {
            "limit": limit,
            "offset": 0
        }
    )


@router.get("/{customer_id}")
async def get_customer(
        customer_id: int
):
    return await ecwid.get(
        f"/customers/{customer_id}"
    )


@router.post("")
async def create_customer(
        payload: dict = Body(...)
):
    return await ecwid.post(
        "/customers",
        payload
    )


@router.put("/{customer_id}")
async def update_customer(
        customer_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/customers/{customer_id}",
        payload
    )


@router.put("/{customer_id}/name")
async def update_customer_name(
        customer_id: int,
        name: str
):
    return await ecwid.put(
        f"/customers/{customer_id}",
        {
            "billingPerson": {
                "name": name
            }
        }
    )


@router.put("/{customer_id}/email")
async def update_customer_email(
        customer_id: int,
        email: str
):
    return await ecwid.put(
        f"/customers/{customer_id}",
        {
            "email": email
        }
    )


@router.put("/{customer_id}/marketing")
async def update_marketing_preferences(
        customer_id: int,
        accept_marketing: bool
):
    return await ecwid.put(
        f"/customers/{customer_id}",
        {
            "acceptMarketing": accept_marketing
        }
    )
