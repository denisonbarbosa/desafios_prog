import numpy


def famous_minefield():

    lines, cols, n_mines = map(int, input().split())
    while(True):
        if lines == cols == n_mines == 0:
            break

        field = []
        field.append(list(map(str, numpy.zeros(cols+2, numpy.int8))))
        for i in range(lines):
            line = '0' + input() + '0'
            field.append(list(line))
        field.append(list(map(str, numpy.zeros(cols+2, numpy.int8))))

        # print(field)

        mines_loc = []
        for i in range(n_mines):
            mines_loc.append(input().split())

        for l in range(lines):
            for c in range(cols):


        lines, cols, n_mines = map(int, input().split())


def update_neighbours(x, y, field):
    x += 1
    y += 1

    



if __name__ == '__main__':
    famous_minefield()
