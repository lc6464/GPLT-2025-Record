number = int(input())

count = 2 * number + 1
pre = number + 1
post = number

start = number * count

pre_range = range(start, start + pre)
post_range = range(start + pre, start + pre + post)

print("^2 + ".join((str(i) for i in pre_range)) + "^2 =")
print("^2 + ".join((str(i) for i in post_range)) + "^2")