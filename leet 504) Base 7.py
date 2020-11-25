import sys

class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        if num < 0:
            res += '-'
            num = abs(num)
        elif num == 0:
            res = "0"

        gather = ""
        while num:
            remain = num % 7  # 먼저 나온 나머지일수록 뒤에 가야 함
            num //= 7
            gather += str(remain)

        res += gather[::-1]
        return res

sol = Solution()
n = int(sys.stdin.readline())
print(sol.convertToBase7(n))