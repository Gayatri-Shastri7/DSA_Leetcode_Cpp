class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        r=[]
        if(n==1):
            return 
        for i in range(0,n-1):
            if(nums[i]==nums[i+1]):
                r.append(nums[i])
        return r
        # rs = []
        # for num in nums:
        #     num = abs(num)
        #     if nums[num-1] < 0:
        #         rs.append(num)
        #     else:
        #         nums[num-1] = -nums[num-1]
        # return rs
    
    # sort
    # 1 1 2
    # for i in range(0,n-1):
    #     r=[]
    #     ind[i] == ind[i+1]
    #     r.append(nums[i])
        
        