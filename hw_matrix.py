import numpy as np

def generate_matrix(m, n):
    return (np.random.randint(0, 99, size = (m, n)))

def add(A, B):
    print(np.add(A, B))
    
def subtract(A, B):
    print(np.subtract(A,B))
    
def transpose(A):
    print(A.T)
    
def dot_product(A, B):
    print(np.dot(A, B))

def main():
    rowA = int(input("Rows in matrix A: "))
    columnA = int(input("Columns in matrix A: "))
    rowB = int(input("Rows in matrix B: "))
    columnB = int(input("Columns in matrix B: "))
    rowC = int(input("Rows in matrix C: "))
    columnC = int(input("Columns in matrix C: "))
    A = generate_matrix(rowA, columnA)
    B = generate_matrix(rowB, columnB)
    print('A:\n', A) 
    print('B:\n', B)
    

    print('1. Calculate A+B\n2. Calculate A-B\n3. Calculate transpose of A\n4. Calculate transpose of B\n5. Calculate A dot B\n6. Quit')
    choice = 0
    while choice != '6':
        if choice == '1':
            add(A, B)
        elif choice == '2':
            subtract(A, B)
        elif choice == '3':
            transpose(A)
        elif choice == '4':
            transpose(B)
        elif choice == '5':
            dot_product(A, B)
        choice = input('Your choice: ')
    print("Bye!")
