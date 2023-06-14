

n = int(input())
D = [{'s': 0, 'p': 0}] * 2 + [{'s': float('inf'), 'p': 0}
                              for i in range(n-1)]


def input_table(next_i):
    global D, n, cur_steps, cur_val
    if next_i > n:
        return 0
    if cur_steps >= D[next_i]['s']:
        return 0
    D[next_i]['s'], D[next_i]['p'] = cur_steps + 1, cur_val


for i in range(1, n+1):
    cur_steps = D[i]['s']
    cur_val = i
    input_table(i+1)
    input_table(i*2)
    input_table(i*3)

print(D[-1]['s'])
prev = D[-1]['p']
nums = [n]

while prev != 0:
    nums.insert(0, prev)
    prev = D[prev]['p']

print(*nums)
