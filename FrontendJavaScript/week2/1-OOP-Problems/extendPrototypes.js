"use strict";

String.prototype.capitalize = function() {
  return this.toUpperCase();
};

console.log("zoom".capitalize());

String.prototype.dasherize = function() {
  return this.replace(/_/g, "-");
};

console.log("border_bottom_width".dasherize());

String.prototype.times = function(amount) {
  var result = this;
  while(amount-1) {
    result += " " + this;
    amount -= 1;
  }
  return result;
};

console.log("bobi".times(5));

String.prototype.blank = function() {
  return this.replace(/ /g, "") === "";
};

console.log("".blank());
console.log("   ".blank());
console.log("  a".blank());

