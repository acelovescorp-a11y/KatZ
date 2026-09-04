"""API v1 Router."""

from fastapi import APIRouter

from .scan import router as scan_router
from .voice import router as voice_router
from .dashboard import router as dashboard_router

router = APIRouter(prefix="/api/v1", tags=["v1"])

router.include_router(scan_router)
router.include_router(voice_router)
router.include_router(dashboard_router)
