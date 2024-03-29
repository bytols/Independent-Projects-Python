
import random


numeromagico = int(random.randint(0,9))
numero = int(input("escolha um numero"))
print(numero)
print(numeromagico)

if numero == numeromagico:
    print("parabens mágico, você acertou!")
if numero < numeromagico:
    print("diminua o chute")
if numero > numeromagico:
    print("aumente o valor do chute")
else:
    print("")