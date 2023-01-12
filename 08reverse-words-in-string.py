#https://leetcode.com/problems/reverse-words-in-a-string/description/
# Input: s = "the sky is blue"
# Output: "blue is sky the"

s = "  hello world  "

print(' '.join(i for i in reversed(s.split())))