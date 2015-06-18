"use strict";


var countConsonants = function(str) {
  var new_str = str.toLowerCase();
  var countVowels = require("./countVowels").countVowels;
  new_str = new_str.replace(/\W+/g, "");
  new_str = new_str.replace(/\s/g, "");
  return new_str.length - countVowels(new_str);
};

console.log(countConsonants("JavaScript") === 7);
console.log(countConsonants("Theistareykjarbunga") === 11);
console.log(countConsonants("grrrrgh!") === 7);
console.log(countConsonants("Github is the second best thing that happend to programmers, after the keyboard!") === 44);
console.log(countConsonants("A nice day to code!") === 6);
