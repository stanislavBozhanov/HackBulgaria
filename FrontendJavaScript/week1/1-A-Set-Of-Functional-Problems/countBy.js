"use strict";

var students = [{
  "name" : "Daniel Taskoff",
  "course" : "Frontend JavaScript"
}, {
  "name" : "Elena Jeleva",
  "course" : "Programming 101"
}, {
  "name" : "Luboslava Dimitrova",
  "course" : "Frontend JavaScript"
}, {
  "name" : "Anton Antonov",
  "course" : "Core Java"
}, {
  "name" : "Nikola Dichev",
  "course" : "Core Java"
}];


var countBy = function(countingFunction, arr) {
  var result = {};
  arr.forEach(function(element) {
    var key = countingFunction(element);
    if(!result[key]) {
      result[key] = 0;
    }
    result[key] += 1;
  });
  return result;
};

console.log(countBy(function(student) {
  return student.course;
}, students));
