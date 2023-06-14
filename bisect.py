import bisect

m, n = map(int, input().split())

points = []
X = []
Y = []

for i in range(m):
    segment = list(map(int, input().split()))
    X.append(segment[0])
    Y.append(segment[1])

X.sort()
Y.sort()

points = list(map(int, input().split()))


for i in points:
    print(bisect.bisect_right(X, i) - bisect.bisect_left(Y, i), end=" ")
