num=list()
valor=0
w=" "
while True:
    valor=int(input("Digite um valor: "))
    if valor not in num:
     num.append(valor)
     print("Valor adcionado com sucesso:")
    else:
        print("Valor duplicado!!!!,Não adcionarei esse numero")
    w=str=input("Deseja continuar? [S/N]").strip().upper()[0]
    if w in"Nn":
      break
num.sort(reverse=True)
print(f"Você digitou os numeros: {num}")