const input = require("fs").readFileSync("/dev/stdin").toString();

N = Number(input);

for (let i = 1; i <= N; i++) {
  console.log(" ".repeat(N - i) + "*".repeat(2 * i - 1));
}
for (let i = N - 1; i > 0; i--) {
  console.log(" ".repeat(N - i) + "*".repeat(2 * i - 1));
}
