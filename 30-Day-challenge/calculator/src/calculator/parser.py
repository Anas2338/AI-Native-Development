import re

class Parser:
    def parse(self, expression: str) -> list:
        if not isinstance(expression, str):
            raise ValueError("Input must be a string")

        # Use a regex to find numbers and operators, handling potential whitespace
        # Use a regex to find numbers and operators, handling potential whitespace
        cleaned_expression = expression.replace(' ', '')
        tokens = re.findall(r'\d+\.?\d*|[-+*/()]', cleaned_expression)

        if not tokens:
            raise ValueError("Invalid or empty expression")

        # Verify that all characters in the cleaned expression were tokenized
        reconstructed_expression = "".join(tokens)
        if reconstructed_expression != cleaned_expression:
            raise ValueError("Invalid characters or malformed expression")

        # Strict validation to ensure all tokens are either valid numbers or operators
        for token in tokens:
            if not (re.fullmatch(r'\d+\.?\d*', token) or re.fullmatch(r'[-+*/]', token)):
                # This specific check might be redundant if the regex for findall is strict
                # but keeping it for an extra layer of safety against unexpected token types.
                raise ValueError(f"Invalid token in expression: {token}")

        return tokens
