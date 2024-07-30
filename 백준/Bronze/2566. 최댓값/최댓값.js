const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let arr = [];

for (let i = 0; i < 9; i++) {
  let arr2 = [];
  const numbers = input[i].split(" ").map(Number);
  const maxNum = Math.max(...numbers);
  const maxIndex = numbers.indexOf(maxNum);

  arr2.push(maxNum, i, maxIndex);
  arr.push(arr2);
}

let overallMax = arr[0][0];
let maxRow = 0;
let maxCol = arr[0][2];

for (let j = 1; j < arr.length; j++) {
  if (arr[j][0] > overallMax) {
    overallMax = arr[j][0];
    maxRow = arr[j][1];
    maxCol = arr[j][2];
  }
}

console.log(overallMax);
console.log(maxRow + 1, maxCol + 1);
