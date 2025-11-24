"""
Domain Layer: Core business logic for calculator operations.
This layer contains the fundamental calculator operations without any dependencies.
"""

import math
from abc import ABC, abstractmethod
from typing import Union


class Operation(ABC):
    """Abstract base class for all calculator operations."""
    
    @abstractmethod
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Execute the operation on two numbers."""
        pass
    
    @abstractmethod
    def symbol(self) -> str:
        """Return the symbol representing this operation."""
        pass


class Addition(Operation):
    """Addition operation."""
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b
    
    def symbol(self) -> str:
        return "+"


class Subtraction(Operation):
    """Subtraction operation."""
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a - b
    
    def symbol(self) -> str:
        return "-"


class Multiplication(Operation):
    """Multiplication operation."""
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b
    
    def symbol(self) -> str:
        return "*"


class Division(Operation):
    """Division operation."""
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def symbol(self) -> str:
        return "/"


class Power(Operation):
    """Exponentiation operation."""

    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a ** b

    def symbol(self) -> str:
        return "^"


class Root(Operation):
    """Root extraction operation (nth root)."""

    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if b == 0:
            raise ValueError("Root degree cannot be zero")
        if a < 0:
            raise ValueError("Cannot extract root of negative number")
        return a ** (1 / b)

    def symbol(self) -> str:
        return "root"


class Sine(Operation):
    """Sine operation (degrees)."""

    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        radians = math.radians(a)
        return math.sin(radians)

    def symbol(self) -> str:
        return "sin"


class Cosine(Operation):
    """Cosine operation (degrees)."""

    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        radians = math.radians(a)
        return math.cos(radians)

    def symbol(self) -> str:
        return "cos"


class Tangent(Operation):
    """Tangent operation (degrees)."""

    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        radians = math.radians(a)
        if abs(math.cos(radians)) < 1e-12:
            raise ValueError("Tangent is undefined for angles where cosine is zero (90° + k*180°)")
        return math.tan(radians)

    def symbol(self) -> str:
        return "tan"
