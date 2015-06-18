"use strict";

var users = [{
    "name" : "Rado",
    "score" : 50
}, {
    "name" : "Ivan",
    "score" : 67
}, {
    "name" : "Vlado",
    "score" : 30
}];

var filter = function(f, arr) {
  var new_arr = [];
  for (var index in arr) {
    if(f(arr[index])) {
      new_arr.push(arr[index]);
    }
  }
  return new_arr;
};

var result = filter(function(user) {
    return user.score > 40;
}, users);

console.log(result);
