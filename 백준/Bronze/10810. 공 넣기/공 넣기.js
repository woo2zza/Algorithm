const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const [N, M] = input[0].split(" ").map(Number);

const arr = Array(N)
  .fill()
  .map(() => 0);
for (let num = 1; num <= M; num++) {
  const [i, j, k] = input[num].split(" ").map(Number);
  for (let st = i - 1; st < j; st++) {
    arr[st] = k;
  }
}

console.log(arr.join(" "));
