const input = require("fs").readFileSync("/dev/stdin").toString().trim();
const arr = input.split("");
let count = 0;
for (let i = 0; i < arr.length; i++) {
  if ((arr[i] == "=") | (arr[i] == "-")) {
    if ((arr[i - 1] == "z") & (arr[i - 2] == "d")) {
      count += 2;
    } else {
      count += 1;
    }
  }
  if ((arr[i + 1] == "j") & (arr[i] == "l")) {
    count += 1;
  }
  if ((arr[i + 1] == "j") & (arr[i] == "n")) {
    count += 1;
  }
}

console.log(arr.length - count);
