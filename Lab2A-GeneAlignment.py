def score(base1, base2):
    if base1 == '-' and base2 == '-':
            score = 0
    elif base1 == '-' or base2 == '-':
            score = -2
    elif base1 != base2:
            score = -1
    elif base1 == base2:
            score = 1
    return(score)
