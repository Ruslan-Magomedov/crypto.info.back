from fastapi import APIRouter

from src.config import settings


router = APIRouter(prefix="/crypto.info", tags=["Get coins"])


@router.get("", summary="Get coins")
async def get_coins():
    ...


@router.get("/{coin_id}", summary="Get a coin")
async def get_coin(coin_id: int):
    ...
