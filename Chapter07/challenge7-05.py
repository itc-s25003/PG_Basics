one = [8, 19, 148, 4]
two = [9, 1, 33, 83]
three = []

for i in one:
    for j in two:
        result = i * j
        three.append(i * j)

print(three)

