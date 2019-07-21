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
