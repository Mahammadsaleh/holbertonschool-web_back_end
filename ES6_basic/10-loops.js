/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
  for (const el of array) {
    array.push(appendString + el);
  }

  return array;
}
