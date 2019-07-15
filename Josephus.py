# https://www.acmicpc.net/problem/1158

# 시간복잡도 O(n)

def get_answer(a, b):
    # 0부터 a까지 숫자가 들어있는 리스트(my_list)를 만듦
    my_list = list(range(1, a + 1))

    # 답을 넣을 리스트를 만듦
    answer_list = []

    # b + b만큼 건너뛰기 위한 변수 만듦
    leap_b = b

    # my_list 길이만큼 반복문을 돌면서
    for i in range(len(my_list)):

        # 정답 리스트에 b만큼 건너뛴 인덱스 값을 넣음
        answer_list.append(my_list[(leap_b - 1)])
        leap_b = leap_b + b

        if leap_b > len(my_list):
            leap_b = leap_b % len(my_list)
    return answer_list

