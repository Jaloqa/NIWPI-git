"""Unit tests for domain layer operations."""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import unittest
from src.domain.operations import Addition, Subtraction, Multiplication, Division, Power, Root


class TestAddition(unittest.TestCase):
    """Test cases for Addition operation."""
    
    def setUp(self):
        self.operation = Addition()
    
    def test_addition_positive_numbers(self):
        result = self.operation.execute(5, 3)
        self.assertEqual(result, 8)
    
    def test_addition_negative_numbers(self):
        result = self.operation.execute(-5, -3)
        self.assertEqual(result, -8)
    
    def test_addition_mixed_numbers(self):
        result = self.operation.execute(5, -3)
        self.assertEqual(result, 2)
    
    def test_addition_floats(self):
        result = self.operation.execute(5.5, 3.2)
        self.assertAlmostEqual(result, 8.7)
    
    def test_symbol(self):
        self.assertEqual(self.operation.symbol(), "+")


class TestSubtraction(unittest.TestCase):
    """Test cases for Subtraction operation."""
    
    def setUp(self):
        self.operation = Subtraction()
    
    def test_subtraction_positive_numbers(self):
        result = self.operation.execute(5, 3)
        self.assertEqual(result, 2)
    
    def test_subtraction_negative_result(self):
        result = self.operation.execute(3, 5)
        self.assertEqual(result, -2)
    
    def test_subtraction_floats(self):
        result = self.operation.execute(5.5, 3.2)
        self.assertAlmostEqual(result, 2.3)
    
    def test_symbol(self):
        self.assertEqual(self.operation.symbol(), "-")


class TestMultiplication(unittest.TestCase):
    """Test cases for Multiplication operation."""
    
    def setUp(self):
        self.operation = Multiplication()
    
    def test_multiplication_positive_numbers(self):
        result = self.operation.execute(5, 3)
        self.assertEqual(result, 15)
    
    def test_multiplication_by_zero(self):
        result = self.operation.execute(5, 0)
        self.assertEqual(result, 0)
    
    def test_multiplication_negative_numbers(self):
        result = self.operation.execute(-5, -3)
        self.assertEqual(result, 15)
    
    def test_multiplication_floats(self):
        result = self.operation.execute(5.5, 2)
        self.assertAlmostEqual(result, 11.0)
    
    def test_symbol(self):
        self.assertEqual(self.operation.symbol(), "*")


class TestDivision(unittest.TestCase):
    """Test cases for Division operation."""
    
    def setUp(self):
        self.operation = Division()
    
    def test_division_positive_numbers(self):
        result = self.operation.execute(6, 3)
        self.assertEqual(result, 2)
    
    def test_division_with_remainder(self):
        result = self.operation.execute(7, 2)
        self.assertEqual(result, 3.5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            self.operation.execute(5, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_division_floats(self):
        result = self.operation.execute(5.5, 2.5)
        self.assertAlmostEqual(result, 2.2)
    
    def test_symbol(self):
        self.assertEqual(self.operation.symbol(), "/")


class TestPower(unittest.TestCase):
    """Test cases for Power operation."""

    def setUp(self):
        self.operation = Power()

    def test_power_positive_numbers(self):
        result = self.operation.execute(2, 3)
        self.assertEqual(result, 8)

    def test_power_with_zero_exponent(self):
        result = self.operation.execute(5, 0)
        self.assertEqual(result, 1)

    def test_power_negative_exponent(self):
        result = self.operation.execute(2, -1)
        self.assertEqual(result, 0.5)

    def test_symbol(self):
        self.assertEqual(self.operation.symbol(), "^")


class TestRoot(unittest.TestCase):
    """Test cases for Root operation."""

    def setUp(self):
        self.operation = Root()

    def test_square_root(self):
        result = self.operation.execute(9, 2)
        self.assertEqual(result, 3.0)

    def test_cube_root(self):
        result = self.operation.execute(27, 3)
        self.assertEqual(result, 3.0)

    def test_root_degree_zero(self):
        with self.assertRaises(ValueError) as context:
            self.operation.execute(4, 0)
        self.assertIn("Root degree cannot be zero", str(context.exception))

    def test_root_negative_number(self):
        with self.assertRaises(ValueError) as context:
            self.operation.execute(-8, 3)
        self.assertIn("Cannot extract root of negative number", str(context.exception))

    def test_symbol(self):
        self.assertEqual(self.operation.symbol(), "root")


if __name__ == '__main__':
    unittest.main()
