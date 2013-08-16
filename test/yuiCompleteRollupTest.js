/*global YUI, IS24, $*/

YUI.add('yuiCompleteRollupTest', function (Y) {
  "use strict";
  
  Y.namespace("IS24Test");  
  Y.IS24Test.yuiCompleteRollupTest = new Y.Test.Case({
    name: "yuiCompleteRollupTest",

    mockedNode: null,

    setUp: function () {
      var testNode = Y.Node.create('<div id="' + this.name + '" />');
      this.mockedNode = testNode;
      Y.one('body').append(testNode);
    },

    tearDown: function () {
      //this.mockedNode.remove(true);
    },

    "test dependency include is available": function () {
      this.mockedNode.append('<h2>Using YUI Version: ' + Y.version + '</h2>');

      Y.Assert.isInstanceOf(Object, Y);
      Y.Assert.isInstanceOf(Object, Y.Node);
      Y.Assert.isInstanceOf(Object, Y.Event);
      Y.Assert.isInstanceOf(Object, Y.IO);
    }
  });

}, '0.0.1', {
  requires: ["test", "node", "event", "io"]
});