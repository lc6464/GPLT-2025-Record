a1, a2, n = (int(i) for i in input().split(" "))

result_list = [a1, a2]

for i in range(n):
    next_result_str = str(result_list[i] * result_list[i + 1])
    for i in next_result_str:
        result_list.append(int(i))

    if len(result_list) >= n:
        break

print(" ".join((str(i) for i in result_list[:n])))