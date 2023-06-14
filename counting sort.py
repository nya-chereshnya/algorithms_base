

n = int(input())
# for i in range(n):
arr = list(map(int, input().split()))
start = min(arr)
end = max(arr)
nums_range = end - start

count = [0] * (nums_range + 1)

for i in arr:
    count[i-start] += 1

for i in range(nums_range+1):
    if count[i] > 0:
        print((str(i+start) + ' ') * count[i], end='')
