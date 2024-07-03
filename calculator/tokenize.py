from collections.abc import Iterator
from typing import Literal

ArithmeticOperator = Literal["+", "-", "*", "/"]
Parenthesis = Literal["(", ")"]
Number = int | float
Token = Number | ArithmeticOperator | Parenthesis


def remove_spaces(s: str) -> str:
    return ''.join(s.split())


def tokenize(s: str) -> Iterator[Token]:
    s = remove_spaces(s)
    tokenizer = Tokenizer(s)
    while tokenizer.has_next():
        yield tokenizer.next()


class Tokenizer:
    s: str
    position: int

    def has_next(self) -> bool:
        return self.position < len(self.s)

    def next(self) -> Token:
        if self.position >= len(self.s):
            raise StopIteration()

        char = self.s[self.position]

        if char.isdigit():
            number = self.read_number()
            if number is not None:
                return number
            else:
                raise ValueError(f"Invalid number: {char}")

        operator = self.read_operator()
        if operator is not None:
            return operator

        parenthesis = self.read_parenthesis()
        if parenthesis is not None:
            return parenthesis

        raise ValueError(f"Invalid token: {char}")

    def __init__(self, s: str):
        self.s = s
        self.position = 0

    @staticmethod
    def check_elements(string: str):
        return all(char not in "><!&#@^$¢" for char in string)

    def read_number(self) -> Number | None:
        number = ""
        dot_count = 0
        for char in self.s[self.position:]:
            if char.isdigit():
                number += char
            elif char == "." and dot_count == 0:
                number += char
                dot_count += 1
            else:
                break
        if number == "" or number == "." or number[0] == "." or not self.check_elements(number):
            return None
        self.position += len(number)
        if dot_count == 1:
            return float(number)
        else:
            return int(number)

    def read_operator(self) -> ArithmeticOperator | None:
        for operator in "+-*/":
            if self.s[self.position:].startswith(operator):
                self.position += len(operator)
                return operator  # type: ignore
        return None

    def read_parenthesis(self) -> Parenthesis | None:
        if self.s[self.position:].startswith("("):
            self.position += 1
            return "("
        elif self.s[self.position:].startswith(")"):
            self.position += 1
            return ")"
        else:
            return None