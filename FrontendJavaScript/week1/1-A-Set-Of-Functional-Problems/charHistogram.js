"use strict";

var str = "Count the characters in this very profound sentence";

var wordHistogram = function(str) {
  var chars = str.replace(/[\W_ ]+/g, " ").toLowerCase().split("");
  var filtered_chars = chars.filter(function(char_) {
    return char_.trim() !== "";
  });
  var result = {};
  filtered_chars.forEach(function(char_) {
    if (!result[char_]) {
      result[char_] = 0;
    }
    result[char_] += 1;
  });
  return result;
};

console.log(wordHistogram((str)));
