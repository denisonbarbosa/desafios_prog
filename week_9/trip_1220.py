def trip():
    while True:
        n_friends = int(input())
        if n_friends == 0:
            break

        payments = list()
        sum = 0
        for _ in range(n_friends):
            int_part, dec_part = map(int, list(input().split('.')))
            payment = (int_part * 100) + dec_part
            sum = sum + payment
            payments.append(payment)

        average = sum/n_friends

        change_higher = change_lower = 0

        for payment in payments:
            if payment > average:
                change_higher += int(payment - average)/100.0
            else:
                change_lower += int(average - payment)/100.0

        answer = f'${change_higher:0.2f}'
        if change_lower > change_higher:
            answer = f'${change_lower:0.2f}'

        print(answer)


if __name__ == '__main__':
    trip()
