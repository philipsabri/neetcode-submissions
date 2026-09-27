class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        right = len(nums1)-1

        # [1,2,2,3,5,6]
        #  ^
        # [2,5,6]
        #  ^

        while right >= 0:
            if j < 0 or (i >= 0 and nums1[i] > nums2[j]):
                nums1[right] = nums1[i]
                i -= 1
            else:
                nums1[right] = nums2[j]
                j -= 1
            right -= 1