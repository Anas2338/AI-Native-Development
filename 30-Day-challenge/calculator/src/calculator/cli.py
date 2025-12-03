import argparse
import sys
from src.calculator.parser import Parser
from src.calculator.evaluator import Evaluator

class CLI:
    def __init__(self):
        self.parser = Parser()
        self.evaluator = Evaluator()
        self.arg_parser = self._setup_arg_parser()

    def _setup_arg_parser(self):
        parser = argparse.ArgumentParser(description="Simple Calculator CLI")
        parser.add_argument("expression", type=str, help="Arithmetic expression to evaluate (e.g., \"5+3\")")
        return parser

    def run(self, args=None):
        parsed_args = self.arg_parser.parse_args(args)
        expression = parsed_args.expression

        try:
            tokens = self.parser.parse(expression)
            result = self.evaluator.evaluate(tokens)
            print(result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr) # Use sys.stderr for error messages
            return 1 # Indicate an error
        except Exception as e:
            print(f"An unexpected error occurred: {e}", file=sys.stderr)
            return 1
        return 0 # Indicate success

# Note: sys module is needed for stderr, will add import to main.py or top of this file later
