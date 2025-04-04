class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        I can simply count in dictionary and sort it but that would be nlogn time complexity so to make it o(N) i will use a bucket sort


        This bucket array of array will hold the frequncy of each element for example for the array [8,8,8,5,2,4,5] the items will be put as such [[], [2, 4], [5], [8], [], [], [], []] so each index represents the frequency of the elements in the bucket
        '''

        count = {}
        bucket = [[] for i in range(len(nums) + 1)]
        top_k_frequent = []
        

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for val, freq in count.items():
            bucket[freq].append(val)
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                if len(top_k_frequent) != k:
                    top_k_frequent.append(num)
                else:
                    break
        
        
        return top_k_frequent
            
        

        


        