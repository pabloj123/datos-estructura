a = [2, 1, 3, 4, 5, 3, 9]


for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

for a in a:
    print(a)

