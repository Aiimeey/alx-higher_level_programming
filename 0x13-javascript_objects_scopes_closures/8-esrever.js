#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0; let j = list.length - 1; let k;
  while (i !== Math.floor(list.length / 2)) {
    k = list[i];
    list[i] = list[j];
    list[j] = k;
    i++; j--;
  }
  return list;
};
