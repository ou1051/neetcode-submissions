class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for i in range(len(nums)):
            for j in range(len(nums)):
                goal = 7 - nums[i]
                hash_map[nums[i]] = goal
                if hash_map[j] != goal:
                    return False
                return True
        
        

