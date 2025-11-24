"""
Presentation Layer: Command-line interface for the calculator.
This layer handles user interaction and input/output.
"""

from typing import Union
from src.application.calculator_service import CalculatorService


class CalculatorCLI:
    """Command-line interface for the calculator."""
    
    def __init__(self, calculator_service: CalculatorService):
        """
        Initialize the CLI with a calculator service.
        
        Args:
            calculator_service: The calculator service to use
        """
        self.calculator_service = calculator_service
    
    def run(self) -> None:
        """Run the calculator CLI in interactive mode."""
        print("=" * 50)
        print("Simple Calculator")
        print("=" * 50)
        print(f"Supported operators: {', '.join(self.calculator_service.get_supported_operators())}")
        print("Type 'quit' or 'exit' to exit the calculator")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\nEnter calculation (e.g., 5 + 3): ").strip()
                
                if user_input.lower() in ['quit', 'exit']:
                    print("Thank you for using the calculator. Goodbye!")
                    break
                
                result = self._process_input(user_input)
                if result is not None:
                    print(f"Result: {result}")
                    
            except KeyboardInterrupt:
                print("\n\nExiting calculator...")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def _process_input(self, user_input: str) -> Union[int, float, None]:
        """
        Process user input and calculate result.
        
        Args:
            user_input: Raw user input string
            
        Returns:
            Calculation result or None if input is invalid
        """
        parts = user_input.split()
        
        if len(parts) != 3:
            print("Invalid input format. Please use format: number operator number")
            print("Example: 5 + 3")
            return None
        
        try:
            a = self._parse_number(parts[0])
            operator = parts[1]
            b = self._parse_number(parts[2])
            
            return self.calculator_service.calculate(a, operator, b)
            
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None
    
    @staticmethod
    def _parse_number(value: str) -> Union[int, float]:
        """
        Parse a string to a number (int or float).
        
        Args:
            value: String representation of a number
            
        Returns:
            Parsed number as int or float
            
        Raises:
            ValueError: If value cannot be parsed as a number
        """
        try:
            # Try to parse as int first
            if '.' not in value:
                return int(value)
            return float(value)
        except ValueError:
            raise ValueError(f"'{value}' is not a valid number")
