"""
Main entry point for the calculator application.
This file wires together all the layers and starts the application.
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.application.calculator_service import CalculatorService
from src.presentation.cli import CalculatorCLI


def main():
    """Main function to start the calculator application."""
    # Dependency injection: Create service and inject into CLI
    calculator_service = CalculatorService()
    calculator_cli = CalculatorCLI(calculator_service)
    
    # Start the application
    calculator_cli.run()


if __name__ == "__main__":
    main()
