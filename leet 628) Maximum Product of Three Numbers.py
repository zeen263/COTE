class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 정렬하고 나면 최대값이 가능한 조합 : (마이너스두개 플러스한개) 또는 (플러스세개)
        nums = sorted(nums)   
        res1 = nums[0]*nums[1]*nums[-1]
        res2 = nums[-1]*nums[-2]*nums[-3]
        
        res = res1 if res1 > res2 else res2
        return res
