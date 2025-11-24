"""Unit tests for GUI presentation layer."""

import sys
from pathlib import Path
import unittest
from unittest.mock import Mock, patch

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.application.calculator_service import CalculatorService


class TestCalculatorGUILogic(unittest.TestCase):
    """Test cases for CalculatorGUI logic (without actual GUI rendering)."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.service = CalculatorService()
    
    def test_number_parsing(self):
        """Test number parsing functionality."""
        # Import here to avoid GUI creation
        from src.presentation.gui import CalculatorGUI
        
        # Test integer parsing
        self.assertEqual(CalculatorGUI._parse_number("5"), 5.0)
        self.assertEqual(CalculatorGUI._parse_number("123"), 123.0)
        
        # Test float parsing
        self.assertEqual(CalculatorGUI._parse_number("5.5"), 5.5)
        self.assertEqual(CalculatorGUI._parse_number("0.123"), 0.123)
        
        # Test negative numbers
        self.assertEqual(CalculatorGUI._parse_number("-5"), -5.0)
        self.assertEqual(CalculatorGUI._parse_number("-5.5"), -5.5)
    
    def test_number_parsing_invalid(self):
        """Test number parsing with invalid input."""
        from src.presentation.gui import CalculatorGUI
        
        with self.assertRaises(ValueError):
            CalculatorGUI._parse_number("abc")
        
        with self.assertRaises(ValueError):
            CalculatorGUI._parse_number("")
    
    def test_service_integration(self):
        """Test that GUI can use calculator service."""
        # Test basic operations
        self.assertEqual(self.service.calculate(5, '+', 3), 8)
        self.assertEqual(self.service.calculate(10, '-', 4), 6)
        self.assertEqual(self.service.calculate(6, '*', 7), 42)
        self.assertEqual(self.service.calculate(20, '/', 4), 5.0)
    
    def test_chained_operations(self):
        """Test chained calculator operations."""
        # Simulate: 5 + 3 = 8, then 8 * 2 = 16
        result1 = self.service.calculate(5, '+', 3)
        self.assertEqual(result1, 8)
        
        result2 = self.service.calculate(result1, '*', 2)
        self.assertEqual(result2, 16)
    
    def test_decimal_operations(self):
        """Test operations with decimal numbers."""
        result = self.service.calculate(5.5, '+', 4.5)
        self.assertEqual(result, 10.0)
        
        result = self.service.calculate(7.5, '*', 2.0)
        self.assertEqual(result, 15.0)
    
    def test_division_by_zero_handling(self):
        """Test division by zero error handling."""
        with self.assertRaises(ValueError) as context:
            self.service.calculate(10, '/', 0)
        self.assertIn("Cannot divide by zero", str(context.exception))


if __name__ == '__main__':
    unittest.main()
