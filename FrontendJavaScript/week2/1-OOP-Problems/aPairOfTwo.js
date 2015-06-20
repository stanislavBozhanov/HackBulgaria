"use strict";

function Pair(left, right) {
  this.left = left;
  this.right = right;
}

Pair.prototype.equals = function(pair) {
  return pair.left === pair.right;
};

Pair.prototype.toString = function(pair) {
  return "(" + pair.left + ", " + pair.right + ")";
};

Pair.prototype.toList = function(pair) {
  var result = [];
  result.push(pair.left);
  result.push(pair.right);
  return result;
};

Pair.prototype.combine = function(f) {
  return f(this.left, this.right);
};

var p = new Pair(4, 6);
var combined = p.combine(function(left, right){
  return right + left;
});

console.log(combined);
