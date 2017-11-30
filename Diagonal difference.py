import math

n = int(input())
matrix = []
diag_dif = 0
left_diag = 0
right_diag = 0
for i in range (n):
    matrix.append(input().split())
    left_diag += int(matrix[i][i])
    right_diag += int(matrix[i][-i-1])
print(abs(left_diag - right_diag))
