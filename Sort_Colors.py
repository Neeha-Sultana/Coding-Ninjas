"""
#Better
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]] += 1
            else:
                dict1[nums[i]] = 1
                
        for i in range(0, dict1.get(0, 0)):
            nums[i] = 0
            
        for i in range(dict1.get(0, 0), dict1.get(0, 0) + dict1.get(1, 0)):
            nums[i] = 1
            
        for i in range(dict1.get(0, 0) + dict1.get(1, 0), len(nums)):
            nums[i] = 2
            
"""
#Optimal
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low=0
        mid=0
        hi=len(nums)-1
        while (mid<=hi):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low=low+1
                mid=mid+1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[hi]=nums[hi],nums[mid]

                hi=hi-1
   
        return nums
