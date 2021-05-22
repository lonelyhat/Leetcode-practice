def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    mapping = dict()
    for i in range(len(nums)):
        if target-nums[i] in mapping:
            return [mapping[target-nums[i]],i]
        else:
            mapping[nums[i]]=i
print(twoSum([2,7,11,15],9))
