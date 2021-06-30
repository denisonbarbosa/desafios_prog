from decimal import Decimal, ROUND_DOWN


def trip():
    case = 0

    while True:
        n_friends = int(input())
        if n_friends == 0:
            break

        case += 1  # DEBUG
        print(f'\n{case}')  # DEBUG

        payments = list()
        sum = Decimal(0)
        for _ in range(0, n_friends):
            payment = Decimal(input())
            # print(f'payment: {payment}') # DEBUG

            sum = sum + payment
            payments.append(payment)

        average = (sum/Decimal(str(n_friends)))

        average = average.quantize(Decimal('1.0000'))
        print(f'average 1.0000: {average}')  # DEBUG

        average = average.quantize(Decimal('1.00'))
        print(f'average 1.00: {average}')  # DEBUG

        change_higher = change_lower = Decimal('0')

        for payment in payments:
            if payment > average:
                change_higher += (payment - average)
                # print(f'partial change higher: {change_higher} incremented in payment: {payment}') # DEBUG
            elif payment < average:
                change_lower += (average - payment)
                # print(f'partial change lower: {change_lower} incremented in payment: {payment}') # DEBUG

        answer = f'${change_lower.quantize(Decimal("1.00"))}'
        # print('answer lower: '+ answer) # DEBUG

        if change_lower > change_higher:
            answer = f'${change_higher.quantize(Decimal("1.00"))}'

        # print('answer higher: '+ answer) # DEBUG
        print(answer)


if __name__ == '__main__':
    trip()
