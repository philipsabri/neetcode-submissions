class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original = {}
        for char in s1:
            original[char] = original.get(char, 0) + 1
        
        res = {}
        left = 0
        for right in range(len(s2)):
            charRight = s2[right]
            res[charRight] = res.get(charRight, 0 ) + 1

            charLeft = s2[left]
            if right-left == len(s1):
                res[charLeft] -= 1
                if res[charLeft] == 0:
                    del res[charLeft]
                left += 1

            if res == original:
                return True

        return False

