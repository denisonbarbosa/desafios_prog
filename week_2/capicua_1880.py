def main():

    instances = int(input())
    while instances > 0:

        n = input()
        answer_string = ''
        for base in range(2, 17):
            if is_capicua(int(n), base):
                if answer_string != '':
                    answer_string += " "
                answer_string = answer_string + str(base)

        if answer_string == '':
            answer_string = '-1'
        print(answer_string)

        instances -= 1


def is_capicua(n, base):
    converted = ''

    while(n > 0):
        if n % base < 10:
            converted += str(n % base)
        else: 
            letters = 'ABCDEF'
            converted += letters[(n % base) - 10]

        n = int(n / base)

    end = len(converted) - 1
    capicua = True
    for i in range(int(len(converted)/2)):
        if converted[i] != converted[end]:
            capicua = False
            break
        end -= 1

    return capicua


if __name__ == "__main__":
    main()
