#!/usr/local/bin

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
    	if numRows == 0:
    		return []
    	if numRows == 1:
    		return [[1],]
    	if numRows == 2:
    		return [[1], [1, 1]]
    	pascal = [[1], [1, 1]] 
    	for row in range(1, numRows - 1):
    		level = [1]
    		for i in range(len(pascal[row]) - 1):
    			level.append(pascal[row][i] + pascal[row][i + 1])
    		level.append(1)
    		pascal.append(level)
    	return pascal


if __name__ == "__main__":
	sol = Solution()
	print sol.generate(5)