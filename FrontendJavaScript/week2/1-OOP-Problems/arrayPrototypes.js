"use strict";

Array.prototype.first = function() {
  if (this.length === 0) {
    throw new RangeError("index doesn't exist");
  }
  return this[0];
};

console.log([1, 2].first());

Array.prototype.range = function(from, to) {
  var result = [];
  while(from <= to) {
    result.push(from);
    from++;
  }
  return result;
};

console.log([].range(1, 10));

Array.prototype.sum = function() {
  var sum = 0;
  this.forEach(function(element) {
    sum += element;
  });
  return sum;
};

console.log([1, 2, 3].sum());

Array.prototype.average = function() {
  return this.sum() / this.length;
};

console.log([1, 2, 3].average());
