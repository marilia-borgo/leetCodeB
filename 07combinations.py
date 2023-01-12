# https://leetcode.com/problems/combinations/description/
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

#algoritmo backtracking: https://pt.wikipedia.org/wiki/Backtracking

result = []
n = 4 
k = 2
def backTrack(array, current_number):
    if (len(array) == k):
        result.append(array.copy())
        return
    
    for start in range (current_number, n+1):
        array.append (start)
        backTrack(array, start+1)
        array.pop()

backTrack([],1)
print(result)
# leetcode
# return result
