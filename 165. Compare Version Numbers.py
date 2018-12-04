"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        """
        用split划分成多个部分
        首先，将共同的部分进行比较。越靠前面的部分大则大
        如果有共同部分都相同，看多出的部分，不全为0，长的大
        """
        version1_list = version1.split('.')
        version2_list = version2.split('.')

        version1_index = 0
        version2_index = 0
        while version1_index < len(version1_list) and version2_index < len(version2_list):
            if int(version1_list[version1_index]) > int(version2_list[version2_index]):
                return 1
            elif int(version1_list[version1_index]) < int(version2_list[version2_index]):
                return -1
            else:
                version1_index += 1
                version2_index += 1
        while version1_index < len(version1_list):
            if int(version1_list[version1_index]) != 0:
                return 1
            version1_index += 1
        while version2_index < len(version2_list):
            if int(version2_list[version2_index]) != 0:
                return -1
            version2_index += 1
        return 0
