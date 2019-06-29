my_list = [0,1,2,3,4]

def binary_serach(list, target):
    low = 0
    high = len(list) - 1

    if target > high:
        return None

    if target < low:
        return None

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if target == guess:
            return mid

        if target > guess:
            low = mid + 1

        else:
            high = mid - 1
    return None

print(binary_serach(my_list, 3))


