const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const [n, arr, v] = input;

const count = arr.split(" ").filter((num) => num === v).length;

console.log(count);
