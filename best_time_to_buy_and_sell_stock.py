def get_answer(list):
    answer = 0
    for i in range(len(list) - 1):
        for number in list[1:]:
            temp = number - list[0]
            if temp > answer:
                answer = temp
        del list[0]
    return answer