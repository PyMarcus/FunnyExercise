
def decresce(lista):
    lista3 = []
    tamanho = len(lista)
    contador = 0
    i= 0
    j = 0

    for valores in lista:
        if contador == 0:
            maior = valores
            menor = valores
        else:
            if valores > maior:
                maior = valores
            if valores < menor:
                menor = valores
        contador = 1

    while i <= len(lista) + 1:
        while j < len(lista):
            if lista[j] < menor:
                menor = lista[j]
            if lista[j] >= maior: 
                maior = lista[j]
            j += 1
        if maior not in lista3:
            lista3.append(maior)
        if j >= len(lista) and len(lista3) <= tamanho:
            j = 0
        if maior in lista:
            valor = lista.index(maior)
            del lista[valor]
        maior = menor
        i += 1
    lista3.append(menor)
    return lista3


if __name__ == '__main__':
    lista = [1, 43232, -321321, 4.4, 12312, 4, 6, -2]
    print(decresce(lista))
