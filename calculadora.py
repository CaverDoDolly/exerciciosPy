def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Erro: Divisão por zero não é permitida.")
        return None
    return a / b

print("=" * 20)
print("CALCULADORA")
print("=" * 20)

print("Operaçoes disponíveis:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("0 - Sair")
print(" ")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação desejada: ")

if op == 0:
    print("Saindo da calculadora...")
    exit()

match op:
    case "1":
        resultado = somar(n1, n2)
        print(f"O resultado da soma é: {resultado:.2f}")
    case "2":
        resultado = subtrair(n1, n2)
        print(f"O resultado da subtração é: {resultado:.2f}")
    case "3":
        resultado = multiplicar(n1, n2)
        print(f"O resultado da multiplicação é: {resultado:.2f}")
    case "4":
        if n2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            resultado = dividir(n1, n2)
            print(f"O resultado da divisão é: {resultado:.2f}")
    case _:
        print("Operação inválida. Por favor, escolha uma operação válida.")