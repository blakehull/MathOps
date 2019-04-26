from calculus import operators

style = operators.Differential()

f = style.Function("3x^32 + 5280x^23 + 91x")

print(style.derivative(14, f))

