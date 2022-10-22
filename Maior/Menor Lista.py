valor=[]
maior=0
menor=0
for cont in range(0,5):
    valor.append(int(input(f"Digite um valor para a {cont} posição: ")))
    if cont==0:
         maior=menor=valor[cont]
    else:
        if valor[cont]>maior:
            maior=valor[cont]
        if valor[cont]<menor:
            menor=valor[cont]
print(f"Você digitou os numeros {valor}")
print(f"O maior valor da lista é: {maior}")
for i,v in enumerate(valor):
    if v==maior:
        print(f"Nas poisções {i}")
print(f"O menor valor da lista é: {menor}")
for l,m in enumerate(valor):
    if m==menor:
        print(f"Nas posições {l}")