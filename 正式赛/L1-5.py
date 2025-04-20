alphabet = "abcdefghijklmnopqrstuvwxyz"

inputCharList = list(input())

scoreList = list(map(int, input().split()))

outputCountList = [0] * 26

outputScore = 0

for c in inputCharList:
    index = alphabet.find(c)
    outputCountList[index] += 1
    outputScore += scoreList[index]

print(" ".join(map(str, outputCountList)))
print(outputScore)