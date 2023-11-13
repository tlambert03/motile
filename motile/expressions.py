from __future__ import annotations

from enum import IntEnum, auto

from ilpy.expressions import Constant, Expression, Variable


class VariableType(IntEnum):
    """Type of a variable."""

    Continuous = 0
    Integer = auto()
    Binary = auto()


__all__ = ["Expression", "Variable", "Constant"]
