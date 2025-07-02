def get_matrix(r, c):
    matrix = []
    print(f"Enter the elements of {r} rows and {c} columns (space separated):")
    for _ in range(r):
        row = list(map(int, input().split()))
        while len(row) != c:
            print(f"Please enter exactly {c} numbers:")
            row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def print_matrix(m):
    for row in m:
        print(' '.join(map(str, row)))

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        print("Cannot multiply matrices")
        return None
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

print("Enter size of Matrix A (rows and columns):")
r1, c1 = int(input()), int(input())
A = get_matrix(r1, c1)

print("Enter size of Matrix B (rows and columns):")
r2, c2 = int(input()), int(input())
B = get_matrix(r2, c2)

print("\nMatrix A:")
print_matrix(A)
print("\nMatrix B:")
print_matrix(B)

if r1 == r2 and c1 == c2:
    print("\nA + B =")
    print_matrix(add_matrices(A, B))
    print("\nA - B =")
    print_matrix(subtract_matrices(A, B))
else:
    print("\nCannot add or subtract matrices of different sizes.")

print("\nA x B =")
product = multiply_matrices(A, B)
if product:
    print_matrix(product)
