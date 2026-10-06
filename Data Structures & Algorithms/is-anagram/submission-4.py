class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        for l in s:
            dic1[l]=dic1.get(l,0) +1
        for l in t:
            dic2[l]=dic2.get(l,0) +1

        if dic1==dic2:
            return True
        else:
            return False