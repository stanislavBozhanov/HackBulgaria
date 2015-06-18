"use strict";

var countSubstrings = function(haystack, needle) {
  var times = 0;
  for(var i = 0; i < haystack.length - needle.length + 1; i++) {
    if (haystack[i] === needle[0]) {
      var match = true;
      for (var j = 0; j < needle.length; j++) {
        if (haystack[i+j] != needle[j]) {
          match = false;
          break;
        }
      }
      if (match) {
        times += 1;
        i += needle.length-1;
      }
    }
  }
  return times;
};

console.log(countSubstrings("This is a test string", "is") === 2);
console.log(countSubstrings("babababa", "baba") === 2);
console.log(countSubstrings("JavaScript is an awesome language to program in!", "o") === 3);
console.log(countSubstrings("We have nothing in common!", "really?") === 0);
console.log(countSubstrings("This is this and that is this", "this")  === 2);
