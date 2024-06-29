const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const number = parseInt(input[0]);

for (let count = 1; count < number + 1; count++) {
  const [A, B] = input[count].split(" ").map(Number);
  console.log(`Case #${count}: ${A} + ${B} = ${A + B}`);
}
