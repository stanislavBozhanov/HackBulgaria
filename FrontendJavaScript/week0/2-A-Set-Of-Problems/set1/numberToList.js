"use strict";

var numberToList = function(n) {
  var arr = n.toString().split("");
  function returnInt(element) {
    return parseInt(element, 10);
  }
  return arr.map(returnInt);
};

var result1 = numberToList(123);
var result2 = numberToList(99999);
var result3 = numberToList(123023);

console.log((result1.length == [1, 2, 3].length) && result1.every(function(element, index) {
    return element === [1, 2, 3][index];
}));
console.log((result2.length == [ 9, 9, 9, 9, 9 ].length) && result2.every(function(element, index) {
    return element === [ 9, 9, 9, 9, 9 ][index];
}));
console.log((result3.length == [ 1, 2, 3, 0, 2, 3 ].length) && result3.every(function(element, index) {
    return element === [ 1, 2, 3, 0, 2, 3 ][index];
}));
