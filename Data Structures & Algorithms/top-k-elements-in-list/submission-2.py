class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {} # Dictionary num:count
        freq = [[] for i in range(len(nums) + 1)] 
        # list of lists ind = count, list = num

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, cnt in counts.items():
            freq[cnt].append(num)

        #freq is in order of count/k appearances in ascending order
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


        
