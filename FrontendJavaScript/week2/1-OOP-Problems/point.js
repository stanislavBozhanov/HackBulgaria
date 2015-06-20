"use strict";

function Point(x, y) {
  var _x = x;
  var _y = y;

  this.xinc = function() {
    _x += 1;
    return _x;
  };
  this.xdex = function() {
    _x -= 1;
    return _x;
  };
  this.yinc = function() {
    _y += 1;
    return _y;
  };
  this.ydec = function() {
    _y += 1;
    return _y;
  };
  this.getX = function() {
    return _x;
  };
  this.getY = function() {
    return _y;
  };
}

Point.prototype.equals = function(point) {
  return this.getX() === point.getX() && this.getY() === point.getY();
};

Point.prototype.toString = function () {
  return ["Point @ {", this.getX(), "}, {", this.getY(), "}"].join("");
};

exports.Point = Point;
