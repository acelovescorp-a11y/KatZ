"""Business Rules Filter Engine."""

import logging
from typing import List, Dict, Any, Tuple

logger = logging.getLogger(__name__)


class BusinessRulesFilter:
    """Strict business rules filter for catalyst selection."""

    def __init__(
        self,
        min_price_eur: float = 250.00,
        allowed_locations: List[str] = None,
    ):
        """
        Initialize Business Rules Filter.

        Args:
            min_price_eur: Minimum price threshold in EUR
            allowed_locations: List of allowed installation locations
        """
        self.min_price_eur = min_price_eur
        self.allowed_locations = allowed_locations or [
            "unterboden",
            "unterboden-katalysator",
        ]
        logger.info(
            f"BusinessRulesFilter initialized (min_price={min_price_eur}EUR, "
            f"locations={self.allowed_locations})"
        )

    def filter_catalysts(
        self,
        catalysts: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """
        Apply business filters to catalysts.

        Filters:
        1. Location filter: Only 'unterboden' location
        2. Price filter: Price >= min_price_eur

        Args:
            catalysts: List of catalyst dictionaries

        Returns:
            Filtered list of catalysts
        """
        logger.info(f"Filtering {len(catalysts)} catalysts")

        filtered = []
        for catalyst in catalysts:
            # Filter 1: Check location
            location = catalyst.get("location", "").lower().strip()
            if location not in self.allowed_locations:
                logger.debug(
                    f"Catalyst {catalyst.get('part_number')} filtered out: "
                    f"location '{location}' not allowed"
                )
                continue

            # Filter 2: Check price
            price = catalyst.get("current_price_eur") or catalyst.get("base_value_eur", 0)
            if price < self.min_price_eur:
                logger.debug(
                    f"Catalyst {catalyst.get('part_number')} filtered out: "
                    f"price {price}EUR < {self.min_price_eur}EUR"
                )
                continue

            filtered.append(catalyst)
            logger.debug(
                f"Catalyst {catalyst.get('part_number')} PASSED filters "
                f"(location={location}, price={price}EUR)"
            )

        logger.info(f"Filtering result: {len(filtered)}/{len(catalysts)} catalysts passed")
        return filtered

    def aggregate_catalyst_prices(
        self,
        catalysts: List[Dict[str, Any]],
    ) -> Tuple[int, float, float]:
        """
        Aggregate filtered catalysts to price range.

        Args:
            catalysts: Filtered catalyst list

        Returns:
            Tuple of (count, min_price, max_price)
        """
        if not catalysts:
            return 0, 0.0, 0.0

        prices = [
            catalyst.get("current_price_eur") or catalyst.get("base_value_eur", 0)
            for catalyst in catalysts
        ]
        prices = [p for p in prices if p > 0]  # Remove zero prices

        if not prices:
            return len(catalysts), 0.0, 0.0

        return len(catalysts), min(prices), max(prices)
