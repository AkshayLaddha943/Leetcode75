class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new = [nums[0]]
        for i in range(1, len(nums)):
            new.append(new[-1] + nums[i])
        return new
