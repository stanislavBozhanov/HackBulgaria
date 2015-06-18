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

var groupBy = function(groupingFunction, arr) {
  var result = {};
  arr.forEach(function(element){
    var key = groupingFunction(element);
    if (!result[key]) {
      result[key] = [];
    }
    result[key].push(element);
  });
  return result;
};

console.log(groupBy(function(student) {
  return student.course;
}, students));
