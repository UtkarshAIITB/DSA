nums = [2,7,11,15]
hashmap = {}
for i in range(len(nums)):
	hashmap[nums[i]] = i
print(hashmap)    #outputs {2: 0, 7: 1, 11: 2, 15: 3}
print(hashmap[2]) #outputs 0


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement]!=i:
                return [i, hashmap[complement]]

# time complexity = O(n)