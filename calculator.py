#!/usr/bin/env python3
"""Simple command-line calculator."""
import operator
import argparse

OPERATIONS = {
    "add": operator.add,
    "sub": operator.sub,
    "mul": operator.mul,
    "div": operator.truediv,
}

def main() -> None:
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("operation", choices=OPERATIONS.keys(), help="Operation to perform")
    parser.add_argument("x", type=float, help="First operand")
    parser.add_argument("y", type=float, help="Second operand")
    args = parser.parse_args()
    func = OPERATIONS[args.operation]
    result = func(args.x, args.y)
    print(result)

if __name__ == "__main__":
    main()
