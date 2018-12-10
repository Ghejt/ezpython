def generate(prev_value):
    return ((1103515245*prev_value) + 12345) % 2**31

def rand_int(curr_value, lower, upper):
    bounds = (upper - lower) + 1
    scale = curr_value % bounds
    return lower + scale

def main():
    seed = int(input("Seed: "))
    cont = "y"
    while cont == "y" or cont == "yes":
        lower = int(input("Lower bound: "))
        upper = int(input("Upper bound: "))
        if upper <= lower:
            print("Lower must be less than upper, silly.")
        else:
            prev_value = seed
            curr_value = generate(prev_value)
            curr_value = rand_int(curr_value, lower, upper)
            print("Random number using " + str(seed) + ": " + str(curr_value))
            cont = input("Continue? (y or n): ")
            cont = cont.lower()
            seed = generate(prev_value)
