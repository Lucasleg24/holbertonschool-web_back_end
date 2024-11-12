export default function appendToEachArrayValue(inputArray, appendString) {
  const newArray = [];

  for (const value of inputArray) {
    newArray.push(appendString + value);
  }

  return newArray;
}
