rowLength, colLength, step = map(int, input().split())

mapMatrix = []

for _ in range(rowLength):
    mapMatrix.append(list(map(int, input().split())))

for _ in range(step):
    maxValue = mapMatrix[0][0]
    maxRow = 0
    maxCol = 0
    for rowIndex in range(len(mapMatrix)):
        for colIndex in range(len(mapMatrix[rowIndex])):
            if mapMatrix[rowIndex][colIndex] > maxValue:
                maxValue = mapMatrix[rowIndex][colIndex]
                maxRow = rowIndex
                maxCol = colIndex
    for row in mapMatrix:
        row.pop(maxCol)
    mapMatrix.pop(maxRow)

for row in mapMatrix:
    print(" ".join(map(str, row)))