t = [1, 2, 3, 3, 4, 4, 5]

dedup = []
[dedup.append(x) for x in t if x not in dedup]

print(dedup)