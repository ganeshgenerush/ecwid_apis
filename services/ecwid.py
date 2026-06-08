import os
from contextvars import ContextVar

import httpx
from dotenv import load_dotenv
from models.environment import Environment

load_dotenv()
STORES = {
    "test": {
        "store_id": os.getenv("TEST_STORE_ID"),
        "token": os.getenv("TEST_TOKEN")
    },
    "production": {
        "store_id": os.getenv("PROD_STORE_ID"),
        "token": os.getenv("PROD_TOKEN")
    }
}


selected_environment: ContextVar[Environment] = ContextVar(
    "selected_environment",
    default=Environment.production,
)


def set_selected_environment(environment: Environment) -> None:
    selected_environment.set(environment)


class EcwidClient:
    def __init__(self, environment: Environment = Environment.production):
        config = STORES[environment.value]
        self.base_url = (
            f"https://app.ecwid.com/api/v3/"
            f"{config['store_id']}"
        )
        self.headers = {
            "Authorization": f"Bearer {config['token']}"
        }

    async def get(self, endpoint: str, params: dict | None = None):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                params=params
            )

        response.raise_for_status()
        return response.json()

    async def post(
            self,
            endpoint: str,
            payload: dict | None = None,
            params: dict | None = None
    ):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                json=payload,
                params=params
            )

        response.raise_for_status()
        return response.json()

    async def put(self, endpoint: str, payload: dict):
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                json=payload
            )

        response.raise_for_status()
        return response.json()

    async def delete(self, endpoint: str):
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{self.base_url}{endpoint}",
                headers=self.headers
            )

        response.raise_for_status()
        return {"success": True}


class EcwidClientProxy:
    def _client(self) -> EcwidClient:
        return EcwidClient(selected_environment.get())

    async def get(self, endpoint: str, params: dict | None = None):
        return await self._client().get(endpoint, params)

    async def post(
            self,
            endpoint: str,
            payload: dict | None = None,
            params: dict | None = None
    ):
        return await self._client().post(endpoint, payload, params)

    async def put(self, endpoint: str, payload: dict):
        return await self._client().put(endpoint, payload)

    async def delete(self, endpoint: str):
        return await self._client().delete(endpoint)


ecwid = EcwidClientProxy()
