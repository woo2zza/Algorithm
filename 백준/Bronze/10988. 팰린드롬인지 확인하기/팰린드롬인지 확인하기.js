const input = require("fs").readFileSync("/dev/stdin").toString().trim();

arr = input.split("");
let Flag = 1;

for (let i = 0; i < Math.floor(arr.length / 2); i++) {
  if (arr[i] !== arr[arr.length - i - 1]) {
    Flag = 0;
    break;
  }
}

console.log(Flag);

