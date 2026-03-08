m, n = map(int,input().split())
data = []
for _ in range(m):
    row = list(map(int,input().split()))
    data.append(row)

print(data)

#設pivot為最左邊的元素