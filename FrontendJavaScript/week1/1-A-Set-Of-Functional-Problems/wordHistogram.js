"use strict";

var str = "A function is a function with a very functional function!";

var wordHistogram = function(str) {
  str = str.replace(/[\W_ ]+/g, " ").toLowerCase().split(" ");
  var filtered = str.filter(function(word) {
    return word.trim() !== "";
  });
  var result = {};
  filtered.forEach(function(word) {
    if (!result[word]) {
      result[word] = 0;
    }
    result[word] += 1;
  });
  return result;
};

console.log(wordHistogram((str)));
