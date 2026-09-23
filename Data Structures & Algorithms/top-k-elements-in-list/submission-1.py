class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int);
        for num in nums:
            freqs[num] += 1
        
        arr = []
        for num, frq in freqs.items():
            arr.append([frq, num])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res