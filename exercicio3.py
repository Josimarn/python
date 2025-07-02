"""
2. Faça um programa que peça três valores e apresente a soma dos quadrados dos valores lidos.
"""

numero1: int = int(input("Informe o primeiro número: "))
numero2: int = int(input("Informe o segundo número: "))
numero3: int = int(input("Informe o terceiro número: "))


soma: int = (numero1 * numero1) + (numero2 * numero2) + (numero3 * numero3)

print(f"A soma dos quadrados dos números {numero1}, {numero2}, e {numero3} é {soma}")
