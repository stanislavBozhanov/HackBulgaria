'use strict';

var isPrime = function(n) {
  if (n <= 1) {
    return false;
  }
  var end = Math.floor(Math.sqrt(n));
  var i = 2;
  var result = true;
  for (i; i<=end; i++) {
    if (n % i === 0) {
      result = false;
    }
  }
  return result;
};

exports.isPrime = isPrime;

// console.log(isPrime(1) === false);
// console.log(isPrime(2) === true);
// console.log(isPrime(8) === false);
// console.log(isPrime(11) === true);
// console.log(isPrime(-10) === false);
