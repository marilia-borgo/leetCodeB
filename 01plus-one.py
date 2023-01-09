#https://leetcode.com/problems/plus-one/
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

digits = [4,3,2,1]
constroi_string='0'
for element in digits:
    entrada_to_string = str(element)
    constroi_string = constroi_string + entrada_to_string
resultado_string = int(constroi_string) + 1 
resultado_lista = list(str(resultado_string))
resultado_final = [int(x) for x in resultado_lista]
# no leet code tem que retornar a função
# return [int(x) for x in resultado_lista]
print(resultado_final)


    



