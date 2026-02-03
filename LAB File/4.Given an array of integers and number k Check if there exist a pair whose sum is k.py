a = [1, 2, 3, 4, 5]
k = 6

seen = set()
pairs = []

for val in a:
    diff = k - val
    if diff in seen:
        pairs.append((diff, val))
    seen.add(val)

print(pairs)
