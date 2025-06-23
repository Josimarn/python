import datetime

data_atual = datetime.datetime.now()
nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))

if idade <= 11:
    print(f"Olá, {nome}!!!, a faixa etária para a sua idade de {idade} anos é de uma criança")
elif idade <= 17:
    print(f"Olá, {nome}!!!, a faixa etária para a sua idade de {idade} anos é de um(a) adolescente")
elif idade <= 24:
    print(f"Olá, {nome}!!!, a faixa etária para a sua idade de {idade} anos é de um(a) jovem")
elif idade <= 29:
    print(f"Olá, {nome}!!!, a faixa etária para a sua idade de {idade} anos é de um(a) jovem adulto(a)")
elif idade <= 59:
    print(f"Olá, {nome}!!!, a faixa etária para a sua idade de {idade} anos é de um(a) adulto(a)")
else:
    print(f"Olá, {nome}!!!, a faixa etária para a sua idade de {idade} anos é de um(a) idoso(a))")

print(data_atual)