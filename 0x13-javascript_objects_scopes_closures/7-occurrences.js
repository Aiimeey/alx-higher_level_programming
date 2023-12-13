#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const value of list) {
    if (value === searchElement) {
      i += 1;
    }
  }
  return i;
};
