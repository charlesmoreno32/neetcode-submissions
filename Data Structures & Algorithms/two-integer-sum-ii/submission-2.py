class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_to_ind = {}
        for i, num in enumerate(numbers):
            complement = target - num

            if complement in num_to_ind:
                return [num_to_ind[complement] + 1, i + 1]

            num_to_ind[num] = i
        
