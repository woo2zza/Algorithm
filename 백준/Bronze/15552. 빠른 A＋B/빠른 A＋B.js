const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const num = Number(input[0]);
let answer = '';

for(let i =1; i <= num; i++ ){
  let A = input[i].split(' ');
  answer += (Number(A[0]) + Number(A[1])) + '\n';
}
console.log(answer);