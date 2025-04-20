count = int(input())

points = [set(), set(), set()]

# maxX0 = -1
# maxX1 = -1
# maxX2 = -1

for _ in range(count):
    x, y = map(int, input().split())
    points[y].add(x)
    # if y == 0 and x > maxX0:
    #     maxX0 = x
    # elif y == 1 and x > maxX1:
    #     maxX1 = x
    # elif y == 2 and x > maxX2:
    #     maxX2 = x

# halfX0 = maxX0 // 2 + 1
# halfX1 = maxX1 // 2 + 1
# halfX2 = maxX2 // 2 + 1

output = []

for x1 in points[1]:
    for x0 in points[0]:
        diff = x1 - x0
        if (x1 + diff) in points[2]:
            result = ([x0, 0], [x1, 1], [x1 + diff, 2])
            if not result in output:
                output.append(result)

output = sorted(output, key = lambda i: i[0] + i[1] * 100000)

for i in output:
    print(" ".join(map(str, i)))