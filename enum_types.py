"""
module enum_types.py

This module implements all enums required for this API.
"""

from enum import Enum

class DriverArchitecture(Enum):
    BIT_32 = 32
    BIT_64 = 64