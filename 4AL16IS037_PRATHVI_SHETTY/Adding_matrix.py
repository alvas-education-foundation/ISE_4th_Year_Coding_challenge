# This program is to add two given matrices
M1 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]
M2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

sum = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

for i in range(len(M1)):
    for j in range(len(M1[0])):
        sum[i][j] = M1[i][j] + M2[i][j]

for num in sum:
    print(num)