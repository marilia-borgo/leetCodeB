#https://leetcode.com/problems/remove-element/
# Input: nums =  [0,1,2,2,3,0,4,2]
#  val = 2
# Output: 5

nums = [0,1,2,2,3,0,4,2]
val = 2

indice = 0 
while indice < len(nums):
    if nums[indice] == val:
        nums.pop(indice)
        print(nums)
    else:
        print(nums)
        indice += 1
result = (len(nums)-1)+1
print(result)
#leet code retorna a função
# return result
