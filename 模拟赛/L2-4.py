count = int(input())
number_bits = list(map(int, input().split()))

numbers = []
if count == 3:
    numbers.extend([
        number_bits[0] * 100 + number_bits[1] * 10 + number_bits[2],
        number_bits[1] * 100 + number_bits[2] * 10 + number_bits[0],
        number_bits[2] * 100 + number_bits[0] * 10 + number_bits[1],
        number_bits[0] * 100 + number_bits[2] * 10 + number_bits[1],
        number_bits[2] * 100 + number_bits[1] * 10 + number_bits[0],
        number_bits[1] * 100 + number_bits[0] * 10 + number_bits[2]
    ])
elif count == 4:
    numbers.extend([
        number_bits[0] * 1000 + number_bits[1] * 100 + number_bits[2] * 10 + number_bits[3],
        number_bits[1] * 1000 + number_bits[2] * 100 + number_bits[3] * 10 + number_bits[0],
        number_bits[2] * 1000 + number_bits[3] * 100 + number_bits[0] * 10 + number_bits[1],
        number_bits[3] * 1000 + number_bits[0] * 100 + number_bits[1] * 10 + number_bits[2],

        number_bits[0] * 1000 + number_bits[1] * 100 + number_bits[3] * 10 + number_bits[2],
        number_bits[1] * 1000 + number_bits[3] * 100 + number_bits[2] * 10 + number_bits[0],
        number_bits[3] * 1000 + number_bits[2] * 100 + number_bits[0] * 10 + number_bits[1],
        number_bits[2] * 1000 + number_bits[0] * 100 + number_bits[1] * 10 + number_bits[3],

        number_bits[0] * 1000 + number_bits[2] * 100 + number_bits[1] * 10 + number_bits[3],
        number_bits[2] * 1000 + number_bits[1] * 100 + number_bits[3] * 10 + number_bits[0],
        number_bits[1] * 1000 + number_bits[3] * 100 + number_bits[0] * 10 + number_bits[2],
        number_bits[3] * 1000 + number_bits[0] * 100 + number_bits[2] * 10 + number_bits[1],

        number_bits[0] * 1000 + number_bits[2] * 100 + number_bits[3] * 10 + number_bits[1],
        number_bits[2] * 1000 + number_bits[3] * 100 + number_bits[1] * 10 + number_bits[0],
        number_bits[3] * 1000 + number_bits[1] * 100 + number_bits[0] * 10 + number_bits[2],
        number_bits[1] * 1000 + number_bits[0] * 100 + number_bits[2] * 10 + number_bits[3],

        number_bits[0] * 1000 + number_bits[3] * 100 + number_bits[1] * 10 + number_bits[2],
        number_bits[3] * 1000 + number_bits[1] * 100 + number_bits[2] * 10 + number_bits[0],
        number_bits[1] * 1000 + number_bits[2] * 100 + number_bits[0] * 10 + number_bits[3],
        number_bits[2] * 1000 + number_bits[0] * 100 + number_bits[3] * 10 + number_bits[1],

        number_bits[0] * 1000 + number_bits[3] * 100 + number_bits[2] * 10 + number_bits[1],
        number_bits[3] * 1000 + number_bits[2] * 100 + number_bits[1] * 10 + number_bits[0],
        number_bits[2] * 1000 + number_bits[1] * 100 + number_bits[0] * 10 + number_bits[3],
        number_bits[1] * 1000 + number_bits[0] * 100 + number_bits[3] * 10 + number_bits[2],
    ])

def sum_with_2(l):
    return sum(map(lambda x: x**2, l))

from random import randint

tested = set()

while True:
    indexes = []
    while len(indexes) < count * (count - 1) * (count - 2):
        next_id = randint(0, 5)
        if not next_id in indexes:
            indexes.append(next_id)
    if tuple(indexes) in tested:
        continue
    else:
        tested.add(tuple(indexes))
    if sum_with_2([numbers[indexes[0]], numbers[indexes[1]], numbers[indexes[2]]]) == sum_with_2([numbers[indexes[3]], numbers[indexes[4]], numbers[indexes[5]]]):
        print(numbers[indexes[0]], numbers[indexes[1]], numbers[indexes[2]], sep="\n")
        break