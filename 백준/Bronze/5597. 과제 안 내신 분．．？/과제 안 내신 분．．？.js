const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let arr = Array(input.length + 2).fill(false);
input.forEach((v) => {
  arr[v] = true;
});

for (let i = 1; i < input.length + 2; i++) {
  if (!arr[i]) {
    console.log(i);
  }
}
