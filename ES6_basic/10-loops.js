export default function appendToEachArrayValue(inputArray, appendString) {
  const newArray = [...inputArray];

  for (const value of inputArray) {
    newArray.push(appendString + value);
  }

  return newArray;
}
