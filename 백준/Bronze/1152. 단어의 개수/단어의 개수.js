const input = require("fs").readFileSync("/dev/stdin").toString();
const arr = input.trim().split(" ");

let count = 0;
for (let i = 0; i < arr.length; i++) {
  if (arr[i] !== "") {
    count++;
  }
}
console.log(count);
