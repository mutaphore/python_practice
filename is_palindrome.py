#!/user/local/bin/python

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        temp = ""
        for c in s:
            if c.isalnum():
                temp += c
        s = temp.upper()
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.isPalindrome("")
