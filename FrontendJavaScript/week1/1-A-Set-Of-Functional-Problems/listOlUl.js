"use strict";

var items = [{ "label" : "Item 1"}, { "label" : "Item 2"}, , { "label" : "Item 3"}];

var ol = function(items) {
  var result = "<ol>";
  var new_line = "\n";
  items.forEach(function(element) {
    result = result.concat(new_line);
    result = result.concat("<li>" + element["label"] + "</li>");
  });
  result = result.concat("\n</ol>");
  return result;
};

console.log(ol(items));
