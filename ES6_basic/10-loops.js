export default function appendToEachArrayValue(array, appendString) {
  const newArray = [...array];

  for (const value of array) {
    newArray.push(appendString + value);
  }

  return newArray;
}
