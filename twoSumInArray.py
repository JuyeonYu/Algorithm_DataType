# 1. 숫자로 이뤄져있는 리스트1개(nums), 숫자1개(target)를 파라미터로 받는 메소드르 만든다.
# 2. nums에서 두개의 숫자를 더해서 target을 만들 수 있는 값을 찾는다
# 3. 2에서 찾는 두개의 값의 인덱스를 반환한다.

def twoSum(nums: list[int], target: int) -> list[int]:
    k = 1
    for i in nums[:-1]:
        for j in nums[k:]:
            if i + j == target:
                return [i, j]
        k += 1
