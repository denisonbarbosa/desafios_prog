def main():

    qtd_banks, qtd_debentures = map(int, input().split())

    while (qtd_banks != 0 and qtd_debentures != 0):
        bank_reserves = list(map(int, input().split()))

        for i in range(qtd_debentures):
            transaction = list(map(int, input().split()))

            bank_reserves[transaction[1]-1] += transaction[2]
            bank_reserves[transaction[0]-1] -= transaction[2]

        liquidated = True
        for reserve in bank_reserves:
            if reserve < 0:
                liquidated = False

        answer = 'N'
        if liquidated:
            answer = 'S'

        print(answer)

        qtd_banks, qtd_debentures = map(int, input().split())


if __name__ == "__main__":
    main()
