"""
Domain Layer: Core business logic for calculator operations.
This layer contains the fundamental calculator operations without any dependencies.
"""

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
        return a + b  # tu była zmianka na minusika
    
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
