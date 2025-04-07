n, m = map(int, input().split(' '))

count = 0

a = list()
b = list()

for i in range(n):
    a.append(input())

for i in range(n):
    b.append(input())

for i in range(n):
    a2 = ''
    for j in range(m):
        a2 += a[i][j] * 2
    
    if a2 == b[i]:
        count += 1

if count == n:
    print('Eyfa')
else:
    print('Not Eyfa')