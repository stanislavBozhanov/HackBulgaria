'use strict';

var isNumberBalanced = function(n) {
  n = n.toString();
  var left_sum = 0;
  var right_sum = 0;
  for (var i = 0; i < n.length - 1 - i; i++) {
    left_sum += parseInt(n[i]);
    right_sum += parseInt(n[n.length - 1- i]);
  }
  if (left_sum === right_sum) {
    return true;
  }
  return false;
};

console.log(isNumberBalanced(9) === true);
console.log(isNumberBalanced(11) === true);
console.log(isNumberBalanced(13) === false);
console.log(isNumberBalanced(121) === true);
console.log(isNumberBalanced(4518) === true);
console.log(isNumberBalanced(28471) === false);
console.log(isNumberBalanced(1238033) === true);
