const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const [arr, i] = input;
console.log(arr[i - 1]);
