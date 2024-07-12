const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const S = parseInt(input[0]);

for (let i = 1; i <= S; i++) {
  const arr = input[i].split(" ");
  const repeatCount = parseInt(arr[0]);
  const result = arr[1]
    .split("")
    .map((char) => char.repeat(repeatCount))
    .join("");

  console.log(result);
}
