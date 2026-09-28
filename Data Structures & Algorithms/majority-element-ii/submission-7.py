class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        current_one = current_two = count_one = count_two = 0

        for num in nums:
            if num == current_one:
                count_one += 1
            elif num == current_two:
                count_two += 1
            elif count_one == 0:
                current_one = num
                count_one = 1
            elif count_two == 0:
                current_two = num
                count_two = 1
            else:
                count_one -= 1
                count_two -= 1

        count_one = count_two = 0
        for num in nums:
            if num == current_one:
                count_one += 1
            elif num == current_two:
                count_two += 1
        
        res = []
        if count_one > len(nums)/3:
            res.append(current_one)
        if count_two > len(nums)/3:
            res.append(current_two)

        return res