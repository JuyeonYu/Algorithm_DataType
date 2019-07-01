# 정수를 나타내는데 필요한 바이트 수
print((999).bit_length())

# 문자열- > 정수 캐스팅
s = '11'
d = int(s)
print("캐스팅된 숫자는 ",d)

#int(x, radix) -> radix진수로 표현된 문자열 x를 10진수로 변환한다.
print(int('11', 2)) # 2진수로 표현된 문자열 '11'을 10진수로 표현하면?

# divmod(a,b) a를 b로 나눌때 몫과 나머지를 반환한다.
print(divmod(45,6))

# 내장 시퀀스 슬라이싱 연산자 seq[시작:끝:스탭] 스탭의 의미 뭔지 모르겠음
word = "공부해서 더러운꼴 보지말자"
print(word[0])
print(word[-1])
print(word[0:3])
print(word[-3:])

