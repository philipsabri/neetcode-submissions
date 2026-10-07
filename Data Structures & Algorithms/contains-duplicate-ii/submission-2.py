class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numIndex = {} 
        for i in range(len(nums)):
            num = nums[i]
            if num in numIndex and abs(i - numIndex[num]) <= k:
                return True
            numIndex[num] = i
        return False