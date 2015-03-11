#!/user/local/bin/python

# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# Here is an example of version numbers ordering:
# 0.1 < 1.1 < 1.2 < 13.37

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        if len(v1) > len(v2):
            v2.extend([0] * (len(v1) - len(v2)))
        elif len(v1) < len(v2):
            v1.extend([0] * (len(v2) - len(v1)))
        index = 0
        while index < len(v1):
            if v1[index] == v2[index]:
                index += 1
            elif v1[index] > v2[index]:
                return 1
            else:
                return -1
        return 0


if __name__ == "__main__":
    sol = Solution()
    print sol.compareVersion("01", "1")
