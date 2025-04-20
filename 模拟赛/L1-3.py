weight = int(input())

result = 0

if weight <= 100:
    if weight % 10 == 0:
        result = weight - 10
    else:
        result = weight // 10 * 10
else:
        result = 100

print(f"Gong xi nin! Nin de ti zhong yue wei: {result} duo jin")