class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberCount = {}
        for num in nums:
            numberCount[num] = numberCount.get(num, 0) + 1
        
        heap = []
        for key, value in numberCount.items():
            heap.append((-value, key))
        
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            value, key = heapq.heappop(heap)
            res.append(key)
        return res