def main():

    a, b = map(int, input().split())

    while (a != 0 and b != 0):

    setA = set(list(map(int, input().split())))
    setB = set(list(map(int, input().split())))
    tradeable_A = setA - setB
    tradeable_B = setB - setA

    print(min(len(tradeable_A), len(tradeable_B)))

    a, b = map(int, input().split())


if __name__ == "__main__":
    main()
