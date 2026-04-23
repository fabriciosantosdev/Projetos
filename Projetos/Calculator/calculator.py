from decimal import Decimal

n1 = Decimal(input("Primeiro número: "))
op = input("Operação (+, -, *, /, **): ")
n2 = Decimal(input("Segundo número: "))

if op == "+":
    print("Resultado:", n1 + n2)
elif op == "-":
    print("Resultado:", n1 - n2)
elif op == "*":
    print("Resultado:", n1 * n2)
elif op == "/":
    print("Resultado:", n1 / n2)
elif op == "**":
    print("Resultado:", n1 ** n2)
else:
    print("Operação inválida")