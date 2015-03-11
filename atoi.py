#!/user/local/bin/python

# Implement atoi to convert a string to an integer.
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front. 

import string

class Solution:
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    # @return an integer
    def atoi(self, str_):
        s = str_.lstrip().split(" ")[0]
        init = False
        int_s = ""
        sign = "+"
        i = 0
        if i < len(s) and (s[i] in string.digits or s[i] in "-+"):
            if s[i] == "-":
                sign = "-"
                i += 1
            elif s[i] == "+":
                i += 1
            while i < len(s) and s[i] in string.digits:
                int_s += s[i]
                i += 1
        if int_s:
            return max(Solution.INT_MIN, min(Solution.INT_MAX, int(sign + int_s)))
        return 0


if __name__ == "__main__":
    sol = Solution()
    print sol.atoi("")
    # print sol.atoi(" .--+++sdf012.301sdfasdj2")
    # print sol.atoi(" +0 123")

