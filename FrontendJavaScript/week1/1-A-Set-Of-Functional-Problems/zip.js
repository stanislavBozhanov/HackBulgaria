"use strict";

var zip = function() {
  var args = [].slice.call(arguments);
  var shortest = args.length===0 ? [] : args.reduce(function(a,b){
    return a.length<b.length ? a : b;
  });

  return shortest.map(function(_,i){
    return args.map(function(array){
      return array[i];
    });
  });
};

console.log(zip([1, 2, 3], [4, 5, 6]));
