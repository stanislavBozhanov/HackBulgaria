'use strict';

var sumOfMinAndMax = function(arr) {
  arr = arr.sort(function(a, b) {return a-b;});
  var sum = arr[0] + arr[arr.length - 1];
  return sum;
};

console.log(sumOfMinAndMax([1,2,3,4,5,6,8,9]) === 10);
console.log(sumOfMinAndMax([-10,5,10,100]) === 90);
console.log(sumOfMinAndMax([1]) === 2);
