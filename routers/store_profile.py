from typing import Literal

from fastapi import APIRouter, Body
from services.ecwid import ecwid

router = APIRouter(
    prefix="/profile",
    tags=["Store Profile"]
)


@router.get("")
async def get_store_profile():
    return await ecwid.get("/profile")


@router.put("")
async def update_store_profile(
        payload: dict = Body(...)
):
    return await ecwid.put(
        "/profile",
        payload
    )


@router.put("/logos/{logo}")
async def upload_store_logo_image(
        logo: Literal["logo", "invoicelogo", "emaillogo"],
        external_url: str
):
    return await ecwid.put(
        f"/profile/{logo}",
        params={
            "externalUrl": external_url
        }
    )


@router.delete("/logos/{logo}")
async def delete_store_logo_image(
        logo: Literal["logo", "invoicelogo", "emaillogo"]
):
    return await ecwid.delete(
        f"/profile/{logo}"
    )


@router.get("/reports/{report_type}")
async def get_store_report(
        report_type: str,
        started_from: int | None = None,
        ended_at: int | None = None,
        time_scale_value: Literal[
            "hour",
            "day",
            "week",
            "month",
            "year"
        ] | None = None,
        compare_period: Literal[
            "noComparePeriod",
            "similarPeriodInPreviousWeek",
            "similarPeriodInPreviousMonth",
            "similarPeriodInPreviousYear",
            "previousPeriod"
        ] | None = None
):
    params = {
        "startedFrom": started_from,
        "endedAt": ended_at,
        "timeScaleValue": time_scale_value,
        "comparePeriod": compare_period
    }

    return await ecwid.get(
        f"/reports/{report_type}",
        {
            key: value
            for key, value in params.items()
            if value is not None
        }
    )


@router.get("/latest-stats")
async def get_latest_store_update_stats(
        reviews_updates_required: bool | None = None,
        domains_required: bool | None = None,
        subscription_required: bool | None = None,
        product_count_required: bool | None = None,
        category_count_required: bool | None = None
):
    params = {
        "reviewsUpdatesRequired": reviews_updates_required,
        "domainsRequired": domains_required,
        "subscriptionRequired": subscription_required,
        "productCountRequired": product_count_required,
        "categoryCountRequired": category_count_required
    }

    return await ecwid.get(
        "/latest-stats",
        {
            key: value
            for key, value in params.items()
            if value is not None
        }
    )


@router.get("/deleted/{entity}")
async def get_deleted_items_history(
        entity: Literal[
            "orders",
            "products",
            "coupons",
            "customers",
            "reviews"
        ],
        from_date: str | None = None,
        to_date: str | None = None,
        offset: int = 0,
        limit: int = 100
):
    params = {
        "from_date": from_date,
        "to_date": to_date,
        "offset": offset,
        "limit": limit
    }

    return await ecwid.get(
        f"/{entity}/deleted",
        {
            key: value
            for key, value in params.items()
            if value is not None
        }
    )
