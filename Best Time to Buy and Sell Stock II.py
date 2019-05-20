def best_transactions(arr):
    a = 0
    for i in range(n):
        if i < n - 1 and arr[i] < arr[i + 1]:
            a += arr[i + 1] - arr[i]
    return a




n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(best_transactions(arr))
