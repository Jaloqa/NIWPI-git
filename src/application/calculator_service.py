"""
Application Layer: Calculator service that orchestrates operations.
This layer contains the use cases and business workflows.
"""

from typing import Dict, Union
from src.domain.operations import (
    Operation,
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Power,
    Root,
    Sine,
    Cosine,
    Tangent,
)


class CalculatorService:
    """Service class that manages calculator operations."""
    
    def __init__(self):
        """Initialize the calculator service with available operations."""
        self._operations: Dict[str, Operation] = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division(),
            '^': Power(),
            'root': Root(),
            'sin': Sine(),
            'cos': Cosine(),
            'tan': Tangent(),
        }
    
    def calculate(self, a: Union[int, float], operator: str, b: Union[int, float]) -> Union[int, float]:
        """
        Perform a calculation using the specified operator.
        
        Args:
            a: First operand
            operator: Operation symbol (+, -, *, /)
            b: Second operand
            
        Returns:
            Result of the calculation
            
        Raises:
            ValueError: If operator is not supported or if division by zero
        """
        if operator not in self._operations:
            raise ValueError(f"Unsupported operator: {operator}. Supported operators: {', '.join(self._operations.keys())}")
        
        operation = self._operations[operator]
        return operation.execute(a, b)
    
    def get_supported_operators(self) -> list:
        """Return list of supported operators."""
        return list(self._operations.keys())
    
    def add_operation(self, operation: Operation) -> None:
        """
        Add a new operation to the calculator.
        This allows for extensibility.
        
        Args:
            operation: An instance of Operation to add
        """
        self._operations[operation.symbol()] = operation
