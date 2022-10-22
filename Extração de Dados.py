lista=[]
elementos=0
while True:
 lista.append(int(input("Digite um  numero inteiro: ")))
 elementos+=1
 w=str(input("VOcê deseja continuar [S/N] ?  ")).strip().upper()[0]
 if w in "Nn":
     break
print(f"Você digitou {len(lista)} elementos")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {lista}")
lista.count(5)
if 5 in lista:
    print("O valor 5 faz parte da listta")
else:
    print(" O valor 5 não faz parte da lista  ")

