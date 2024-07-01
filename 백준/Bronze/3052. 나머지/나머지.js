const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(Number);
let arr = Array(42).fill(0);

input.forEach((v) => {
  arr[v % 42] = 1;
});

const sum = arr.reduce((accumulator, current) => accumulator + current, 0);
console.log(sum);
