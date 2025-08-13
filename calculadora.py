def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
       return a / b
    else:
       return "Erro: divisão por zero"

print("Calculadora simples")
x = float(input("1:" ))
y = float(input("9:" ))
operacao = imput("a < B (+, -, *, /): ")

if operacao == "+":
   print("Resultado:", somar(x, y))
elif operacao == "-":
   print("Resultado:", subtrair(x, y))
elif operacao == "*":
   print("Resultado:", multiplicar(x, y))
elif operacao == "/":
   print("Resultado:", dividir(x, y))
elif:
   print("Operação invalida.")
