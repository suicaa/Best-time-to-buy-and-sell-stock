'''例子1
8 8 3 3 5 0 0 3 1 4 .  一共十个数字
从左边开始
0 0 0 0 2 2 2 3 3 4
例子2
           1, 7, 15, 6, 57, 32, 76
从左边开始 0，6，14，14，56，56，75
从右边开始 75，70，70，70，44，44，0
'''

def max_left(arr):
    list_fromleft = [0]
    brr = []
    for i in range(n):
        if i < n:
            brr.append(arr[i])
            if arr[i] - min(brr) > max(list_fromleft):
                list_fromleft.append(arr[i] - min(brr))
            else:
                list_fromleft.append(list_fromleft[i])
    list_fromleft.append(0)
    return list_fromleft

def max_right(arr):
    list_fromright = [0]            #1, 7, 15, 6, 57, 32, 76
    crr = []                        #从左边开始 0，6，14，14，56，56，75
    for i in range(n):              #从右边开始 75，70，70，70，44，44，0
        if i < n:
            j = n - i - 1
            crr.append(arr[j])
            if max(crr) - arr[j] > max(list_fromright):
                list_fromright.insert(0, max(crr) - arr[j])
            else:
                list_fromright.insert(0, list_fromright[0])
    list_fromright.insert(0, 0)
    return list_fromright

def best_transactions(arrrrr):
    gain_loss = []
    for i in range(len(max_right(arrrrr))):
        gain_loss.append(max_left(arrrrr)[i] + max_right(arrrrr)[i])
    return max(gain_loss)

n = int(input())
arrrrr = []
for i in range(n):
    arrrrr.append(int(input()))

print(best_transactions(arrrrr))
