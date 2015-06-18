"use strict";

var forEachArray = function(f, arr) {
  var i = 0;
  var n = arr.length;
  for(i; i<n; i++) {
    f(arr[i], i, arr);
  }
};

var forEachDict = function(f, arr) {
  for( var key in arr) {
    f(arr[key], key, arr);
  }
};

var info = {
  "stenly": 23,
  "Rado": 24
};

forEachDict(function(value, key) {
  console.log(key, value);
}, info);
