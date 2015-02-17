#!/usr/local/bin/python

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        slopes = {}
        for point in points:
            if point.x == 0:
                slope = float("inf")
            else:
                slope = point.y / point.x
            slopes[str(slope)] = slopes.get(str(slope), 0) + 1
        return max([v for k, v in slopes.iteritems()])
            
