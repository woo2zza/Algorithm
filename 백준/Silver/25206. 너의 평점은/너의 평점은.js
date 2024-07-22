const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let score = 0;
let passScore = 0;
const arr = [
  { grade: "A+", score: 4.5 },
  { grade: "A0", score: 4 },
  { grade: "B+", score: 3.5 },
  { grade: "B0", score: 3 },
  { grade: "C+", score: 2.5 },
  { grade: "C0", score: 2 },
  { grade: "D+", score: 1.5 },
  { grade: "D0", score: 1 },
  { grade: "F", score: 0 },
];
for (let i = 0; i < input.length; i++) {
  for (let j = 0; j < 9; j++) {
    if (input[i].split(" ")[2] === arr[j].grade) {
      const grade = input[i].split(" ")[1] * arr[j].score;
      score += grade;
      passScore += Number(input[i].split(" ")[1]);
    }
  }
}

console.log(score / passScore);
