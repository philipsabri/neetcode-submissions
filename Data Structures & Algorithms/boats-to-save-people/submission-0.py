class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1, 3, 2, 3, 2
        # 1, 2, 2, 3, 3
        
        res = 0
        left = 0
        right = len(people)-1
        people.sort()
        
        while left <= right:                
            if left == right or people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            res += 1
        return res