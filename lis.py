
arr_len = int(input())
arr = list(map(int, input().split()))

dp = [1] * arr_len


def lis(arr, dp):
    for i in range(arr_len):
        for j in range(i):
            if arr[j] <= arr[i] and dp[j] + 1 > dp[i] and arr[i] % arr[j] == 0:
                dp[i] = dp[j] + 1


lis(arr, dp)
print(max(dp))
