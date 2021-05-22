##Runtime: 584 ms, faster than 87.51% of Python online submissions for Container With Most Water.
##Memory Usage: 23.9 MB, less than 81.15% of Python online submissions for Container With Most Water.
def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxi = 0
        while left<right:
            w = right - left
            h = 0
            if height[left]<height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            temp = w*h
            if temp>maxi:
                maxi = temp
        return maxi
            
                
        

print(maxArea([1,8,6,2,5,4,8,3,7]))
