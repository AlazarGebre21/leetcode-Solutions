class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #creating hashtable to store the elements in the array
        length = len(nums)
        hash_table = [0] * (length + 1)

        #storing the values int the hashmap using the values the nums as the index
        for i in range(length):
            hash_table[nums[i]] += 1

        #iterating through the hashmap and if we got any zero the index is the missing number
        length1 = len(hash_table)
        for i in range(length1):
            if hash_table[i] == 0:
                return i
            else:
                continue
        
        
