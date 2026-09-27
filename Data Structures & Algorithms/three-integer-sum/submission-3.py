class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            while left < right:
                num = nums[i] + nums[left] + nums[right]
                if num == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif num > 0:
                    right -= 1
                else:
                    left += 1
        return res