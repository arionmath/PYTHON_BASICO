lista=[]

while(True):
    print("Digite seu comando (insert a b,print,remove a,append a,sort ,pop ,reverse )")
    comando=input()

    if comando[0:3] == 'ins':
        print("comando de inserção")
        parteDocomando=comando.split(' ')
        numero=int(parteDocomando[2])
        lista.insert(int(parteDocomando[2]),parteDocomando[1])


    elif comando[0:3] == 'pri':
        print("comando de impressao")
        print(lista)

    elif comando[0:3] == 'rem':
        print("comando de remoção")
        parteDocomando = comando.split(' ')
        lista.remove(parteDocomando[1])

    elif comando[0:3] == 'app':
        print("comando de inserção no fim")
        parteDocomando = comando.split(' ')
        lista.append(parteDocomando[1])

    elif comando[0:3] == 'sor':
        print("comando de ordenação")
        lista.sort()

    elif comando[0:3] == 'pop':
        print("comando de pop")
        print(lista.pop())

    elif comando[0:3] == 'rev':
        print("comando de reversão")
        lista.reverse()

    else:
        print("invalido")
