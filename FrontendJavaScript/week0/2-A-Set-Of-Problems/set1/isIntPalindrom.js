'use strict';

var isIntPalindrom = function(n) {
  var arr = [];
  while(n > 0) {
    var element = n % 10;
    arr.push(element);
    n = Math.floor(n / 10);
  }
  for(var i = 0; i < arr.length - 1 - i; i++) {
    if (arr[i] != arr[arr.length - 1 - i]) {
      return false;
    }
  }
  return true;
};

console.log(isIntPalindrom(1) === true);
console.log(isIntPalindrom(42) === false);
console.log(isIntPalindrom(100001) === true);
console.log(isIntPalindrom(999) === true);
console.log(isIntPalindrom(123) === false);
