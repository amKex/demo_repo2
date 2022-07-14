
"""Running sum of a arrey e.g---> input:[1,2,5,4,3] output:[1,3,8,12,15]"""
def runningSum(self, nums: List[int]) -> List[int]:
    # for i in range(1, len(nums)):
    #     nums[i] = nums[i] + nums[i - 1]
    # return nums
        
    #sumlist = [nums[0]]
    for i in range(1,len(nums)):
        #sumlist.append(nums[i])
        nums[i] = nums[i - 1] + nums[i]
    return nums

print(runningSum([1,2,5,4,3]))
