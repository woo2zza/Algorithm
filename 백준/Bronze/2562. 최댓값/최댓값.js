const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map(Number);

const maxValue = Math.max(...input);
const maxIndex = input.indexOf(maxValue);
console.log(maxValue);
console.log(maxIndex + 1);
