from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
import json

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


class DashboardEntry(BaseModel):
    id: str
    timestamp: str
    vehicle_manufacturer: Optional[str]
    vehicle_model: Optional[str]
    catalyst_count: int
    min_price_eur: float
    max_price_eur: float
    note: Optional[str] = None


@router.get("/", response_model=List[DashboardEntry])
async def get_dashboard_entries():
    """Return a list of dashboard entries (mock data).

    The endpoint reads backend/data/dashboard_mock.json and returns it.
    This keeps the implementation free (no external APIs).
    """
    try:
        base = Path(__file__).resolve().parents[3]
        data_file = base / "data" / "dashboard_mock.json"
        if not data_file.exists():
            raise HTTPException(status_code=404, detail="Dashboard mock data not found")
        with data_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
