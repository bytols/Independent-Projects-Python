def func1():
    print("Selecione os 2 números da multiplicação")
    num1 = int(input("Escolha o número 1:"))
    num2 = int(input("Escolha o número 2:"))
    soma = num1 * num2
    print(f"a soma de {num1} e {num2} resulta em:")

    return func1

def func2():
    print("escolha os 2 númeors á serem dividdos:")
    num1 = int(input("Escolha o número 1:"))
    num2 = int(input("Escolha o número 2:"))
    soma = num1 / num2
    print(f"a divisão entre {num1} e enntre {num2} é equivalente á:")

    return func2

def func3():
    print("escolha os números a serem subtraidos:")
    num1 = int(input("Escolha o Número 1:"))
    num2 = int(input("Escolha o Número 2:"))
    num3 = int(input("Escolha o Número 3:"))
    num4 = int(input("Escolha o Número 4:"))
    subtracao = num1 - num2 - num3 - num4;
    print(f"a subtração entre {num1} , {num2} , {num3} e {num4}")

    return func3

func2()

