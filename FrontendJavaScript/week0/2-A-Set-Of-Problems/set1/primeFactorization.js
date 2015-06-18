'use strict';

var isPrime = require('./isPrime').isPrime;

var primeFactorization = function(n) {
  var result = [];
  for(var i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
    var counter = 0;
    while(isPrime(i) && n % i === 0) {
      counter += 1;
      n = Math.floor(n / i);
    }
    if (counter) {
      result.push([i, counter]);
    }
  }
  return result;
};

console.log(primeFactorization(18));
