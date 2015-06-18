"use strict";

var isIncreasing = function(seq) {
  return seq.every(function(element, index) {
    if (index+1 === seq.length) {
      return true;
    }
    return seq[index] < seq[index+1];
  });
};

console.log(isIncreasing([1,2,3,4,5]) === true);
console.log(isIncreasing([1]) === true);
console.log(isIncreasing([5,6,-10]) === false);
console.log(isIncreasing([1,1,1,1]) === false);
