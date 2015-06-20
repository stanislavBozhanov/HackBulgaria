"use strict";

function Shape(type) {
  this.getType = function() {
    return type;
  };
}

Shape.prototype.area = function() {
  throw new Error("Cannot call area of Shape. Use subclasses!");
};

function Rectangle(type, width, height) {
  Shape.call(this, type);
  this.width = width;
  this.height = height;
}

Rectangle.prototype = Object.create(Shape.prototype);
Rectangle.prototype.constructor = Rectangle;

Rectangle.prototype.area = function() {
  return this.width * this.height;
};

function Triangle(type, altitude, side) {
  Shape.call(this, type);
  this.altitude = altitude;
  this.side = side;
}

Triangle.prototype = Object.create(Shape.prototype);
Triangle.prototype.constructor = Triangle;

Triangle.prototype.area = function() {
  return (this.altitude * this.side) / 2;
};

function Circle(type, radius) {
  Shape.call(this, type);
  this.radius = radius;
}

Circle.prototype = Object.create(Shape.prototype);
Circle.prototype.constructor = Circle;

Circle.prototype.area = function() {
  return 2 * this.radius * 3.14;
};
