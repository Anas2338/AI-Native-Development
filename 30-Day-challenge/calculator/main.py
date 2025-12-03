import sys
from src.calculator.cli import CLI

def main():
    cli = CLI()
    sys.exit(cli.run())

if __name__ == "__main__":
    main()
