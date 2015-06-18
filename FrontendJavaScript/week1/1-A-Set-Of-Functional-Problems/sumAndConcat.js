"use strict";

var sum = function(a, b) {
  if (typeof a != "number" || typeof b != "number") {
    throw new TypeError("Something is wrong with the types.");
  }
  return a + b;
};

console.log(sum(1, 2));
console.log(sum("as", 2));
