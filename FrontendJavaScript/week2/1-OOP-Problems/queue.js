"use strict";

var queue = {
  items: [],
  push: function(item) {
    this.items.push(item);
  },
  pop: function() {
    this.items = this.items.slice(1);
    return this.items;
  },
  isEmpty: function() {
    return this.items.length === 0;
  }
};

var event_queue = (function() {
  var events = {};

  function on(eventName, f) {
    if(!events[eventName]) {
      events[eventName] = [];
    }
    events[eventName].push(f);
  }

  function remove(eventName) {
    if (events[eventName]) {
      events[eventName] = [];
    }
  }

  function trigger(eventName) {
    if (events[eventName]) {
      events[eventName].forEach(function(element) {
        element();
      });
    }
  }
  function getData() {
    return events;
  }

  return {
    on: on,
    remove: remove,
    trigger: trigger,
    getData: getData
  };
})();
