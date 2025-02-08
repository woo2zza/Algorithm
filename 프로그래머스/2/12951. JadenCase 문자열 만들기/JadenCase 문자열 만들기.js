function solution(s) {
    let arr = [];
    let answer = s.split(' ');

    for (let i = 0; i < answer.length; i++) {
        if (answer[i]) {  
            arr.push(answer[i][0].toUpperCase() + answer[i].slice(1).toLowerCase());
        } else {
            arr.push(''); 
        }
    }
    
    return arr.join(' ');
}
