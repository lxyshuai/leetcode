# coding=utf-8
"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.
"""


class Solutions(object):
    def canWin(self, string):
        if string is None or len(string) <= 1:
            return False

        for i, j in zip(range(0, len(string) - 1), range(1, len(string))):
            if string[i] == string[j] == '+':
                next_string = string[:i] + '--' + string[j + 1:]
                # 如果要赢不仅要自己能动，要保证下一步不能动
                if not self.canWin(next_string):
                    return True
        return False
