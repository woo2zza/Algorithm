const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const [N, M] = input[0].split(" ").map(Number);

const arr = Array(N).fill(0);
for (let i = 0; i < N; i++) {
  arr[i] = i + 1;
}

for (let num = 1; num <= M; num++) {
  const [i, j] = input[num].split(" ").map(Number);
  const dummy = arr[i - 1];
  arr[i - 1] = arr[j - 1];
  arr[j - 1] = dummy;
}
console.log(arr.join(" "));
