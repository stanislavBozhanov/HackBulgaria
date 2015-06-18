"use strict";

var only = function(type, arr) {
  var result = true;
  arr.forEach(function(element) {
    if(typeof element != type) {
      result = false;
    }
  });
  return result;
};

console.log(only("string", [1,2,3,4]));
console.log(only("number", [1,2, 3,4]));
