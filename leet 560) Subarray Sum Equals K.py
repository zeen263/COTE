# 1) nums 리스트의 누적합을 딕셔너리 maps에 저장 {누적합:해당 값의 발생 횟수}
# 2) 누적합을 쭉 저장해놨는데 maps[p]와 maps[q]의 차가 k라면 nums[p]~nums[q] 사이에 있는 수의 합이 k라는 것
# 3) 근데 p~q까지 합의 차도 k, p~r까지 누적합의 차도 k일 수가 있다
#     (nums : [1 2 -1 1 2] 라면 0~1의 누적합도 3, 0~4의 누적합도 3)
#     (maps : [1 3  2 3 5])
# 4) k가 3일 경우 누적합들을 살펴봤을 때 걔네끼리의 차가 3인 횟수를 찾으면 된다
# 5) 이것을 하는 방법 : 새로운 누적합 S를 딕셔너리에 저장하면서, 앞에서 계산해온 값들 중 (S-k)가 나온 횟수를 체크하면 됨
#    S-k가 나온 '횟수'를 세는 이유 : 3번 항목

# 딕셔너리를 쓰는 이유는
# 1) 찾는 속도를 빠르게 하기 (누적합 값 n이 나온 횟수를 알고 싶으면 maps[n] 하면 됨)
# 2) 누적합을 키로 사용해서 공간을 줄이기 (리스트로 이걸 만들면 빈 공간이 너무 많이 생김)

class Solution(object):
    def subarraySum(self, nums, k):
        LEN = len(nums)
        cnt = 0
        sum = 0
        maps = {0:1}

        for i in range(LEN):
            sum += nums[i]

            if sum-k in maps:
                cnt += maps[sum-k]

            if sum in maps:
                maps[sum] += 1
            else:
                maps[sum] = 1

        return cnt

S = Solution()
ret = S.subarraySum([1,1,1],0)
print(ret)