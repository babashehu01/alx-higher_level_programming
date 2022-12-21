#!/usr/bin/node
exports.esrever = function (list) {
  const length = list.length;
  const rev = [];
  for (let i = length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
