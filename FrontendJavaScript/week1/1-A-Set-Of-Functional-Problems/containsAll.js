"use strict";

var contains = function(element, arr) {
  return arr.some(function(x) {
    return x === element;
  });
};

var containsAll = function(elements, arr) {
  return elements.every(function(element) {
    return contains(element, arr);
  });
};

console.log(containsAll([1, 2, 3], [2, 3, 4, 5, 4, 1, 5]));
