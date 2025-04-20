rawLength, actionCount = map(int, input().split())

numberList = list(map(int, input().split()))

for _ in range(actionCount):
    action = int(input())
    if action == 1:
        needToSliceList = list(map(int, input().split()))
        needToSliceLength = needToSliceList.pop(0)
        sliceTargetList = list(map(int, input().split()))
        sliceTargetLength = sliceTargetList.pop(0)
        for i in range(len(numberList) - needToSliceLength + 1):
            if numberList[i:(i+needToSliceLength)] == needToSliceList:
                for _ in range(needToSliceLength):
                    numberList.pop(i)
                for sliceIndex in range(sliceTargetLength):
                    numberList.insert(i + sliceIndex, sliceTargetList[sliceIndex])
                break
    if action == 2:
        index = 1
        for _ in range(len(numberList) * 2):
            sumOf2Number = sum(numberList[index-1:index+1])
            if sumOf2Number % 2 == 0:
                numberList.insert(index, sumOf2Number // 2)
                index += 2
            else:
                index += 1
            
            if index >= len(numberList):
                break
    if action == 3:
        reverseStart, reverseStop = map(int, input().split())
        reverseStart -= 1
        reverseStop -= 1
        reverseLength = reverseStop - reverseStart + 1
        reverseTarget = numberList[reverseStart:(reverseStop+1)]
        reverseTarget.reverse()
        for _ in range(reverseLength):
            numberList.pop(reverseStart)
        for reverseIndex in range(reverseLength):
            numberList.insert(reverseStart + reverseIndex, reverseTarget[reverseIndex])

print(" ".join(map(str, numberList)))