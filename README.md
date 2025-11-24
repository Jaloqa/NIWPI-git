# Simple Calculator

A well-architected calculator application built with Python following clean architecture principles and SOLID design patterns.

## Architecture

This project follows a **layered architecture** with clear separation of concerns:

### 1. Domain Layer (`src/domain/`)
- Contains core business logic and entities
- Independent of external dependencies
- Defines calculator operations using the Strategy pattern
- **Files:**
  - `operations.py`: Abstract Operation class and concrete implementations (Addition, Subtraction, Multiplication, Division)

### 2. Application Layer (`src/application/`)
- Contains use cases and business workflows
- Orchestrates domain objects
- Implements the Calculator Service
- **Files:**
  - `calculator_service.py`: Service that manages operations and performs calculations

### 3. Presentation Layer (`src/presentation/`)
- Handles user interaction and I/O
- Independent of business logic
- Can be easily replaced with different UIs (CLI, GUI, Web API)
- **Files:**
  - `cli.py`: Command-line interface implementation
  - `gui.py`: Graphical user interface (tkinter-based)

## Design Patterns Used

1. **Strategy Pattern**: Each operation (Addition, Subtraction, etc.) is a separate strategy
2. **Dependency Injection**: Layers depend on abstractions, not concrete implementations
3. **Single Responsibility Principle**: Each class has one reason to change
4. **Open/Closed Principle**: Easy to extend with new operations without modifying existing code

## Project Structure

```
NIWPI-git/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Application entry point (CLI/GUI)
│   ├── main_gui.py             # GUI-specific entry point
│   ├── domain/                 # Core business logic
│   │   ├── __init__.py
│   │   └── operations.py
│   ├── application/            # Use cases and services
│   │   ├── __init__.py
│   │   └── calculator_service.py
│   └── presentation/           # User interface
│       ├── __init__.py
│       ├── cli.py              # Command-line interface
│       └── gui.py              # Graphical interface
├── tests/                      # Unit tests
│   ├── __init__.py
│   ├── test_operations.py
│   ├── test_calculator_service.py
│   └── test_gui.py
└── README.md
```

## Features

- ✅ Basic arithmetic operations (+, -, *, /)
- ✅ Support for integers and floating-point numbers
- ✅ Division by zero protection
- ✅ Extensible architecture (easy to add new operations)
- ✅ Comprehensive unit tests
- ✅ **Interactive CLI**
- ✅ **Modern GUI with tkinter**
- ✅ Keyboard support in GUI (numbers, operators, Enter, Escape, Backspace)
- ✅ Chain operations support
- ✅ Sign change (±) functionality
- ✅ Visual feedback and error handling

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd NIWPI-git
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Usage

### Running the Calculator

**CLI Mode (default):**
```bash
python -m src.main
# or
python src/main.py
```

**GUI Mode:**
```bash
python -m src.main --gui
# or
python src/main_gui.py
```

### CLI Example Session

```
==================================================
Simple Calculator
==================================================
Supported operators: +, -, *, /
Type 'quit' or 'exit' to exit the calculator
==================================================

Enter calculation (e.g., 5 + 3): 10 + 5
Result: 15

Enter calculation (e.g., 5 + 3): 20 / 4
Result: 5.0

Enter calculation (e.g., 5 + 3): 7.5 * 2
Result: 15.0

Enter calculation (e.g., 5 + 3): quit
Thank you for using the calculator. Goodbye!
```

### GUI Features

The GUI calculator provides:

- **Visual Calculator Interface**: Clean, modern design with color-coded buttons
- **Button Layout**:
  - Number pad (0-9)
  - Decimal point (.)
  - Operators (+, -, *, /)
  - Special functions (C=Clear, ⌫=Backspace, ±=Sign change)
  - Equals (=) for results
- **Keyboard Support**:
  - Type numbers and operators directly
  - Enter key for equals
  - Escape key for clear
  - Backspace for deletion
- **Chain Operations**: Continue calculating without clearing
- **Error Handling**: User-friendly error messages
- **Responsive Layout**: Buttons adapt to clicks with visual feedback

## Running Tests

Run all tests:
```bash
python -m unittest discover tests
```

Run specific test file:
```bash
python -m unittest tests.test_operations
python -m unittest tests.test_calculator_service
python -m unittest tests.test_gui
```

## Extending the Calculator

To add a new operation:

1. Create a new class in `src/domain/operations.py` that inherits from `Operation`
2. Implement the `execute()` and `symbol()` methods
3. Add the operation to `CalculatorService` (or use `add_operation()` method)

Example:
```python
class Power(Operation):
    def execute(self, a, b):
        return a ** b
    
    def symbol(self):
        return "^"
```

## Benefits of This Architecture

1. **Testability**: Each layer can be tested independently
2. **Maintainability**: Clear separation of concerns makes code easy to understand and modify
3. **Extensibility**: New operations can be added without changing existing code
4. **Flexibility**: Easy to add different UIs (web, GUI) without touching business logic
5. **Reusability**: Core business logic can be reused across different applications

## License

This project is open source and available under the MIT License.
