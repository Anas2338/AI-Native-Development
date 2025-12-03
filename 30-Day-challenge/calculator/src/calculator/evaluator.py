class Evaluator:
    def evaluate(self, tokens: list) -> float:
        if not isinstance(tokens, list) or not all(isinstance(t, str) for t in tokens):
            raise ValueError("Input must be a list of strings (tokens)")

        # Using a simple stack-based approach for evaluation
        # This assumes a pre-parsed expression (e.g., from the parser)
        # For simplicity, this evaluator processes a flat list of tokens in order
        # A more robust solution would involve converting to RPN or building an AST

        if not tokens:
            raise ValueError("Empty token list for evaluation")

        # Initial pass to handle multiplication and division
        temp_tokens = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '*':
                operand1 = float(temp_tokens.pop())
                operand2 = float(tokens[i+1])
                temp_tokens.append(str(operand1 * operand2))
                i += 2
            elif token == '/':
                operand1 = float(temp_tokens.pop())
                operand2 = float(tokens[i+1])
                if operand2 == 0:
                    raise ValueError("Division by zero")
                temp_tokens.append(str(operand1 / operand2))
                i += 2
            else:
                temp_tokens.append(token)
                i += 1

        tokens = temp_tokens

        # Second pass to handle addition and subtraction
        if not tokens:
            raise ValueError("Empty token list after multiplication/division")

        result = float(tokens[0])
        i = 1
        while i < len(tokens):
            operator = tokens[i]
            operand = float(tokens[i+1])
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            else:
                raise ValueError(f"Invalid operator: {operator}")
            i += 2

        return result
