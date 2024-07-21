const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const S = Number(input[0]);
let count = 0;
for (let i = 1; i <= S; i++) {
  input[i].split("");
}

for (let i = 1; i <= S; i++) {
  const word = input[i];
  const letter = [];
  let isGroupWord = true;

  for (let j = 0; j < word.length; j++) {
    if (letter.indexOf(word[j]) === -1) {
      letter.push(word[j]);
    } else {
      if (letter.indexOf(word[j]) !== letter.length - 1) {
        isGroupWord = false;
        break;
      }
    }
  }

  if (isGroupWord) {
    count += 1;
  }
}

console.log(count);
