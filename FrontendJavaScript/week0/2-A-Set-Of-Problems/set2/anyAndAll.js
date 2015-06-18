"use strict";

var any = function(pred, arr) {
  var i = 0, n = arr.length;
  while(i < n) {
    if (pred(arr[i])) {
      return true;
    }
    i++;
  }
  return false;
};

var all = function(pred, arr) {
  var i = 0, n = arr.length;
  while(i < n) {
    if (!pred(arr[i])) {
      return false;
    }
    i++;
  }
  return true;
};

var bigData = function(x) {
  return x > 10;
};

console.log(any(bigData, [11,1,12,3]));
console.log(all(bigData, [11,1,12,3]));
