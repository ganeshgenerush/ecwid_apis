from fastapi import APIRouter, Query
from services.ecwid import ecwid
from fastapi import Body

router = APIRouter(
    prefix="/paymentOptions",
    tags=["Payment Options"]
)


@router.get("")
async def get_payment_options(
        lang: str | None = None
):
    params = {}

    if lang:
        params["lang"] = lang

    return await ecwid.get(
        "/profile/paymentOptions",
        params
    )


@router.get("/{payment_option_id}")
async def get_payment_option(
        payment_option_id: str,
        lang: str | None = None
):
    params = {}

    if lang:
        params["lang"] = lang

    return await ecwid.get(
        f"/profile/paymentOptions/{payment_option_id}",
        params
    )


@router.post("")
async def create_payment_option(
        payload: dict = Body(...)
):
    return await ecwid.post(
        "/profile/paymentOptions",
        payload
    )


@router.put("/{payment_option_id}")
async def update_payment_option(
        payment_option_id: str,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/profile/paymentOptions/{payment_option_id}",
        payload
    )


@router.delete("/{payment_option_id}")
async def delete_payment_option(
        payment_option_id: str
):
    return await ecwid.delete(
        f"/profile/paymentOptions/{payment_option_id}"
    )
