#!/usr/bin/node
a = process.argv[2];
b = process.argv[3];
function add(a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(a, b);
