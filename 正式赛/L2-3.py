count = int(input())

timestampsList = []
for _ in range(count):
    timestamps = input().split()
    startH, startM, startS = map(int, timestamps[0].split(":"))
    stopH, stopM, stopS = map(int, timestamps[1].split(":"))
    startTimestamp = startH * 3600 + startM * 60 + startS
    stopTimestamp = stopH * 3600 + stopM * 60 + stopS
    timestampsList.append((startTimestamp, stopTimestamp))

stopTimestamps = []
for timestamps in sorted(timestampsList, key = lambda x: x[1]):
    found = False
    for index in range(len(stopTimestamps)):
        if stopTimestamps[index] < timestamps[0]:
            stopTimestamps[index] = timestamps[1]
            found = True
            break
    
    if not found:
        stopTimestamps.append(timestamps[1])

print(len(stopTimestamps))