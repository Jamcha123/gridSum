grid = [[9, 8, 3], [12, 5, 1], [2, 5, 7]]
rows = []
indexRows = 0
for x in range(len(grid)): 
    target = 0
    for x in range(len(grid[indexRows])):
        target += grid[indexRows][x]
    rows.append([target])
    indexRows += 1
cols = []
indexCols = 0
for x in range(len(grid)):
    target = 0
    for x in range(len(grid)):
        target += grid[x][indexCols] 
    cols.append([target])
    indexCols += 1
score = []
for x in range(len(grid)):
    if (rows[x][0] == cols[x][0]):
        score.extend(["draw"])
    elif (rows[x][0] > cols[x][0]): 
        score.extend(["rows win"])
    elif (rows[x][0] < cols[x][0]): 
        score.extend(["cols win"])
print(score)