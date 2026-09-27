class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        targetNew = 0

        for index, value in enumerate(nums):
            table[value] = index
#print(table)
        for i in range(len(nums)):
            targetNew = target - nums[i]
            if targetNew in table and table[targetNew] != i:
                return [i, table[targetNew]]
        
        return []

