rows, columns, height = (int(i) for i in input().split(" "))

playground_matrix = []
for _ in range(rows):
    playground_matrix.append([int(i) for i in input().split(" ")])

framework_points = []
empty_points = []
for r in range(rows):
    for c in range(columns):
        if playground_matrix[r][c] == 0:
            empty_points.append((r, c))
        elif playground_matrix[r][c] < 0:
            framework_points.append((r, c))

def is_visible(point, framework):
    pr, pc = point
    fr, fc = framework
    if pr == fr:
        for h in playground_matrix[pr][min(pc, fc)+1:max(pc, fc)]:
            if h >= height:
                return False
        return True
    elif pc == fc:
        for row in playground_matrix[min(pr, fr)+1:max(pr, fr)]:
            if row[pc] >= height:
                return False
        return True
    return False

count = 0
first_X = -1
first_Y = -1
max_visible_frameworks = 0

for point in empty_points:
    visible_frameworks = 0
    for framework in framework_points:
        if is_visible(point, framework):
            visible_frameworks += 1
    if visible_frameworks >= 3:
        count+=1
        if max_visible_frameworks < visible_frameworks:
            first_X, first_Y = point
            max_visible_frameworks = visible_frameworks

print(count)
print(first_X, first_Y)