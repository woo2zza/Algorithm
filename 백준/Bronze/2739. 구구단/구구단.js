const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString();

const number = parseInt(input[0]);

for (let i = 1; i < 10; i++) {
  console.log(`${number} * ${i} = ${number * i}`);
}
