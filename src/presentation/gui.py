"""
Presentation Layer: Graphical User Interface for the calculator.
This layer provides a modern GUI using tkinter.
"""

import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.application.calculator_service import CalculatorService


class CalculatorGUI:
    """Modern graphical user interface for the calculator."""
    
    def __init__(self, calculator_service: CalculatorService):
        """
        Initialize the GUI with a calculator service.
        
        Args:
            calculator_service: The calculator service to use
        """
        self.calculator_service = calculator_service
        self.window = tk.Tk()
        self.window.title("Simple Calculator")
        self.window.geometry("400x550")
        self.window.resizable(False, False)
        
        # Variables
        self.display_var = tk.StringVar(value="0")
        self.current_input = ""
        self.first_operand: Optional[float] = None
        self.current_operator: Optional[str] = None
        self.reset_display = False
        self.show_expression = False  # Flag to show full expression
        
        # Configure style
        self._configure_style()
        
        # Create UI elements
        self._create_display()
        self._create_buttons()
        
        # Keyboard bindings
        self._setup_keyboard_bindings()
        
    def _configure_style(self):
        """Configure the visual style of the calculator."""
        self.window.configure(bg='#2C3E50')
        
        style = ttk.Style()
        style.theme_use('clam')
        
    def _create_display(self):
        """Create the display area for showing numbers and results."""
        display_frame = tk.Frame(self.window, bg='#2C3E50', pady=20, padx=20)
        display_frame.pack(fill=tk.BOTH)
        
        # Display label
        display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=('Arial', 32, 'bold'),
            bg='#34495E',
            fg='#ECF0F1',
            anchor='e',
            padx=15,
            pady=15,
            relief=tk.SUNKEN,
            bd=3
        )
        display.pack(fill=tk.BOTH, expand=True)
        
    def _create_buttons(self):
        """Create the calculator buttons."""
        button_frame = tk.Frame(self.window, bg='#2C3E50', padx=20, pady=10)
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Define buttons with their positions (row, col, colspan, text)
        button_definitions = [
            # Row 0
            (0, 0, 1, 'C'), (0, 1, 1, '⌫'), (0, 2, 1, '±'), (0, 3, 1, '/'),
            # Row 1
            (1, 0, 1, '7'), (1, 1, 1, '8'), (1, 2, 1, '9'), (1, 3, 1, '*'),
            # Row 2
            (2, 0, 1, '4'), (2, 1, 1, '5'), (2, 2, 1, '6'), (2, 3, 1, '-'),
            # Row 3
            (3, 0, 1, '1'), (3, 1, 1, '2'), (3, 2, 1, '3'), (3, 3, 1, '+'),
            # Row 4 - 0 button spans 2 columns
            (4, 0, 2, '0'), (4, 2, 1, '.'), (4, 3, 1, '='),
        ]
        
        for row, col, colspan, button_text in button_definitions:
            # Determine button color
            if button_text in ['C', '⌫', '±']:
                bg_color = '#E74C3C'  # Red for special operations
                fg_color = '#FFFFFF'
            elif button_text in ['+', '-', '*', '/', '=']:
                bg_color = '#3498DB'  # Blue for operators
                fg_color = '#FFFFFF'
            else:
                bg_color = '#95A5A6'  # Gray for numbers
                fg_color = '#2C3E50'
            
            btn = tk.Button(
                button_frame,
                text=button_text,
                font=('Arial', 18, 'bold'),
                bg=bg_color,
                fg=fg_color,
                activebackground=self._darken_color(bg_color),
                activeforeground=fg_color,
                relief=tk.RAISED,
                bd=3,
                command=lambda text=button_text: self._on_button_click(text)
            )
            
            btn.grid(
                row=row,
                column=col,
                columnspan=colspan,
                sticky='nsew',
                padx=3,
                pady=3
            )
        
        # Configure grid weights for responsive layout
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def _darken_color(self, hex_color: str) -> str:
        """Darken a hex color for active state."""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        darkened = tuple(max(0, int(c * 0.8)) for c in rgb)
        return '#{:02x}{:02x}{:02x}'.format(*darkened)
    
    def _setup_keyboard_bindings(self):
        """Setup keyboard shortcuts."""
        self.window.bind('<Key>', self._on_key_press)
        self.window.bind('<Return>', lambda e: self._on_button_click('='))
        self.window.bind('<Escape>', lambda e: self._on_button_click('C'))
        self.window.bind('<BackSpace>', lambda e: self._on_button_click('⌫'))
    
    def _on_key_press(self, event):
        """Handle keyboard input."""
        key = event.char
        
        if key.isdigit() or key == '.':
            self._on_button_click(key)
        elif key in ['+', '-', '*', '/']:
            self._on_button_click(key)
        elif key.lower() == 'c':
            self._on_button_click('C')
    
    def _on_button_click(self, button_text: str):
        """
        Handle button click events.
        
        Args:
            button_text: The text of the clicked button
        """
        try:
            if button_text.isdigit():
                self._handle_digit(button_text)
            elif button_text == '.':
                self._handle_decimal()
            elif button_text in ['+', '-', '*', '/']:
                self._handle_operator(button_text)
            elif button_text == '=':
                self._handle_equals()
            elif button_text == 'C':
                self._handle_clear()
            elif button_text == '⌫':
                self._handle_backspace()
            elif button_text == '±':
                self._handle_sign_change()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self._handle_clear()
    
    def _handle_digit(self, digit: str):
        """Handle digit button press."""
        if self.reset_display:
            self.current_input = digit
            self.reset_display = False
            self.show_expression = False
        else:
            if self.current_input == "0":
                self.current_input = digit
            else:
                self.current_input += digit
        self._update_display()
    
    def _handle_decimal(self):
        """Handle decimal point button press."""
        if self.reset_display:
            self.current_input = "0."
            self.reset_display = False
            self.show_expression = False
        elif '.' not in self.current_input:
            if not self.current_input:
                self.current_input = "0."
            else:
                self.current_input += '.'
        self._update_display()
    
    def _handle_operator(self, operator: str):
        """Handle operator button press."""
        if self.current_input:
            current_value = self._parse_number(self.current_input)
            
            if self.first_operand is not None and self.current_operator and not self.reset_display:
                # Chain operations
                result = self.calculator_service.calculate(
                    self.first_operand,
                    self.current_operator,
                    current_value
                )
                self.first_operand = result
                self.current_input = str(result)
            else:
                self.first_operand = current_value
            
            self.current_operator = operator
            self.reset_display = True
            self.show_expression = True
            
            # Show the expression in display
            self._update_display_with_operator()
    
    def _handle_equals(self):
        """Handle equals button press."""
        if self.first_operand is not None and self.current_operator and self.current_input:
            try:
                current_value = self._parse_number(self.current_input)
                result = self.calculator_service.calculate(
                    self.first_operand,
                    self.current_operator,
                    current_value
                )
                
                # Format result
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                
                self.current_input = str(result)
                
                # Reset for next calculation
                self.first_operand = None
                self.current_operator = None
                self.reset_display = True
                self.show_expression = False
                self._update_display()
                
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                self._handle_clear()
    
    def _handle_clear(self):
        """Handle clear button press."""
        self.current_input = ""
        self.first_operand = None
        self.current_operator = None
        self.reset_display = False
        self.show_expression = False
        self.display_var.set("0")
    
    def _handle_backspace(self):
        """Handle backspace button press."""
        if self.current_input and not self.reset_display:
            self.current_input = self.current_input[:-1]
            if not self.current_input:
                self.current_input = "0"
            self._update_display()
    
    def _handle_sign_change(self):
        """Handle sign change button press."""
        if self.current_input and self.current_input != "0":
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
            self._update_display()
    
    def _update_display(self):
        """Update the display with the current input."""
        if self.show_expression and self.first_operand is not None and self.current_operator:
            # Don't update if we're showing the expression
            return
            
        display_text = self.current_input if self.current_input else "0"
        
        # Limit display length
        if len(display_text) > 15:
            display_text = display_text[:15]
            self.current_input = display_text
        
        self.display_var.set(display_text)
    
    def _update_display_with_operator(self):
        """Update display to show the expression with operator."""
        if self.first_operand is not None and self.current_operator:
            # Format the first operand
            first_op_str = str(int(self.first_operand) if isinstance(self.first_operand, float) and self.first_operand.is_integer() else self.first_operand)
            
            # Show expression like "5 +"
            expression = f"{first_op_str} {self.current_operator}"
            self.display_var.set(expression)
    
    @staticmethod
    def _parse_number(value: str) -> float:
        """
        Parse a string to a number.
        
        Args:
            value: String representation of a number
            
        Returns:
            Parsed number as float
        """
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"'{value}' is not a valid number")
    
    def run(self):
        """Start the GUI application."""
        # Center the window on screen
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
        
        self.window.mainloop()
