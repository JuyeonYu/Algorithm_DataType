# 1. 배열에는 숫자가 들어있음
# 2. 숫자는 오름차순으로 정렬되어 있음
# 3. 배열에는 중복된 숫자가 들어갈 수 있음
# 4. 이 배열에서 중복된 숫자를 제거하고 중복되지 않는 숫자만을 셀 때 그 갯수는?
# 시간 복잡도 0(n)
def remove_duplicated_in_list(list):
    dictionary = {}
    for num in list:
        dictionary.setdefault(num, None)
    return len(dictionary)


def remove_duplicated_in_list_using_set(list):
    sett = set()
    for num in list:
        sett.add(num)

    return len(sett)