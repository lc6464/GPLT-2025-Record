n, start, stop = map(int, input().split())

found = False

for number in range(start, stop + 1):
    valid = True
    for index in range(2, n + 1):
        if (number // (10 ** (n - index)) % index) != 0:
            valid = False
            break

    if valid:
        print(number)
        found = True

if not found:
    print("No Solution")