class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # changing all the str elements to int element
        for i in range(len(nums)):
            nums[i] = int(nums[i])

        #Sorting the array in reverse order
        nums.sort(reverse=True)

        #Returning the final result
        return str(nums[k-1])