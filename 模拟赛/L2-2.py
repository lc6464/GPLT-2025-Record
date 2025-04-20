count = int(input())
requests = []

def timeToSecond(time):
    hour, minute, second = map(int, time.split(":"))
    return hour * 3600 + minute * 60 + second

for _ in range(count):
    try:
        requests.append(tuple(map(timeToSecond, input().split(" "))))
    except:
        pass

requests = sorted(requests, key=lambda r: r[1])

last_end_time = -1
permitted_count = 0

for request in requests:
    if request[0] >= last_end_time:
        last_end_time = request[1]
        permitted_count += 1

print(permitted_count)