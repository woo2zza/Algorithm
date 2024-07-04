const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const N = Number(input[0]);
const arr = input[1].split("").map(Number);
const result = arr.reduce((a, b) => a + b, 0);
console.log(result);
