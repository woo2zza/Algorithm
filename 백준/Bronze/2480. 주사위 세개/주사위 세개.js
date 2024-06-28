const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

const first = parseInt(input[0]);
const second = parseInt(input[1]);
const third = parseInt(input[2]);

if (first == second && first == third && second == third) {
  console.log(10000 + first * 1000);
} else if (first == second) {
  console.log(1000 + first * 100);
} else if (second == third) {
  console.log(1000 + second * 100);
} else if (first == third) {
  console.log(1000 + first * 100);
} else if (first !== second && second !== first && second !== third) {
  console.log(Math.max(first, second, third) * 100);
}
