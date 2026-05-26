"""Simple Python calculator with CLI and safe expression parsing."""

import ast
import operator
import sys
from typing import Any, Union

Number = Union[int, float]

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

HELP_TEXT = """
Simple Calculator

Usage:
  - Enter arithmetic expressions like: 2 + 3 * (4 - 1)
  - Supported operators: +, -, *, /, //, %, **
  - Commands: help, history, exit, quit
  - Press Enter on an empty line to continue.
"""


def eval_expr(expression: str) -> Number:
    """Evaluate a numeric expression safely."""
    if not expression or not expression.strip():
        raise ValueError("Expression is empty")

    node = ast.parse(expression, mode="eval").body
    return _evaluate_node(node)


def _evaluate_node(node: ast.AST) -> Number:
    if isinstance(node, ast.BinOp):
        operator_type = type(node.op)
        if operator_type not in OPERATORS:
            raise ValueError(f"Unsupported operator: {operator_type.__name__}")
        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)
        return OPERATORS[operator_type](left, right)

    if isinstance(node, ast.UnaryOp):
        operator_type = type(node.op)
        if operator_type not in UNARY_OPERATORS:
            raise ValueError(f"Unsupported unary operator: {operator_type.__name__}")
        operand = _evaluate_node(node.operand)
        return UNARY_OPERATORS[operator_type](operand)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numeric literals are allowed")

    if isinstance(node, ast.Expr):
        return _evaluate_node(node.value)

    raise ValueError(f"Unsupported expression: {type(node).__name__}")


def format_result(value: Number) -> str:
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def main() -> int:
    history: list[str] = []

    if len(sys.argv) > 1:
        expression = " ".join(sys.argv[1:])
        try:
            result = eval_expr(expression)
            print(format_result(result))
            return 0
        except Exception as exc:
            print(f"Error: {exc}")
            return 1

    print("Calculator ready. Type 'help' for usage, 'exit' to quit.")

    while True:
        try:
            line = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0

        if not line:
            continue

        command = line.lower().strip()
        if command in {"exit", "quit", "q"}:
            return 0
        if command == "help":
            print(HELP_TEXT)
            continue
        if command == "history":
            if not history:
                print("No history yet.")
                continue
            for index, entry in enumerate(history, start=1):
                print(f"{index}: {entry}")
            continue

        try:
            result = eval_expr(line)
            history.append(line)
            print(format_result(result))
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    raise SystemExit(main())
