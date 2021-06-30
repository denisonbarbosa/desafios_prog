from math import sqrt

cherries_coords = list()


def calc_diff(p1, p2):
    global lowest_diference, cherries_coords

    if p2[0] < p1[0]:
        p2, p1 = p1, p2

    x2_x1 = p2[0] - p1[0]
    y2_y1 = p2[1] - p1[1]

    bottom = (x2_x1**2) + (y2_y1**2)
    bottom = sqrt(bottom)

    right_sum = left_sum = 0
    for cherry in cherries_coords:
        if cherry == p1 or cherry == p2:
            continue

        top = (x2_x1*(p1[1]-cherry[1])) - ((p1[0]-cherry[0])*y2_y1)

        distance = abs(top)/bottom

        if top <= 0:
            right_sum += distance
        else:
            left_sum += distance

    if abs(left_sum - right_sum) < lowest_diference:
        lowest_diference = abs(left_sum - right_sum)


def bobby_fantastic_cake():
    while True:

        n_cherries = int(input())

        if n_cherries == 0:
            break

        for _ in range(n_cherries):
            cherries_coords.append(tuple(map(int, input().split())))

        global lowest_diference
        lowest_diference = 10000000

        for i in range(n_cherries-1):
            for j in range(i+1, n_cherries):
                calc_diff(cherries_coords[i], cherries_coords[j])

        print(f'{lowest_diference:.3f}')


if __name__ == '__main__':
    bobby_fantastic_cake()
