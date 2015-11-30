var tape = require('tape');
var saveSvg = require('../');

tape('saveSvg() returns the answer to the ultimate question of life, the universe, and everything.', function(test) {
  test.equal(saveSvg.saveSvg(), 42);
  test.end();
});
