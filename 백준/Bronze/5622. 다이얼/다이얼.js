const input = require("fs").readFileSync("/dev/stdin").toString().split("");

arr = [
  ["A", "B", "C"],
  ["D", "E", "F"],
  ["G", "H", "I"],
  ["J", "K", "L"],
  ["M", "N", "O"],
  ["P", "Q", "R", "S"],
  ["T", "U", "V"],
  ["W", "X", "Y", "Z"],
];
let result = [];
for (let i = 0; i < arr.length; i++) {
  for (let j = 0; j < input.length; j++) {
    if (arr[i].includes(input[j])) {
      result.push(i + 3);
    }
  }
}
console.log(result.reduce((a, b) => a + b, 0));
