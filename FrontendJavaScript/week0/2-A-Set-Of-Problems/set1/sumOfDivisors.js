'use strict';

var sumOfDivisors = function(n){
  var sum = 0;
  var i = n;
  for(i; i>0; i--) {
    if (n % i === 0) {
      sum += i;
    }
  }
  return sum;
};

console.log(sumOfDivisors(8) === 15);
console.log(sumOfDivisors(7) === 8);
console.log(sumOfDivisors(1) === 1);
console.log(sumOfDivisors(1000) === 2340);
