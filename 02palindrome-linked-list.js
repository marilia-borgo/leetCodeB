// https://leetcode.com/problems/palindrome-linked-list/
// Input: head = [1,2,2,1]
// Output: true
// Input: head = [1,2]
// Output: false


//Essa era a minh solução original, mas o leet code inicia como
//linked list não como array, logo deu errado.


// let head = [1,2]
// let listaRevertida = head.map((x) => x); 
// let resposta = listaRevertida.reverse()
// if (resposta.every((value, index) => value === head[index])){
//     return true
// }
// return false


//solução pro linked list que ta no leet code
var isPalindrome = function(head) {
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
    }
    let prev = null;
    let curr = slow;
    while (curr) {
      let next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
    }
    let p1 = head;  
    let p2 = prev;
    while (p2) {
      if (p1.val !== p2.val) return false;
      p1 = p1.next;
      p2 = p2.next;
    }
    return true;
  }