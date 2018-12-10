import random
def make_deck():
    deck = ['D3', 'HK', 'C7', 'C3', 'DK', 'H8', 'H6', 'DJ', 'H2', 'CJ', 'D8', 'HA', 'H5', 'DX', 'S8', 'S2', 'CK', 'D4', 'D9', 'C6', 'CA', 'HQ', 'C4', 'S5', 'S3', 'HJ', 'S9', 'D2', 'CQ', 'SJ', 'H4', 'C5', 'HX', 'C9', 'H7', 'C2', 'S6', 'H9', 'C8', 'SA', 'DQ', 'SX', 'D5', 'S7', 'SK', 'D6', 'D7', 'S4', 'H3', 'DA', 'CX', 'SQ']
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    i = 0
    count = 1
    for i in range(0, len(deck), 4):
        if count == 1:
            pile1 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 2:
            pile2 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 3:
            pile3 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 4:
            pile4 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 5:
            pile5 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 6:
            pile6 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 7:
            pile7 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 8:
            pile8 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 9:
            pile9 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 10:
            pile10 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 11:
            pile11 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 12:
            pile12 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
        elif count == 13:
            pile13 = [deck[i], deck[i+1], deck[i+2], deck[i+3]]
            count += 1
            i += 4
    piles = [pile1, pile2, pile3, pile4, pile5, pile6, pile7, pile8, pile9, pile10, pile11, pile12, pile13]
    return piles

def show_cards(piles, row):
    print("    A  2  3  4  5  6  7  8  9  X  J  Q  K")
    height = 4
    while height > 0:
        print(height, ":", end="")
        for card in range(0, 13):
            if row == card and height == len(piles[row]):
                print(piles[row][height-1], end=" ")
            elif height <= len(piles[card]):
                print("**", end=" ")
            else:
                print("  ", end=" ")
        print()
        height -= 1
    return piles[row].pop()
        
    
def main():
    piles = deal_cards(make_deck())
    king = 0
    row = 12
    while king < 4:
        game = show_cards(piles, row)
        if game[1] == "K":
            row = 12
            king += 1
        elif game[1] == "Q":
            row = 11
        elif game[1] == "J":
            row = 10
        elif game[1] == "X":
            row = 9
        elif game[1] == "9":
            row = 8
        elif game[1] == "8":
            row = 7
        elif game[1] == "7":
            row = 6
        elif game[1] == "6":
            row = 5
        elif game[1] == "5":
            row = 4
        elif game[1] == "4":
            row = 3
        elif game[1] == "3":
            row = 2
        elif game[1] == "2":
            row = 1
        elif game[1] == "A":
            row = 0
        print("King Count:" + str(king))
    if (len(piles) - 1) == 0 and king == 4:
        print("I'm pretty sure you won lol.")
    else:
        print("Game Over. You Lost. I think. I'm not entirely sure how this game works.")
    
            
