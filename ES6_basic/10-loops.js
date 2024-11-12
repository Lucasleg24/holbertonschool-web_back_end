export default function appendToEachArrayValue(array, appendString) {
  const newArray = [...array];

  for (const value of array) {
    newArray[array.indexOf(value)] = appendString + value;
  }

  return newArray;
}
