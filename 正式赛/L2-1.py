charList = list(input())

index = 5
while True:
    try:
        index = charList.index(")")
        # print(index)
        if charList[index-1] == "(":
            for _ in range(2):
                charList.pop(index-1)
        else:
            for i in range(2, 6):
                if charList[index-i] == "(":
                    print("".join(charList[index-i+1:index]))
                    for _ in range(i+1):
                        charList.pop(index-i)
                    break
        # print(charList)
    except:
        break