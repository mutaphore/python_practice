#!/usr/local/bin/python

# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 

import math
class Solution:
    # @return a string
    def convertToTitle(self, num):
        """Complicated way"""
        alpha = [chr(65 + x) for x in range(26)]
        digits = max(1, int(math.ceil(math.log(num, 26))))
        places = [-1] * digits
        clock = [0] + [1] * (digits - 1)
        for i in range(1, num + 1):
            for d in range(digits):
                if i > clock[d] * 26**d:
                    clock[d] += 1
                    places[d] = (places[d] + 1) % 26
        output = [alpha[p] for p in places]
        return "".join(output[::-1])


    def convertToTitle2(self, num):
        

if __name__ == "__main__":
    sol = Solution()
    print sol.convertToTitle(1000)
    print sol.convertToTitle2(1000)

