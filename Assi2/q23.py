matrix = [list(map(int, input(f"Enter row {i+1}: ").split())) for i in range(2)]
r = int(input("Enter row: "))
c = int(input("Enter col: "))
print(matrix[r][c])
