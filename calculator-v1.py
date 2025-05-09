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

def main():
    calc = PostfixCalculator()
    while True:
        try:
            expression = input("\nEnter infix expression (or 'q' to quit): ")
            if expression.lower() == 'q':
                break
                
            postfix = calc.infix_to_postfix(expression)
            result = calc.evaluate_postfix(postfix)
            
            print(f"Postfix: {postfix}")
            print(f"Result: {result}")
            
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
