class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(t):
            return False
            
        return sorted(s) == sorted(t)