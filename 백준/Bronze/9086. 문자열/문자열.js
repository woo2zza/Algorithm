const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const N = Number(input[0]);

for (let i = 1; i < N + 1; i++) {
  console.log(`${input[i][0]}${input[i][input[i].length - 1]}`);
}
