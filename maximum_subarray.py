# https://leetcode.com/problems/maximum-subarray/description/

# 숫자가 들어있는 배열이 주어진다
# 배열 안 두 수의 합이 가장 큰 값을 찾아라

# 두 수의 값이 가장 크려면 가장 큰 수 + 두번째로 큰수를 하면됨

def answer(list):
    # 가장 큰수를 찾는다
    # 리스트 0번째를 기준으로 기준보다 큰 숫자를 배열에 넣는다.
    # 리스트의 갯수가 1이 될때까지 반복한다.
    largerThanPivot = []

    for num in list[1:]:
        if num > list[0]:
            largerThanPivot.append(num)

    if len(largerThanPivot) == 0:

        answer(list)
        return list[0]

# 배열 안에 두 수를 더했을 때 가장 큰 수
# 해결법: 배열 안의 가장 큰 수는
# 가장 큰 수 + 두번째로 큰 수 이다.

def get_answer(get_list):
    largest = 0

    #가장 큰 수 찾기
    for num in get_list:
        if num > largest:
            largest = num

    answer = largest
    get_list.remove(largest)

    # 가장 큰 수 초기화
    largest = 0

    # 두번째로 큰 수 찾기
    for num in get_list:
        if num > largest:
            largest = num
    answer = answer + largest
    return answer
>>>>>>> 717841d770c32d85b951004bb8593aca29d4b1d4
