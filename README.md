# Calculator-using-postfix-notation

A simple calculator implementation that converts standard infix expressions to postfix notation for evaluation. This repository includes three versions: a command-line interface and two GUI applications with increasing functionality.

## Demonstration video

[![Calculator Demo](https://img.youtube.com/vi/OOwUB-HDook/0.jpg)](https://www.youtube.com/watch?v=OOwUB-HDook)

## Overview

These calculators convert familiar infix expressions (like `3 + 4`) to postfix notation (like `3 4 +`) behind the scenes, making operator precedence handling more straightforward. The applications support basic arithmetic operations, parentheses, and exponents.

## Files in this Repository

1. **calculator-v1.py** - Command-line calculator
2. **calculator-v2.py** - Basic GUI calculator
3. **calculator-v3.py** - Enhanced GUI calculator with separate expression and result displays

## Implementation Details

### Postfix Calculator Class

All implementations share the same core `PostfixCalculator` class with two main methods:

- **infix_to_postfix(expression)** - Converts an infix expression to postfix notation using the shunting yard algorithm
- **evaluate_postfix(postfix)** - Evaluates a postfix expression and returns the result

The calculator supports the following operations:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Exponentiation (^)
- Parentheses for grouping

### Command-Line Version (calculator-v1.py)

- Simple interactive command-line interface
- Enter expressions and see their postfix representation and result
- Type 'q' to quit

#### Usage:
```
python calculator-v1.py
```

### Basic GUI Version (calculator-v2.py)

- Tkinter-based graphical user interface
- Single display for both input and output
- Calculator buttons for digits and operations

#### Usage:
```
python calculator-v2.py
```

### Enhanced GUI Version (calculator-v3.py)

- Improved Tkinter-based interface
- Separate displays for expression input and result output
- Larger font for better readability

#### Usage:
```
python calculator-v3.py
```

## How It Works

1. **Conversion to Postfix**: The calculator first converts the infix expression to postfix notation using the shunting yard algorithm:
   - Numbers are directly added to output
   - Operators are pushed to a stack and popped based on precedence
   - Parentheses manage operator precedence

2. **Evaluation**: The postfix expression is evaluated using a stack:
   - Numbers are pushed onto the stack
   - When an operator is encountered, operands are popped, the operation is performed, and the result is pushed back

## Error Handling

The calculator handles common errors such as:
- Division by zero
- Invalid expressions
- Mismatched parentheses

## Requirements

- Python 3.x
- Tkinter (for GUI versions, usually included with Python)
