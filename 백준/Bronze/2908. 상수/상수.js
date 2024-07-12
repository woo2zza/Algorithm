const input = require("fs").readFileSync("/dev/stdin").toString().split(" ");

let arr = [];
for (let i = 0; i < input.length; i++) {
  arr.push(Number(input[i].split("").reverse().join("")));
}
console.log(arr[0] > arr[1] ? arr[0] : arr[1]);
