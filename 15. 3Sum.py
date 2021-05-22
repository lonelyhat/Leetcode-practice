##Runtime: 6236 ms, faster than 5.01% of Python online submissions for 3Sum.
##Memory Usage: 17.8 MB, less than 13.09% of Python online submissions for 3Sum.
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    output = []
    for i in range(len(nums)):
        target = 0-nums[i]
        mapping = dict()
        for j in range(i+1,len(nums)):
            if target - nums[j] in mapping:
                answer = sorted([nums[i],target - nums[j],nums[j]])
                if answer not in output:
                    output.append(answer)
            else:
                mapping[nums[j]]=j
    return output

print(threeSum([-1,0,1,2,-1,-4]))
                
            
