"""Catalyst Data Models."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CatalystBase(BaseModel):
    """Base Catalyst Model."""

    part_number: str = Field(
        ..., description="Herstellerteilnummer (z.B. GM28, 174-900)"
    )
    vehicle_id: int = Field(..., description="Zugehörige Fahrzeug-ID")
    location: str = Field(
        ..., description="Einbauort (unterboden, kruemmer, motorraum)"
    )
    platinum_grams: float = Field(
        default=0.0, description="Platin-Gehalt in Gramm"
    )
    palladium_grams: float = Field(
        default=0.0, description="Palladium-Gehalt in Gramm"
    )
    rhodium_grams: float = Field(
        default=0.0, description="Rhodium-Gehalt in Gramm"
    )
    base_value_eur: Optional[float] = Field(
        None, description="Basiswert ohne Edelmetallkurs-Anpassung"
    )
    current_price_eur: Optional[float] = Field(
        None, description="Aktueller Preis (mit Kurs-Anpassung)"
    )
    source: Optional[str] = Field(
        None, description="Datenquelle (z.B. Ankaufseite)"
    )


class CatalystCreate(CatalystBase):
    """Catalyst Create Schema."""

    pass


class Catalyst(CatalystBase):
    """Catalyst Database Model."""

    id: int = Field(..., description="Eindeutige Katalysator-ID")
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic Config."""

        from_attributes = True


class CatalystResponse(BaseModel):
    """Catalyst Response Schema."""

    id: int
    part_number: str
    vehicle_id: int
    location: str
    platinum_grams: float
    palladium_grams: float
    rhodium_grams: float
    base_value_eur: Optional[float]
    current_price_eur: Optional[float]
    source: Optional[str]


class CatalystAggregation(BaseModel):
    """Aggregated Catalyst Data for Response."""

    vehicle_manufacturer: str
    vehicle_model: str
    vehicle_generation: str
    catalyst_count: int = Field(..., description="Anzahl gültiger Katalysatoren")
    min_price_eur: float = Field(..., description="Minimaler Preis")
    max_price_eur: float = Field(..., description="Maximaler Preis")
    catalysts: list[CatalystResponse] = Field(
        ..., description="Liste der Katalysator-Details"
    )
