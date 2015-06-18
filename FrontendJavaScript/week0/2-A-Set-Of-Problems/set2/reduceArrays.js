"use strict";

var sum = function(arr) {
    return arr.reduce(function(acc, next) {
        return acc + next;
    }, 0);
};
console.log(sum);

var plus = function(a, b) {
  return a + b;
};

var minus = function(a, b) {
  return a - b;
};


var reduceFunc = function(oper, arr, start) {
    var result = start;
    arr.forEach(function(element) {
      result = oper(result, element);
    });
    return result;
  };

console.log(reduceFunc(plus, [1,2,3], 0));
console.log(reduceFunc(minus, [1,2,3], 0));
