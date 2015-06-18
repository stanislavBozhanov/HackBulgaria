'use strict';

var primeNumberOfDivisors = function(n) {
  var isPrime = require('./isPrime').isPrime;
  var number = 0;
  var i = n;
  for(i; i>0; i--) {
    if (n % i === 0) {
      number += 1;
    }
  }
  return isPrime(number);
};

console.log(primeNumberOfDivisors(7) === true);
console.log(primeNumberOfDivisors(8) === false);
console.log(primeNumberOfDivisors(9) === true);
