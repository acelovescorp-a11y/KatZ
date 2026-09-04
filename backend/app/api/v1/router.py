"""API v1 Router."""

from fastapi import APIRouter

from .scan import router as scan_router
from .voice import router as voice_router

router = APIRouter(prefix="/api/v1", tags=["v1"])

router.include_router(scan_router)
router.include_router(voice_router)
