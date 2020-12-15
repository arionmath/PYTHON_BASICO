print("Seja bem vindo ao meu programa de calculo imc.")
nome=input('Por favor, digite seu nome\n')

try:
    peso = float(input('Agora digite sua peso usando o ponto como separador decimal\n'))
    altura = float(input('Agora digite sua altura usando o ponto como separador decimal\n'))
except:
    print("Aconteceu algum erro enquanto voce digitava os valores numéricos")
    exit()


imc = peso/(altura*altura)
print(f"{nome}, seu imc será %.3f" %imc)

