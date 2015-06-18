'use strict';

var fib = function(n) {
  if(n === 1 || n === 2) {
    return 1;
  }
  return fib(n-1) + fib(n-2);
};

console.log(fib(1));
console.log(fib(2));
console.log(fib(3));
console.log(fib(10));

