rail_count, item_count_each_rail, box_size = map(int, input().split(" "))

rails = []
box = []
output = []

for _ in range(rail_count):
    rails.append(list(input()))

actions = map(int, input().split())

for action in actions:
    if action > 0 and action <= rail_count:
        rail = rails[action - 1]
        if len(rail) > 0:
            if len(box) >= box_size:
                output.append(box.pop())
            box.append(rail.pop(0))
    elif action == 0:
        if len(box) > 0:
            output.append(box.pop())
    else:
        break

print("".join(output))
