# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for each item in the list, if not in set, add to set, else return true
        encountered = set()
        for item in nums:
            if item in encountered:
                return True
            else:
                encountered.add(item)
                
        return False