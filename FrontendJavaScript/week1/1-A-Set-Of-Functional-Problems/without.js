"use strict";

var without = function(exclude, arr) {
  return arr.filter(function(arr_el) {
    return !(exclude.some(function(excl_el) {
      return excl_el === arr_el;
    }));
  });
};

console.log(without([5,6], [1,2,3,4,5,6]));
