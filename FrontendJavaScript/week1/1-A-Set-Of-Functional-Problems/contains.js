"use strict";

var contains = function(element, arr) {
  return arr.some(function(x) {
    return x === element;
  });
};

console.log(contains("d", ["a", "b", "c"]));
console.log(contains("b", ["a", "b", "c"]));
