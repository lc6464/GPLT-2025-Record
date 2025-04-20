rowCount, colCount = map(int, input().split())

countries = []
for _ in range(rowCount):
    countries.append(list(map(int, input().split())))

output = []
for selfRowIndex in range(rowCount):
    output.append([])
    for selfColIndex in range(colCount):
        distances = 0
        for targetRowIndex in range(rowCount):
            for targetColIndex in range(colCount):
                distances += max(abs(selfRowIndex - targetRowIndex), abs(selfColIndex - targetColIndex))
        # print(selfRowIndex, selfColIndex, distances)
        output[selfRowIndex].append(distances * countries[selfRowIndex][selfColIndex])

# print(countries)
# print(output)
for row in output:
    print(" ".join(map(str, row)))