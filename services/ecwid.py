import os
import httpx
from dotenv import load_dotenv

load_dotenv()

STORE_ID = os.getenv("STORE_ID")
TOKEN = os.getenv("TOKEN")

BASE_URL = f"https://app.ecwid.com/api/v3/{STORE_ID}"


class EcwidClient:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }

    async def get(self, endpoint: str, params: dict | None = None):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}{endpoint}",
                headers=self.headers,
                params=params
            )

        response.raise_for_status()
        return response.json()

    async def post(self, endpoint: str, payload: dict):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}{endpoint}",
                headers=self.headers,
                json=payload
            )

        response.raise_for_status()
        return response.json()

    async def put(self, endpoint: str, payload: dict):
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{BASE_URL}{endpoint}",
                headers=self.headers,
                json=payload
            )

        response.raise_for_status()
        return response.json()

    async def delete(self, endpoint: str):
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{BASE_URL}{endpoint}",
                headers=self.headers
            )

        response.raise_for_status()
        return {"success": True}


ecwid = EcwidClient()