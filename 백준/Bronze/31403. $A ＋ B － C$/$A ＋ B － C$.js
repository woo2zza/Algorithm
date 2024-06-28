const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const first = input[0];
const second = input[1];
const third = parseInt(input[2]);

console.log(parseInt(first) + parseInt(second) - third);
console.log(first + second - third);
