"""Helper Utility Functions."""

import re
from typing import Optional, Tuple


def normalize_part_number(part_number: str) -> str:
    """
    Normalize catalyst part number.

    Args:
        part_number: Raw part number string

    Returns:
        Normalized part number (uppercase, trimmed)
    """
    return part_number.upper().strip()


def validate_part_number(part_number: str) -> bool:
    """
    Validate part number format.

    Regex pattern: 2-4 alphanumeric characters followed by 3-7 digits
    Examples: GM28, 174-900, 6N0, BOSC123456

    Args:
        part_number: Part number to validate

    Returns:
        True if valid format
    """
    pattern = r"^[A-Z0-9]{2,4}[\s-]?[0-9]{3,7}$"
    return bool(re.match(pattern, part_number.upper()))


def extract_vehicle_info(
    query: str,
) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Extract vehicle manufacturer, model from natural language query.

    Examples:
    - "Was bringt der Kat vom BMW E46 328i?" -> ("BMW", "E46", "328i")
    - "VW Polo 6N" -> ("VW", "Polo", "6N")

    Args:
        query: Natural language query

    Returns:
        Tuple of (manufacturer, model, variant)
    """
    # Placeholder for NLP extraction
    # TODO: Implement sophisticated NLP parsing
    query_upper = query.upper()
    manufacturer = None
    model = None
    variant = None

    # Simple keyword matching
    manufacturers = {"BMW": "BMW", "VW": "VW", "VOLKSWAGEN": "VW", "AUDI": "AUDI",
                    "MERCEDES": "Mercedes", "FORD": "Ford", "GM": "GM"}
    for key, value in manufacturers.items():
        if key in query_upper:
            manufacturer = value
            break

    return manufacturer, model, variant
