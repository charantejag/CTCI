class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(n-1):
            if n%(i+1) == 0 and s == s[0:i+1]*int(n/(i+1)):
                return True
        return False
                
        