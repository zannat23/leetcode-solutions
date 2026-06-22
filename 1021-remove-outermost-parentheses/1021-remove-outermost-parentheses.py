class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        ans = ""

        for ch in s:
            if ch == '(':
                if count > 0:
                    ans += ch
                count += 1
            else:
                count -= 1
                if count > 0:
                    ans += ch

        return ans