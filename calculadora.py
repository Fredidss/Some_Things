num1 = float(input("Ingresa el primer número: "))
operador = input("Ingresa el operador (+, -, *, /): ")
num2 = float(input("Ingresa el segundo número: "))

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
else:
    print("Operador inválido")
    exit()

print("El resultado es:", resultado)