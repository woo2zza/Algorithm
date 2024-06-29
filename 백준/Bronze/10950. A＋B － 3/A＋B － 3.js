const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const number = parseInt(input[0]);

for (let count = 1; count < number + 1; count++) {
  const score = input[count].split(" ");
  console.log(parseInt(score[0]) + parseInt(score[1]));
}
