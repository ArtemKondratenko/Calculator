from calculator.calculating_expression import ArithmeticOperationNode, NumberNode


tree = ArithmeticOperationNode(
  operation="*",
  left=NumberNode(3),
  right=ArithmeticOperationNode(
    operation="-",
    left=NumberNode(7),
    right=NumberNode(2)
  )
)

result = tree.calculate()
print(result)
