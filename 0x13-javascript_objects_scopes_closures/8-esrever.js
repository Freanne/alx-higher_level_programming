exports.esrever = function (list) {
  // Clone the original list to avoid modifying it
  const reversedList = [...list];

  // Use a loop to reverse the elements of the list without using the reverse method
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    // Swap elements at positions i and j
    const temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }

  return reversedList;
};
