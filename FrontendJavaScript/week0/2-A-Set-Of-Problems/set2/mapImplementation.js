"use strict";

var map = function(f, arr) {
  var new_arr = [];
  var i = 0;
  var n = arr.length;
  for(i; i < n; i++) {
    new_arr.push(f(arr[i]));
  }
  return new_arr;
};

var result = map(function(x) {
  return x * x;
}, [1, 2, 3]);
console.log(result);
