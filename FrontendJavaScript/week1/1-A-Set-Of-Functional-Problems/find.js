"use strict";

var find = function(predicate, arr) {
  if (arr.length === 0) {
    return;
  }
  if (predicate(arr[0])) {
    return arr[0];
  }
  return find(predicate, arr.slice(1));
};

var func = function(element) {
  return element > 5;
};

var my_arr = [1, 2, 2, 4, 3, 2, 1 , 1];

console.log(find(func, my_arr));
