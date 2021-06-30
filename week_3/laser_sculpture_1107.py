def laser_sculpture():
    
    lines, cols = list(map(int, input().split()))
    
    while True:
        if lines == cols == 0:
            break

        heights = list(map(int, input().split()))

        total = 0
        last_height = lines
        for i in heights:
            if (i < last_height):
                total += last_height - i
            last_height = i

        print(total)

        lines, cols = list(map(int, input().split()))


if __name__ == '__main__':
    laser_sculpture()
