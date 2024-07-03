const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const N = Number(input[0]);

const arr = input[1].split(" ").map(Number);
const maxScore = Math.max(...arr);

const result = arr.map((v) => (v / maxScore) * 100);

const value = result.reduce((sum, value) => sum + value) / N;
console.log(value);
