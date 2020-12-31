class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # left, right, mid를 비교하면 left<mid<right 순으로 커져야 함
        # l,r,m을 비교해서 정렬이 많이 된 쪽이 왼쪽인지 오른쪽인지 찾기 (어디를 기준으로 돌아갔는지)
 
        '''
        1 2 3 4 5       r>m>l
            
        5 (1) 2  3  4 : l>r>m -> l>m, 정렬 오른쪽
        4  5 (1) 2  3 : l>r>m -> l>m, 정렬 오른쪽
        3  4  5 (1) 2 : m>l>r -> m>l, 정렬 왼쪽
        2  3  4  5 (1): m>l>r -> m>l, 정렬 왼쪽
        '''        
        left = 0
        right = len(nums)-1

        
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target: return mid

            if nums[mid]>=nums[left]: # 왼쪽이 더 길다
                if target < nums[mid] and target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            
            else: # 오른쪽이 더 길다
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            

        return -1
