const input = require("fs").readFileSync("/dev/stdin").toString();

const count = parseInt(input);
const num = count / 4;
const str = "long";

const result = Array(num).fill(str).join(" ");
console.log(`${result} int`);
