n = int(input("Digite o número: "))
number = 2**n

lista = []

def soma_multiplos_dois(n: float) -> float:

    lista.append(1/n)
    
    if n % 2 != 0:
        
        print(lista)

    else:
        n = n/2
        soma_multiplos_dois(n)
        soma = sum(lista)
        return soma

somatorio = soma_multiplos_dois(number)

print(f"Somatorio: {somatorio}")