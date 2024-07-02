const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const bucket = [];
for (let i = 0; i < N; i++) {
  bucket[i] = i + 1;
}

for (let i = 1; i <= M; i++) {
  let [a, b] = input[i].split(" ").map(Number);
  let arr = [];
  for (let j = a - 1; j < b; j++) {
    arr.push(bucket[j]);
  }
  arr.reverse();
  bucket.splice(a - 1, b - a + 1, ...arr);
}
console.log(bucket.join(" "));
