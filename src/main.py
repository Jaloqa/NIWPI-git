"""
Main entry point for the calculator application.
This file wires together all the layers and starts the application.
Supports both CLI and GUI modes.
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.application.calculator_service import CalculatorService
from src.presentation.cli import CalculatorCLI
from src.presentation.gui import CalculatorGUI


def main():
    """Main function to start the calculator application."""
    # Check command line arguments for mode selection
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        # Start GUI mode
        calculator_service = CalculatorService()
        calculator_gui = CalculatorGUI(calculator_service)
        calculator_gui.run()
    else:
        # Start CLI mode (default)
        calculator_service = CalculatorService()
        calculator_cli = CalculatorCLI(calculator_service)
        calculator_cli.run()


if __name__ == "__main__":
    main()
