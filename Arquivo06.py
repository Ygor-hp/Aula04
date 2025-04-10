soma=0
fora=0
for x in range(10):
    numero=int(input("Digite 10 valores:"))
    if numero>=10 and numero<=20:
        soma=soma+1
    else:
        fora=fora+1
print(f"Estes numeros estão entre 10 e 20:{soma}.")
print(f"os que estão fora {fora}")