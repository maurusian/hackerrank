#!/bin/python3

import re

def word_connect(matrix):
    ss = ''
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            ss+=matrix[i][j]
    return ss

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

pattern = r"(?<=[A-Za-z0-9])([^0-9a-zA-Z]+)(?=[A-Za-z0-9])"
ss = word_connect(matrix)
print(re.sub(pattern,' ',ss))
