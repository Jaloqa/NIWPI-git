"""Unit tests for application layer calculator service."""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import unittest
from src.application.calculator_service import CalculatorService
from src.domain.operations import Operation


class MockPowerOperation(Operation):
    """Mock operation for testing extensibility."""
    
    def execute(self, a, b):
        return a ** b
    
    def symbol(self):
        return "^"


class TestCalculatorService(unittest.TestCase):
    """Test cases for CalculatorService."""
    
    def setUp(self):
        self.service = CalculatorService()
    
    def test_calculate_addition(self):
        result = self.service.calculate(5, '+', 3)
        self.assertEqual(result, 8)
    
    def test_calculate_subtraction(self):
        result = self.service.calculate(5, '-', 3)
        self.assertEqual(result, 2)
    
    def test_calculate_multiplication(self):
        result = self.service.calculate(5, '*', 3)
        self.assertEqual(result, 15)
    
    def test_calculate_division(self):
        result = self.service.calculate(6, '/', 3)
        self.assertEqual(result, 2)

    def test_calculate_power(self):
        result = self.service.calculate(2, '^', 3)
        self.assertEqual(result, 8)

    def test_calculate_root(self):
        result = self.service.calculate(9, 'root', 2)
        self.assertEqual(result, 3.0)
    
    def test_calculate_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            self.service.calculate(5, '/', 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_calculate_unsupported_operator(self):
        with self.assertRaises(ValueError) as context:
            self.service.calculate(5, '%', 3)
        self.assertIn("Unsupported operator", str(context.exception))
    
    def test_get_supported_operators(self):
        operators = self.service.get_supported_operators()
        self.assertEqual(set(operators), {'+', '-', '*', '/', '^', 'root'})
    
    def test_add_custom_operation(self):
        # Test extensibility by adding a new operation
        power_op = MockPowerOperation()
        self.service.add_operation(power_op)
        
        result = self.service.calculate(2, '^', 3)
        self.assertEqual(result, 8)
        
        operators = self.service.get_supported_operators()
        self.assertIn('^', operators)


if __name__ == '__main__':
    unittest.main()
