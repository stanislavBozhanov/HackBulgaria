"use strict";

var Point = require("./point").Point;

function Robot(point) {
  var startPoint = {
    "x": point.getX(),
    "y": point.getY()
  };

  this.moveLeft = function(amount) {
    startPoint.x -= amount;
    return startPoint;
  };
  this.moveRight = function(amount) {
    startPoint.x += amount;
    return startPoint;
  };
  this.moveUp = function(amount) {
    startPoint.y -= amount;
    return startPoint;
  };
  this.moveDown = function(amount) {
    startPoint.y += amount;
    return startPoint;
  };
  this.getPosition = function() {
    return startPoint;
  };
}
