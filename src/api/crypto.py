from fastapi import APIRouter

from src.config import settings
from src.http_client import CMCHttpClient


router = APIRouter(prefix="/crypto.info", tags=["Get coins"])
cmc_client = CMCHttpClient(
    url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_KEY
)


@router.get("", summary="Get coins")
async def get_coins():
    return await cmc_client.get_listings()


@router.get("/{coin_id}", summary="Get a coin")
async def get_coin(coin_id: int):
    return await cmc_client.get_currency(coin_id)
