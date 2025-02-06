class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        even_sum = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_sum += nums[i]
            
        for i in range(len(queries)):
            catch = nums[queries[i][1]]
            nums[queries[i][1]] = nums[queries[i][1]] + queries[i][0]
            if catch % 2 != 0 and nums[queries[i][1]] % 2 == 0:
                even_sum += nums[queries[i][1]]
            elif catch % 2 == 0 and nums[queries[i][1]] % 2 != 0:
                even_sum -= catch
            elif catch % 2 == 0 and nums[queries[i][1]] % 2 == 0:
                even_sum += nums[queries[i][1]] - catch
            answer.append(even_sum)
        return answer
