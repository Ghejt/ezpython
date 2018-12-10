def print_word(word):
    charindex= len(word) - 1
    i = 0
    while i <= charindex:
        print(word[i], end=" ")
        i += 1

def print_stars(n):
    stars = int(n)
    while stars > 0:
        print("*", end=" ")
        stars -= 1
    
def main():
    word = input("WORD> ")
    n = 1
    while n <= len(word):
        num_spaces = len(word) - n
        while num_spaces > 0:
            print(" ", end="")
            num_spaces -= 1
        print_stars(n)
        print("\n")
        n += 1
        
    print_word(word)
