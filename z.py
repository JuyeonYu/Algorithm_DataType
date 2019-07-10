# 백준 z
# https://www.acmicpc.net/problem/1074
# Z의 각 모서리를 1,2,3,4 분면으로 나눔

# 1. 숫자가 몇 사분면에 위치했는지 구하면
# 2. 몇 번째로 방문했는지 구할 수 있음

#몇 사분면에 위치했는지 구함.
#배열을 반환함
# ex) [1,2,3] = 1사분면 안에 2사분면 안에 3사분면에 r,c가 위치해있음

location_list = []
def get_location(n,r,c):
    if n is not 0:
        if r < (2 ** n) // 2 :
            r_location = {1,2}
        else:
            r_location = {3,4}
            r = r - (2 ** (n-1))

        if c < (2 ** n) // 2 :
            c_loation = {1,3}
        else:
            c_loation = {2,4}
            c = c - (2 ** (n-1))

        n = n - 1
        location_list.append(r_location & c_loation)
        get_location(n,r,c)
    return location_list

def get_answer(location_list): #몇번째로 방문했는지 구함
    if len(location_list) is not 0:
        n = list(location_list.pop(0)).pop()
    else:
        return 0
    t1 = 2 ** (2 * (len(location_list))) * (n-1)
    return t1 + get_answer(location_list)
