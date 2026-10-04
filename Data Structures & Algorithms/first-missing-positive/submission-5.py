class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            while num:
                if num > 0 and num <= len(nums) and num != nums[num-1]:
                    next_num = nums[num-1]
                    nums[num-1] = num
                    num = next_num
                else:
                    num = None
        res = 0
        print(nums)

        for i in range(len(nums)):
            if i != nums[i]-1:
                return i+1

        return len(nums)+1
