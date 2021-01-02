class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lowerIdx = self.lowerBound(nums,target) # target이 처음 나타나는 인덱스
        upperIdx = self.upperBound(nums,target) # target보다 큰 값이 처음 나타나는 인덱스
        
        subs = upperIdx - lowerIdx
        
        if subs <= 0: return [-1,-1]
        else: return [lowerIdx,upperIdx-1]
    
    
    def lowerBound(self, nums, target): 
        left = 0
        right = len(nums)
        
        while left < right:
            mid = (left+right)//2
            
            if target <= nums[mid]:
                right = mid
            else:
                left = mid+1
        return right
    
    
    def upperBound(self, nums, target): 
        left = 0
        right = len(nums)
        
        while left < right:
            mid = (left+right)//2
            
            if target < nums[mid]:
                right = mid
            else:
                left = mid+1
        return right
