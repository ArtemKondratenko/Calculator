from collections.abc import Iterator
from typing import Literal

ArithmeticOperator = Literal["+", "-", "*", "/"]
Parenthesis = Literal["(", ")"]
Number = int | float
Token = Number | ArithmeticOperator | Parenthesis


def tokenize(expression: str) -> Iterator[Token]:
    return Tokenizer(expression)


class Tokenizer:
    expression: str
    position: int

    def __init__(self, expression: str):
        self.expression = expression
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self) -> Token:
        self.skip_spaces()

        if not self.peek():
            raise StopIteration

        token = self.read_number() or self.read_arithmetic_operator() or self.read_parenthesis()
        if not token:
            raise ValueError("Error!")

        return token

    def peek(self) -> str:
        if self.position >= len(self.expression):
            return ""
        return self.expression[self.position]

    def advance(self):
        self.position += 1

    def skip_spaces(self):
        while self.peek().isspace():
            self.advance()

    def read_number(self) -> Number | None:
        number = ""
        while c := self.peek():
            if c.isdigit() or (c == "." and "." not in number and number != ""):
                number += c
                self.advance()

        if not number:
            return None

        if "." in number:
            return float(number)

        return int(number)

    def read_arithmetic_operator(self) -> ArithmeticOperator | None:
        match c := self.peek():
            case "+" | "-" | "*" | "/":
                self.advance()
                return c
            case _:
                return None

    def read_parenthesis(self) -> Parenthesis | None:
        match c := self.peek():
            case "(" | ")":
                self.advance()
                return c
            case _:
                return None
