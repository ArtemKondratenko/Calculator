from calculator.tokenize import Token, ArithmeticOperator, Number
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Node(ABC):
  @abstractmethod
  def calculate(self) -> Number:
    pass


@dataclass
class ArithmeticOperationNode(Node):
  operation: ArithmeticOperator
  left: Node
  right: Node

  def calculate(self) -> Number:
    if self.operation == "+":
      return self.left.calculate() + self.right.calculate()
    elif self.operation == "-":
      return self.left.calculate() - self.right.calculate()
    elif self.operation == "*":
      return self.left.calculate() * self.right.calculate()
    else:
      return self.left.calculate() / self.right.calculate()


@dataclass
class NumberNode(Node):
  value: Number

  def calculate(self) -> Number:
    return self.value



