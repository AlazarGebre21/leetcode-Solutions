class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #function to calculate the gap
        def difference(n):
            return abs(target - (n))


        #sorting the function because we are going to use two pointer from the left and from the right after fixing the first
        nums.sort()
        

        # fixing i and moving like the 2 sum from the right and left
        closet_sum = nums[0] + nums[1] + nums[-1]
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                closet_sum = min(current_sum,closet_sum, key=difference)
                if current_sum > target:
                    k -= 1
                elif current_sum < target:
                    j += 1
                elif current_sum == target:
                    closet_sum = current_sum
                    break
        return closet_sum

