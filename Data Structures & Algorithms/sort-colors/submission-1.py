class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for color in nums:
            count[color] += 1

        current_color = 0
        for i in range(len(nums)):
            while count[current_color] == 0:
                current_color += 1
            nums[i] = current_color
            count[current_color] -= 1