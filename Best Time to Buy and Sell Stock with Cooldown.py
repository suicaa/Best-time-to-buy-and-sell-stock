def best_transaction(arr):
    if len(arr) < 2:
        return 0

    n = len(arr)

    hold = [0] * n
    unhold = [0] * n

    hold[0] = 0 - arr[0]
    unhold[0] = 0
    hold[1] = max(-arr[0], -arr[1])
    unhold[1] = max(arr[1] - arr[0], 0)

    for i in range(2, n):
        hold[i] = max(hold[i - 1], unhold[i - 2] - arr[i])
        unhold[i] = max(hold[i - 1] + arr[i], unhold[i - 1])
    return unhold[-1]

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(best_transaction(arr))
