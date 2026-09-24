class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        maxArea = -1
        while l < r:
            smaller_height = min(heights[l], heights[r])
            area = (r-l) * smaller_height
            if area > maxArea:
                maxArea = area

            if smaller_height == heights[l]:
                l += 1
            else:
                r -= 1
        return maxArea
