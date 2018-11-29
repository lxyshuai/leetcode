"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def process(candidates, target, current_index, path):
            if target == 0:
                path.sort()
                if path not in result:
                    result.append(path)
                return
            if target < 0:
                return
            for index in range(current_index, len(candidates)):
                process(candidates, target - candidates[index], index + 1, path + [candidates[index]])

        result = []
        process(candidates, target, 0, [])
        return result


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def process(candidates, target, current_index, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for index in range(current_index, len(candidates)):
                if index != current_index and candidates[index] == candidates[index - 1]:
                    continue
                process(candidates, target - candidates[index], index + 1, path + [candidates[index]])

        result = []
        candidates.sort()
        process(candidates, target, 0, [])
        return result
