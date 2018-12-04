"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip twoconsecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]


If there is no valid move, return an empty list [].
"""


class Solution(object):
    def generatePossibleNextMoves(self, string):
        result = []
        if string is None or len(string) <= 1:
            return result

        for i, j in zip(range(0, len(string) - 1), range(1, len(string))):
            if string[i] == string[j] == '+':
                result.append(string[:i] + '--' + string[j + 1:])
        return result


if __name__ == '__main__':
    print Solution().generatePossibleNextMoves('++++')
