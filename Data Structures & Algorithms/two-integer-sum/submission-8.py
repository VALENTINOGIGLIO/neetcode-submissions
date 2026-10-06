class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diz={}
        
        for i,n in enumerate(nums):
            c=target-n

            if c not in diz:
                diz[n]=i
            else:
                
                return [diz[c],i]
        return output