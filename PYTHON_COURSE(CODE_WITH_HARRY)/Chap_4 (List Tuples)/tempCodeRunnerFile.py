[]
for i in range(4):
  transposed_row = []
  for row in matrix:
    transposed_row.append(row[i])
  transposed.append(transposed_row)
print(transposed)