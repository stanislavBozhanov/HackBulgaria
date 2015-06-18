"use strict";

var forEachDict = function(f, arr) {
  for( var key in arr) {
    f(arr[key], key, arr);
  }
};

var format = function(str, dict) {
  forEachDict(function(value, key) {
    var re = "{" + key + "}";
    str = str.replace(re, value);
  }, dict)
  return str;
};

var formatted = format("{lang} is a very wierd {thing}!", {
  "lang": "JavaScript",
  "thing": "language"
});

console.log(formatted);
