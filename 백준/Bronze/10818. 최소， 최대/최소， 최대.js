const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const arr = input[1].split(" ").map(Number);

const minValue = Math.min(...arr);
const maxValue = Math.max(...arr);

console.log(`${minValue} ${maxValue}`);
