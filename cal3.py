import tkinter as tk
from tkinter import ttk

class PostfixCalculator:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def infix_to_postfix(self, expression):
        stack = []
        output = []
        
        for char in expression.replace(" ", ""):
            if char.isdigit():
                output.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop() if stack else None
            else:
                while (stack and stack[-1] != '(' and 
                       self.precedence.get(stack[-1], 0) >= self.precedence.get(char, 0)):
                    output.append(stack.pop())
                stack.append(char)
        
        while stack:
            output.append(stack.pop())
            
        return ' '.join(output)

    def evaluate_postfix(self, postfix):
        stack = []
        
        for token in postfix.split():
            if token.isdigit():
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ValueError("Division by zero")
                    stack.append(a / b)
                elif token == '^':
                    stack.append(a ** b)
                    
        return stack[0]

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.calc = PostfixCalculator()
        
        style = ttk.Style()
        style.configure('Calculator.TButton', padding=10)
        
        # Expression display
        self.expression_var = tk.StringVar()
        expression_display = ttk.Entry(root, textvariable=self.expression_var, justify='right', font=('Arial', 16))
        expression_display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=2)
        
        # Result display
        self.result_var = tk.StringVar()
        result_display = ttk.Entry(root, textvariable=self.result_var, justify='right', font=('Arial', 24, 'bold'))
        result_display.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=5, pady=2)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '(', ')', '+',
            'C', '^', '='
        ]
        
        row = 2
        col = 0
        for button in buttons:
            if button == '=':
                cmd = self.calculate
                btn = ttk.Button(root, text=button, command=cmd, style='Calculator.TButton')
                btn.grid(row=row, column=col, columnspan=2, sticky='nsew', padx=2, pady=2)
            else:
                cmd = lambda x=button: self.add_to_display(x)
                btn = ttk.Button(root, text=button, command=cmd, style='Calculator.TButton')
                btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
            
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def add_to_display(self, char):
        if char == 'C':
            self.expression_var.set('')
            self.result_var.set('')
        else:
            current = self.expression_var.get()
            self.expression_var.set(current + char)

    def calculate(self):
        try:
            expression = self.expression_var.get()
            postfix = self.calc.infix_to_postfix(expression)
            result = self.calc.evaluate_postfix(postfix)
            self.result_var.set(str(result))
        except Exception as e:
            self.result_var.set("Error")

def main():
    root = tk.Tk()
    root.geometry("400x600")
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()