"""Vehicle Data Models."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class VehicleBase(BaseModel):
    """Base Vehicle Model."""

    manufacturer: str = Field(..., description="Fahrzeughersteller (z.B. VW, BMW)")
    model: str = Field(..., description="Fahrzeugmodell (z.B. Polo, 3er)")
    generation: str = Field(
        ..., description="Baureihe/Generation (z.B. 6N, E46)"
    )
    year_from: int = Field(
        ..., description="Produktionsbeginn"
    )
    year_to: Optional[int] = Field(
        None, description="Produktionsende"
    )
    engine_variants: Optional[str] = Field(
        None, description="Motor-Varianten (z.B. 1.0, 1.2, 1.6)"
    )


class VehicleCreate(VehicleBase):
    """Vehicle Create Schema."""

    pass


class Vehicle(VehicleBase):
    """Vehicle Database Model."""

    id: int = Field(..., description="Eindeutige Fahrzeug-ID")
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic Config."""

        from_attributes = True


class VehicleResponse(BaseModel):
    """Vehicle Response Schema."""

    id: int
    manufacturer: str
    model: str
    generation: str
    year_from: int
    year_to: Optional[int]
    engine_variants: Optional[str]
