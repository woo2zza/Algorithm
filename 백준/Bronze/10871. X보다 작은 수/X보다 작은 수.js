const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const arr = input[1].split(" ").map(Number);
const [dummy, X] = input[0].split(" ");

const result = arr.filter((num) => num < parseInt(X));
console.log(result.join(" "));
