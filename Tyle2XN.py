# https://www.acmicpc.net/problem/11726
#
# 풀이1
# 숫자 n을 1 + 2로 구성할 수 있는 경우의 수를 구한다.
# ex) 숫자가 5일 때 5를 1 + 2로 만들 수 있는 경우의 수는
# 1. 1+1+1+1+1
# 2. 1+1+1+2
# 3. 1+1+2+1
# 4. 1+2+1+1
# 5. 2+1+1+1
# 6. 1+2+2
# 7. 2+1+1
# 8. 2+1+2
# 답은 8
#
# 풀이2
# 풀이1로 풀이를 하다보니 이 문제의 답은 피보나치 수열이라는 것을 밢견
# 숫자 n이 1일 때 답은 1
# 숫자 n이 2일 때 답은 2
# 숫자 n이 3일 때 답은 3
# 숫자 n이 4일 때 답은 5
# 숫자 n이 5일 때 답은 8
# 숫자 n이 6일 때 답은 13
# .
# .
# .
# 숫자 n이 9일 때 답은 55
#
# 해당 문제는 풀이2로 풀었음

class Tyle2X:
    fibonacciList = [1,2]

    def __init__(self, n):
        self.n = n

    def getFibonacxciNumber(self):
        if self.n == 1 or self.n == 2:
            return self.n
        else:
            for i in range(self.n-2):
                self.fibonacciList.append(self.fibonacciList[i]+self.fibonacciList[i+1])
            return self.fibonacciList[self.n-1]

