const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const count = parseInt(input[0]);
const arr = input[1].split(" ");
const find = parseInt(input[2]);

let result = 0;
for (let i = 0; i < count + 1; i++) {
  if (parseInt(arr[i]) == find) result += 1;
}
console.log(result);
