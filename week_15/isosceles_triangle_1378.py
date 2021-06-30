from math import sqrt


def distance(p1, p2):
    distance = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
    return sqrt(distance)


def calc_triangle(p1, p2, p3):

    answer = False

    d_p1_p2 = distance(p1, p2)
    d_p1_p3 = distance(p1, p3)
    d_p2_p3 = distance(p2, p3)

    if d_p1_p2 == d_p1_p3 and d_p2_p3 != d_p1_p2:
        answer = True

    elif d_p1_p2 == d_p2_p3 and d_p1_p2 != d_p1_p3:
        answer = True

    elif d_p1_p3 == d_p2_p3 and d_p1_p3 != d_p1_p2:
        answer = True

    return answer


def isosceles_triangle():
    while True:
        n_coords = int(input())

        if n_coords == 0:
            break

        coords = list()
        for _ in range(n_coords):
            coords.append(tuple(map(int, input().split())))

        n_sets = 0
        for i in range(n_coords-2):
            for j in range(i+1, n_coords-1):
                for k in range(j+1, n_coords):
                    if calc_triangle(coords[i], coords[j], coords[k]):
                        n_sets += 1

        print(n_sets)


if __name__ == '__main__':
    isosceles_triangle()
