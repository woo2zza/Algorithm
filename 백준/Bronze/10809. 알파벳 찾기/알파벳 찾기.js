const input = require("fs").readFileSync("/dev/stdin").toString().trim();
const S = input;
const lst = Array.from(S).map((v) => {
  return v.charCodeAt() - 97;
});
const result = Array(26).fill(-1);

for (let i = 0; i <= lst.length; i++) {
  if (result[lst[i]] == -1) {
    result[lst[i]] = i;
  }
}

console.log(result.join(" "));
