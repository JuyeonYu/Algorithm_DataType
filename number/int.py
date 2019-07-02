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
print(word[5:])

#문자열 메소드
# A.join(a) 리스트 a에 있는 모든 문자열은 하나의 단일 문자열 A로 결합
singer = ["아이유", "볼빨간사춘기", "방탄소년단"]
print("-".join(singer))
print("-".join(reversed(singer)))

#lust, rjust /
# A.ljust(width, fillchat) 문자열 A 맨 처음부터 문자열을 포함한 길이 width만큼 fillchar를 채운다.
dancer = "마이클잭슨"
print(dancer.ljust(10, "*"))
print(dancer.rjust(10, "*"))

#A.format() 문자열 A에 변수 추가 하거나 형식화
"{0} {1}".format("안녕", "나야")

#f string / 파이썬 3.6이상부터 사용가능 기존 %나 format 방식 대체
name = "알프레도"
print(f"그의 이름은 {name!r}입니다") # !r을 붙이면 변수 양옆 외따옴표 repr(name) 과 같은 결과

#리스트 컴프리헨션
#[항목 for 항목 in 반복 가능한 객체]
#[표현식 for 항목 in 반복 가능한 객체]
#[표현식 for 항목 in 반복 가능한 객체 if 조건문]

a = [y for y in range(1900, 1940) if y%4 ==0]
print("리스트 컴프리헨션1: ", a)
b = [2**i for i in range(12)]
print("리스트컴프리헨션2: ", b)
c = [x for x in b if x%4 ==0]
print("리스트컴프리헨션3: ", c)
