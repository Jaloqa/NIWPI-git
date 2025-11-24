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
        self._unary_operators = {'sin', 'cos', 'tan'}
    
    def run(self) -> None:
        """Run the calculator CLI in interactive mode."""
        print("=" * 50)
        print("Simple Calculator")
        print("=" * 50)
        print(f"Supported operators: {', '.join(self.calculator_service.get_supported_operators())}")
        print("Use 'root' for nth root (e.g., 9 root 2) and '^' for power (e.g., 2 ^ 3)")
        print("Use 'sin', 'cos', 'tan' for trigonometry (angles in degrees), e.g., sin 30")
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
        
        try:
            if len(parts) == 2:
                first, second = parts[0].lower(), parts[1].lower()
                if first in self._unary_operators:
                    operator = first
                    a = self._parse_number(parts[1])
                    b = 0
                elif second in self._unary_operators:
                    operator = second
                    a = self._parse_number(parts[0])
                    b = 0
                else:
                    print("Invalid input format. Examples: sin 30 | cos 45 | 5 + 3 | 9 root 2")
                    return None
            elif len(parts) == 3:
                a = self._parse_number(parts[0])
                operator = parts[1].lower()
                b = self._parse_number(parts[2])
            else:
                print("Invalid input format. Examples: sin 30 | cos 45 | 5 + 3 | 9 root 2")
                return None

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
