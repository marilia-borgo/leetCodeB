let nums = [2,7,11,15]
let target = 9 

const map = {}
for (let index = 0; index < nums.length; index++) {
  const element = nums[index]
  const complement = target - element
  if (map[complement] !== undefined) {
    console.log ( [map[complement], index])
    //leetcode
    // return [map[complement], index]
  } else {
    map[element] = index
  }
}
return []
