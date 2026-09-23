class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i1, i2 = 0, 1
        max_area = 0
        while i1 < i2:
            i2 = i1 + 1
            while i2 < len(heights):
                height = min(heights[i1], heights[i2])
                curr_area = height * (i2 - i1)
                if curr_area > max_area:
                    max_area = curr_area
                i2 +=1
            i1 += 1
        
        return max_area
            
        

        