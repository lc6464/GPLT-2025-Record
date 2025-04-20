remain, cityCount, pathCount, questionCount = map(int, input().split())

paths = []

for _ in range(pathCount):
    a, b, costs, happiness = map(int, input().split())
    paths.append({
        "a": a,
        "b": b,
        "costs": costs,
        "happiness": happiness
    })

paths = sorted(paths, key = lambda x: x["costs"] * 10000 + x["a"] * 100 + x["b"])
froms = map(int, input().split())

for f in froms:
    print("T_T")