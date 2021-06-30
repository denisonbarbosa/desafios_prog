def where_is_my_pen():

    # [i] = 1 se a caneta i+1 foi devolvida, 0 c.c.
    case = [0] * 100000

    while True:

        try:
            # Le o número de canetas
            n = int(input())

        # Quando input() == EOF, sai do loop principal
        except:
            break

        # Recebe a entrada e divide em uma lista
        pens = input().split()

        # Calcula as canetas devolvidas
        for pen in pens:
            case[int(pen)-1] = 1

        # Procura a caneta que está faltando e imprime o resultado.
        # Se a caneta estiver no estojo, redefine para 0 pensando na próxima iteração
        for i in range(n):
            if case[i] == 0:
                print(i+1)
            case[i] = 0


if __name__ == "__main__":
    where_is_my_pen()
