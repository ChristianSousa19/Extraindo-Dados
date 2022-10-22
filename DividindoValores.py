lista=list()
par=list()
impar=list()
while True:
 lista.append(int(input("Digite um  numero inteiro: ")))
 w=str(input("VOcê deseja continuar [S/N] ?  ")).strip().upper()[0]
 if w in "Nn":
     break
for i,v in enumerate(lista):
    if v%2==0:
        par.append(v)
    else:
        impar.append(v)
print(f"A lista completa é {lista}")
print(f"As listas de pares é {par} ")
print(f"As listas de ímpares é {impar}")
