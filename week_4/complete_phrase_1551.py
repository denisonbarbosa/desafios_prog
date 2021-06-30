def complete_phrase():
    
    instances = int(input())

    while instances > 0:
        phrase = list(map(str, input()))

        letters = []
        for letter in phrase:
            if letter not in letters and letter.isalpha():
                letters.append(letter)

        answer = 'frase completa'
        if len(letters) < 13:
            answer = 'frase mal elaborada' 
        elif len(letters) >= 13 and len(letters) < 26:
            answer = 'frase quase completa'

        print(answer)

        instances -= 1

if __name__ == '__main__':
    complete_phrase()