"use strict";

var listToNumber = function(arr) {
  var str_arr = arr.map(function(num) {
    return num.toString();
  });
  str_arr = str_arr.join("");
  return parseInt(str_arr);
};

console.log(listToNumber([1,2,3]) === 123);
console.log(listToNumber([9,9,9,9,9]) === 99999);
console.log(listToNumber([1,2,3,0,2,3]) === 123023);
