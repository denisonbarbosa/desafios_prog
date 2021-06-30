def square_lotery():
    while True:
        n, percentage = list(input().split())
        n = int(n)
        percentage = float(percentage)
        if n == int(percentage) == 0:
            break
        
        square = n*n
        fatorials = square * (square - 1) * (square - 2) * (square - 3)
        
        award_money = fatorials / (check_square_shapes(n) * 24)
        
        answer = award_money * (percentage/100)
        
        print(f'{answer:.2f}')


# Checks the number of possible square shapes inside a n x n ticket
def check_square_shapes(n):
    return ((n-1) * n * (n+1) * n) / 12


if __name__ == '__main__':
    square_lotery()