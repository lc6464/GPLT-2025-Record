maxTemp, place, placeTemp = map(int, input().split())

if place == 1:
    if maxTemp >= 35 and placeTemp >= 33:
        print("Bu Tie")
        print(maxTemp)
    else:
        print("Bu Re")
        print(placeTemp)
else:
    if maxTemp >= 35 and placeTemp >= 33:
        print("Shi Nei")
        print(maxTemp)
    else:
        print("Shu Shi")
        print(placeTemp)