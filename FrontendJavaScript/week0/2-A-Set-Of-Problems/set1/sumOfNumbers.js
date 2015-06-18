'use strict';

var sumOfDigits = function(num) {
  var result = 0;
  if (num < 0) {
    num *= -1;
  }
  while(num > 0) {
    var digit = num % 10;
    num = Math.floor(num / 10);
    result += digit;
  }
  return result;
};

console.log(sumOfDigits(1325132435356) === 43);
console.log(sumOfDigits(123) === 6);
console.log(sumOfDigits(6) === 6);
console.log(sumOfDigits(-10) === 1);
