"use strict";

var countVowels = function(str) {
  var vowels = "aeiouy".split("");
  var times = 0;
  str = str.toLowerCase();
  str = str.split("");
  str.forEach(function(letter) {
    if (vowels.indexOf(letter) != -1) {
      times += 1;
    }
  });
  return times;
};
exports.countVowels = countVowels;

// console.log(countVowels("JavaScript") === 3);
// console.log(countVowels("Theistareykjarbunga") === 8);
// console.log(countVowels("grrrrgh!") === 0);
// console.log(countVowels("Github is the second best thing that happend to programmers, after the keyboard!") === 22);
// console.log(countVowels("A nice day to code!") === 8);
