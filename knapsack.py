
W, n = map(int, input().split())
ingots = list(map(int, input().split()))
# gavno = list(map(int, input().split()))

X = [[0 for i in range(W+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, W+1):
        X[i][j] = X[i][j-1]
        if j >= ingots[i-1]:
            X[i][j] = max(X[i-1][j], X[i-1][j-ingots[i-1]] + ingots[i-1])
        else:
            X[i][j] = X[i-1][j]

print(X[-1][-1])
# for i in range(n+1):
#     print(X[i])
