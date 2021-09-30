points = 0
contador = 0
valor = 3
respostas = ["d", "b", "a", "a", "d", "c", "b", "d", "a", "a", "d", "c", "b", "b", "c", "b", "d", "d", "d", "b", "d", "a", "b", "a", "b", "d", "a", "c", "a", "c"]

while contador < (len(respostas)):
    valor = 3
    while True:
        res = input("Qual a resposta da pergunta {}: (Tentativa(s) restante: {}):".format(contador + 1, valor))
        if (res == respostas[contador]):
            contador += 1
            points += valor
            print("Você acertou! Proxima...")
            break
        else:
            valor -= 1
            if valor == 0:
                print("Você errou todas as tentativas desta pergunta.")
                contador += 1
                break

print("Sua pontuação foi {}".format(points))


    

