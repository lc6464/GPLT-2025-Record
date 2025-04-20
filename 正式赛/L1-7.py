import sys

number = int(input())

for k in range(30, 0, -1):
    for n in range(2, 2 ** 20):
        tempRange = range(1, n)
        tempResult = sum((i ** k for i in tempRange))
        if tempResult < number:
            continue
        elif tempResult == number:
            print(f"^{k}+".join(map(str, tempRange)), "^", k, sep="")
            sys.exit(0)
        else:
            break

print(f"Impossible for {number}.")