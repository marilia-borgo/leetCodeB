//https://leetcode.com/problems/single-number/
// Input: nums = [2,2,1]
// Output: 1

nums = [2,2,1]

let resultado = nums.reduce((acc, val) => {
    if (!acc[val]) acc[val] = {
      "número": val,
      "quantidade": 1
    };
    else acc[val]["quantidade"]++;
    return acc;
  }, {});
quantidadeNumeros = Object.values(resultado) 
for (let i = 0; i < quantidadeNumeros.length; i++) {
    if (quantidadeNumeros[i].quantidade === 1){
        console.log (quantidadeNumeros[i].número)
        //leetcode
        //return quantidadeNumeros[i].número
    }
} 