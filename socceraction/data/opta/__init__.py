"""Module for loading Opta event data."""

__all__ = [
    'OptaLoader',
    'OptaCompetitionSchema',
    'OptaGameSchema',
    'OptaPlayerSchema',
    'OptaTeamSchema',
    'OptaEventSchema',
]

from .loader import OptaLoader, _eventtypesdf
from .schema import (
    OptaCompetitionSchema,
    OptaEventSchema,
    OptaGameSchema,
    OptaPlayerSchema,
    OptaTeamSchema,
)
