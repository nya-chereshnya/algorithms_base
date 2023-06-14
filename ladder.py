n = int(input())
stairs = list(map(int, input().split()))
stairs_sum = [0] + [stairs[0]]
# print(stairs, n)
for i in range(1, n):
    max_n = max(stairs_sum)
    stairs_sum[0], stairs_sum[1] = stairs_sum[1],  max_n + stairs[i]
print(stairs_sum[-1])
