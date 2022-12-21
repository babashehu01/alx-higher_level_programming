#!/usr/bin/node
exports.esrever = function (list) {
  const length = list.length;
  let rev = [];
  for (let i = length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
