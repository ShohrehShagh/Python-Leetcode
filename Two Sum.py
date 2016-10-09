class Solution(object):
    def twoSum(self, nums, target):
        map=dict();
        for i in range (len(nums)):
            if target-nums[i] in map:
                return [map[target-nums[i]],i]
            else:
                map[nums[i]]=i;
        return []
        
