# https://www.acmicpc.net/problem/1016
# 풀이
# 1. boolean 변수 upperDouble = False
# 2. int 변수 count = 0
# 3. int 변수 x = 1
# 4. 매개변수로 (int)min과 (int)max를 받는 함수를 정의한다.
#
# 4. min과 max의 크기를 비교한다.
#     4-1. min이 max보다 같거나 크면 매개변수 오류를 반환하며 함수 종료
#
#     4-2. min이 max보다 작으면
#         5. x의 제곱수를 y를 구한다. (x = 2)
#
#         7.  y와 min, max 크기를 비교한다.
#             7-1. y가 max보다 크면
#
#                 8. upperDouble를 검사한다.
#                     8-1. True면
#                         9. count를 반환하고 함수 종료
#                     8-2. False면
#                         10. x = x + x
#                         11. upperDouble = False
#                         12. 5로 이동
#
#             7-2. y가 max보다 작으면
#                 13. y = y + y를 한다.
#                 14. count = count + 1을 한다.
#                 15. upperDouble = True
#                 16. 7로 이동한다.
#
#              7-3. y가 min보다 작으면
#                 17. int startPoint = min/y 반올림한다.
#                 18. y = y * startPoint
#                 19. 7로 이동한다.