const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const total = parseInt(input[0]);
const count = parseInt(input[1]);

let totalItem = 0;

for (let i = 0; i < count; i++) {
  const [price, quantity] = input[i + 2].split(" ").map(Number);
  totalItem += price * quantity;
}

if (total == totalItem) {
  console.log("Yes");
} else {
  console.log("No");
}
