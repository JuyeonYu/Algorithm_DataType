# 배열 안에 두 수를 더했을 때 가장 큰 수
# 해결법: 배열 안의 가장 큰 수는
# 가장 큰 수 + 두번째로 큰 수 이다.

def get_answer(get_list):
    largest = get_list[0]
    answer_list = []

    for num in get_list[1:]:
        if num > largest:
            largest = num

    answer_list.append(largest)
    get_list.remove(largest)

    if len(answer_list) != 2:
        largest = 0
        for num in get_list[1:]:
            if num > largest:
                largest = num
    answer_list.append(largest)

    return answer_list[0] + answer_list[1]
