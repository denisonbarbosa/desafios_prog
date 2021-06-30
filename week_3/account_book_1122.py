def account_book():

    n_transactions, balance = list(map(int, input().split()))

    while n_transactions != balance != 0:
        transaction_values = []
        for i in range(n_transactions):
            transaction_values.append([int(input()), i])

        print(transaction_values)

        n_transactions, balance = list(map(int, input().split()))


if __name__ == '__main__':
    account_book()
