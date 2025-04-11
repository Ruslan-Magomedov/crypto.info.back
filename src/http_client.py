from aiohttp import ClientSession


class HttpClient:
    def __init__(self, url: str, api_key: str):
        self._session = ClientSession(
            base_url=url,
            headers={
                'X-CMC_PRO_API_KEY': api_key,
            }
        )


class CMCHttpClient(HttpClient):
    async def get_listings(self):
        async with self._session.get("/v1/cryptocurrency/listings/latest") as res:
            result = await res.json()
            return result["data"]

    async def get_currency(self, currency_id: int):
        async with self._session.get(
            "/v2/cryptocurrency/quotes/latest",
            params={"id": currency_id}
        ) as res:
            result = await res.json()
            return result["data"][str(currency_id)]
