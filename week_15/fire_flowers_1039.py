from math import sqrt


def calc_norm(x1, y1, x2, y2):
    x_ = x2 - x1
    y_ = y2 - y1

    return sqrt((x_ ** 2) + (y_ ** 2))


def fire_flowers():

    while True:
        try:
            r1, x1, y1, r2, x2, y2 = list(map(int, input().split()))
        except EOFError:
            break

        norm = calc_norm(x1, y1, x2, y2)

        if norm > r1 or (norm+r2) > r1:
            print('MORTO')
        else:
            print('RICO')


if __name__ == '__main__':
    fire_flowers()
