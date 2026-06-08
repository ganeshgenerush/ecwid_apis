from fastapi import APIRouter, Body
from services.ecwid import ecwid

router = APIRouter(
    prefix="/staff",
    tags=["Staff"]
)


@router.get("")
async def get_staff():
    return await ecwid.get("/staff")


@router.get("/{staff_id}")
async def get_staff_member(
        staff_id: int
):
    staff = await ecwid.get("/staff")

    for member in staff.get("items", []):
        if member.get("id") == staff_id:
            return member

    return {
        "success": False,
        "message": "Staff member not found"
    }


@router.post("")
async def create_staff(
        payload: dict = Body(...)
):
    return await ecwid.post(
        "/staff",
        payload
    )


@router.put("/{staff_id}")
async def update_staff(
        staff_id: int,
        payload: dict = Body(...)
):
    return await ecwid.put(
        f"/staff/{staff_id}",
        payload
    )


@router.delete("/{staff_id}")
async def delete_staff(
        staff_id: int
):
    return await ecwid.delete(
        f"/staff/{staff_id}"
    )


@router.post("/invitations")
async def invite_staff(
        payload: dict = Body(...)
):
    return await ecwid.post(
        "/staff/invitations",
        payload
    )


@router.post("/invite")
async def quick_invite(
        email: str
):
    return await ecwid.post(
        "/staff/invitations",
        {
            "email": email
        }
    )


@router.put("/{staff_id}/permissions")
async def update_permissions(
        staff_id: int,
        permissions: list[str]
):
    return await ecwid.put(
        f"/staff/{staff_id}",
        {
            "permissions": permissions
        }
    )


@router.put("/{staff_id}/activate")
async def activate_staff(
        staff_id: int
):
    return await ecwid.put(
        f"/staff/{staff_id}",
        {
            "enabled": True
        }
    )


@router.put("/{staff_id}/deactivate")
async def deactivate_staff(
        staff_id: int
):
    return await ecwid.put(
        f"/staff/{staff_id}",
        {
            "enabled": False
        }
    )


@router.get("/stats/count")
async def staff_count():
    staff = await ecwid.get("/staff")

    return {
        "total": len(staff.get("items", []))
    }
