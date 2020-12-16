import random


numAl = random.randint(0,100)
tentativas=0

while tentativas<6:

    tentativas+=1
    print(f"\n--------tentativa n {tentativas}--------\n")
    NumEsc=int(input("Digite um numero\n"))
    
    if NumEsc!=numAl:
        if NumEsc>numAl:
            print("O seu numero escolhido foi maior do que o numero definido")
        else:
            print("O seu numero escolhido foi menor do que o numero definido")
    else:
        print("Parabéns, você venceu com %i tentativas"%tentativas)
        exit()

print("Tentativas excedidas!")