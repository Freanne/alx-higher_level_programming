
exports.nbOccurences = function (list, searchElement) {
  // Use the reduce method to count occurrences
  return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
