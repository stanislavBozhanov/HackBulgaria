"use strict";

var isDecreasing = function(seq) {
  return seq.every(function(element, index) {
    if (index+1 === seq.length) {
      return true;
    }
    return seq[index] > seq[index+1];
  });
};

console.log(isDecreasing([5,4,3,2,1]) === true);
console.log(isDecreasing([1,2,3]) === false);
console.log(isDecreasing([100, 50, 20]) === true);
console.log(isDecreasing([1,1,1,1]) === false);
