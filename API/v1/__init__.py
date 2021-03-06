from fastapi import APIRouter
from .eu import EuropeRouter
from .kr import KrRouter
from .world import GlobalRouter

router = APIRouter()

router.include_router(
    KrRouter,
    prefix="/kr"
)
router.include_router(
    EuropeRouter,
    prefix="/eu"
)
router.include_router(
    GlobalRouter,
    prefix="/global"
)