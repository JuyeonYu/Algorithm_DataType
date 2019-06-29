def countdown_while(num):
    while num > 0:
        print(num)
        num = num -1

def countdown_self(num):
    print(num)
    if num > 1:
        countdown_self(num-1)

def quick_sort(arr):
    left, right, equal = [],[],[]
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                equal.append(arr[i])
        return quick_sort(left) + equal + quick_sort(right)