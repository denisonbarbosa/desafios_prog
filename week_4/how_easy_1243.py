def how_easy():
    while True:
        words = input().split()
        if not words:
            break
        
        total_length = 0
        valid_words_count = 0

        for word in words:
            valid = True
            for index, char in enumerate(word):
                if not char.isalpha():
                    if char == '.' and index == len(word) - 1:
                        break
                    valid = False
            if valid:
                word_length = len(word)
                if word[len(word)-1] == '.':
                    word_length -= 1
                total_length += word_length
                valid_words_count += 1

        average = 0
        if valid_words_count > 0:
            average = total_length / valid_words_count

        difficulty = 1000
        if average <= 3:
            difficulty = 250
        elif average < 6:
            difficulty = 500

        print(difficulty)


if __name__ == '__main__':
    how_easy()
