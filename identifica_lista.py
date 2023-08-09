def confere_lista(lista_numerica):

    crescente = True
    decrescente = True

    for i in range(1,len(lista_numerica)):
        if lista_numerica[i] > lista_numerica[i-1]:
            decrescente = False
        elif lista_numerica[i] < lista_numerica[i-1]:
            crescente = False

    if crescente:
        return "crescente"
    elif decrescente:
        return "decrescente"
    else:
        return "não ordenada"



numeros = input("Digite os números da lista separados por um espaço: ")
lista = [int(num) for num in numeros.split()]

ordem = confere_lista(lista)
print(f"Essa é uma lista {ordem}.")