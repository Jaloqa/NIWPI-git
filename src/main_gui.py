"""
Main entry point for the calculator GUI application.
This file wires together all the layers and starts the GUI.
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.application.calculator_service import CalculatorService
from src.presentation.gui import CalculatorGUI


def main():
    """Main function to start the calculator GUI application."""
    # Dependency injection: Create service and inject into GUI
    calculator_service = CalculatorService()
    calculator_gui = CalculatorGUI(calculator_service)
    
    # Start the application
    calculator_gui.run()


if __name__ == "__main__":
    main()
