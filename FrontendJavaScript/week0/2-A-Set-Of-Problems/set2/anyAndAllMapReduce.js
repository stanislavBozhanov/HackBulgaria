"use strict";

var reduceFunc = function(oper, arr, start) {
    var result = start;
    arr.forEach(function(element) {
      result = oper(result, element);
    });
    return result;
};

var map = function(f, arr) {
  var new_arr = [];
  var i = 0;
  var n = arr.length;
  for(i; i < n; i++) {
    new_arr.push(f(arr[i]));
  }
  return new_arr;
};

var bigData = function(x) {
  return x > 10;
};

var all = function(pred, arr) {
  var pred_arr = map(pred, arr);
  var result = reduceFunc(function(a, b) {
  return a && b;
  }, pred_arr, true);
  return result;
};

var any = function(pred, arr) {
  return reduceFunc(function(a, b) { return a && b; }, map(pred, arr), true);
};

console.log(any(bigData, [11,1,12,3]));
console.log(all(bigData, [11,11,12,3]));
