# https://www.acmicpc.net/problem/1463
# 풀이
# 1. 3으로 나누어 0인 숫자면 3으로 나눈다
# 2. 2으로 나누어 0인 숫자면 2으로 나눈다
# 3. 1,2가 아니면 1을 뺀다.
# 4. 1로 이동
#     - 숫자가 1이되면 종료


class MakeItOne:
    n = 0
    count = 0

    def __init__(self, n):
        self.n = n

    def getAnswer(self):
        if self.n == 0:
            return self.count

        elif self.n % 3 == 0:
            self.n = self.n // 3
            self.countAndRepeatAgain()

        elif self.n % 2 == 0:
            self.n = self.n // 2
            self.countAndRepeatAgain()

        else:
            self.n = self.n - 1
            self.getAnswer()

    def countAndRepeatAgain(self):
        self.count = self.count + 1
        self.getAnswer()