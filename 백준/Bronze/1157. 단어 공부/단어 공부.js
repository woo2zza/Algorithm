const input = require("fs").readFileSync("/dev/stdin").toString();
const arr = input.toUpperCase();
const bucket = Array(26).fill(0);
const upperArr = arr.split("");
for (let i = 0; i < upperArr.length; i++) {
  bucket[upperArr[i].charCodeAt() - 65] += 1;
}

const maxChar = Number(bucket.indexOf(Math.max(...bucket)) + 65);
let count = bucket.filter((v) => Number(v) == Math.max(...bucket)).length;

if (count >= 2) {
  console.log("?");
} else {
  console.log(String.fromCharCode(maxChar));
}
