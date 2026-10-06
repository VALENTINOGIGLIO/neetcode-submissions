class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diz={}
        output=[]
        for i,n in enumerate(nums):
            c=target-n

            if c not in diz:
                diz[n]=i
            else:
                
                output.append(diz[c])
                output.append(i)
        return output