const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

const hour = parseInt(input[0]);
const min = parseInt(input[1]);

if (min > 45) {
  console.log(hour, min - 45);
} else if (min == 45) {
  console.log(hour, 0);
} else if (min < 45) {
  if (hour == 0) {
    console.log(23, 60 - 45 + min);
  } else {
    console.log(hour - 1, 60 - 45 + min);
  }
}
