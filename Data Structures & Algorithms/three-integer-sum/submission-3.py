class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue

            i1 = i + 1
            i2 = len(nums) - 1
            while i1 < i2:
                threeSum = a + nums[i1] + nums[i2]
                if(threeSum > 0):
                    i2 -= 1
                elif(threeSum < 0):
                    i1 += 1
                else:
                    res.append([a, nums[i1], nums[i2]])
                    i1 += 1
                    i2 -= 1
                    while nums[i1] == nums[i1-1]and i1 < i2:
                        i1 += 1
        return res

            
