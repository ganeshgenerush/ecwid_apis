from fastapi import APIRouter, Query
from services.ecwid import ecwid
from fastapi import Body

router = APIRouter(prefix="/catalog", tags=["Catalog"])


@router.get("/products")
async def get_products():
    try:
        return await ecwid.get("/products")
    except Exception as e:
        raise e


@router.get("/products/search")
async def search_products(
        keyword: str,
        category: int | None = None
):
    params = {
        "keyword": keyword
    }

    if category:
        params["category"] = category

    return await ecwid.get(
        "/products",
        params
    )


@router.get("/products/{product_id}")
async def get_product(product_id: int):
    return await ecwid.get(f"/products/{product_id}")


@router.post("/products")
async def create_product(
        payload: dict = Body(...)
):
    return await ecwid.post("/products", payload)


@router.put("/products/{product_id}")
async def update_product(
        product_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/products/{product_id}",
        payload
    )


@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    return await ecwid.delete(
        f"/products/{product_id}"
    )


@router.get("/categories")
async def get_categories():
    return await ecwid.get("/categories")


@router.get("/categories/{category_id}")
async def get_category(category_id: int):
    return await ecwid.get(
        f"/categories/{category_id}"
    )


@router.put("/categories/{category_id}")
async def update_category(
        category_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/categories/{category_id}",
        payload
    )


@router.delete("/categories/{category_id}")
async def delete_category(
        category_id: int
):
    return await ecwid.delete(
        f"/categories/{category_id}"
    )


@router.get("/brands")
async def get_brands():
    return await ecwid.get("/brands")


@router.post("/products/batch-delete")
async def batch_delete_products(
        product_ids: list[int] = Body(...)
):
    return await ecwid.post(
        "/products/batchDelete",
        {
            "ids": product_ids
        }
    )
