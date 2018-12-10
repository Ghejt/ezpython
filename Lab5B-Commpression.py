def compress(word):
    x = 0
    while x < len(word):
        number = str(word.count(word[x]))
        if x == len(word) - 1:
            print("")
        elif word[x] != word[x + 1]:
            print(word[x] + number, end="")
        x += 1
