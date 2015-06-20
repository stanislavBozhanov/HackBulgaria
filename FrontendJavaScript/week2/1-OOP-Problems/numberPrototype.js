"use strict";

Number.prototype.times = function(action) {
  for (var i=0; i<5; i++) {
    action();
  }
};

(5).times(function() {
  console.log("OMG");
});
