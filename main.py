def sweep_mines(mines):
  for i in range(len(mines)):
    for ii in range(len(mines[i])):
      if mines[i][ii] == "-":
         mines[i][ii] = str(mine_counter(mines, i, ii))
  print(mines)
  return mines

def mine_counter(mines, arr_index, index):
  count = 0
  count = count_row(mines, arr_index, index, count) #check current row
  count = count if arr_index == len(mines) - 1 else count_row(mines, arr_index + 1, index, count) #check bottom row
  count = count if arr_index == 0 else count_row(mines, arr_index - 1, index, count) #check top row
  return count

def count_row(mines, arr_index, index, count): #query rows
  if index != 0 and mines[arr_index][index - 1] == '#': #check previous tile
    count += 1
  if mines[arr_index][index] == '#': #check current tile
    count += 1
  if index != len(mines[arr_index]) - 1 and mines[arr_index][index + 1] == '#': #check next tile
    count += 1
  return count
