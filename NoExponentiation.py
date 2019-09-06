# https://www.acmicpc.net/problem/1016
# 풀이
# https://www.acmicpc.net/problem/1016
# 풀이
# 1. 세팅
#     x = 2
#     y = x의 배수
#     count = y의 배수가 min과 max사이에 몇개 있는지 저장
#     isUpper2Y = y가 2배수 이상인지 저장
#     min과 max를 매개변수로 받는 함수 정의
#
# 2. 매개 변수 제대로 들어왔는지 검사
#     min과 max가 정수인지
#     min이 max보다 작은지
#     max가 4보다 작은지
#         max가 4보다 작다면 시작을 할 수 없음
#         2 제곱이 4
#
# 3. x의 제곱 수 계산하는 함수 정의 후 실행
#     y = 4로 첫 시작
#
# 4. x,y를 min, max와 비교하는 함수 정의 후 실행
#     y가 최대값 보다 크다면
#         y가 2배수 이상이면서 x + 1의 제곱이 최대값 보다 크다면
#             ex) 최소값이 1이고 최대값이 10일 때 y가 9라면(9 = 3의 제곱) x가 4일 상황(4의 제곱은 16)을 고려할 필요가 없음
#             count를 반환하고 함수 종료
#         아니면
#             x = x + 1
#             3. 으로 이동
#             4. 로 이동
#     y가 최소값 이상이면서 최대값 이하일때
#         count = count + 1
#         isUpper2Y = True
#         y = y + (x * x)
#         4. 로 이동
#     y가 최소값 보다 작다면 (최소값을 100으로 시작할 경우)
#         startPoint = min / y
#         y = y * startPoint
#
#         y가 min보다 작다면
#             y = y + (x * x)
#         4. 로 이동
        


import math


class NoExponentiation:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    x = 2
    y = 0
    count = 0
    isUpper2Y = False

    def getNoExponentiation(self):
        if not isinstance(self.min, int) and not isinstance(self.max, int) and self.min > self.max and self.max < 4:
            return "parameter error"
        else:
            self.calculateXTimesX()
            self.compareXY()

    def calculateXTimesX(self):
        self.y = self.x * self.x

    def compareXY(self):
        if self.y > self.max:
            if self.isUpper2Y and (self.x + 1) * (self.x + 1) > self.max:
                print(((self.max - self.min) + 1) - self.count)
                return ((self.max - self.min) + 1) - self.count
            else:
                self.x = self.x + 1
                self.calculateXTimesX()
                self.compareXY()

        elif self.y >= self.min and self.y <= self.max:
             self.y = self.y + (self.x * self.x)
             self.count = self.count + 1
             self.isUpper2Y = True
             self.compareXY()
        elif self.y < self.min:
             startPoint = math.ceil(self.min // self.y)
             self.y = self.y * startPoint
             if not self.y >= self.min:
                self.y = self.y + self.x * self.x
             self.compareXY()

