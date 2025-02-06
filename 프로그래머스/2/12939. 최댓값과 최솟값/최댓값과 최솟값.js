function solution(s) {
    arr = s.split(' ').map(Number)
    
    return `${Math.min(...arr)} ${Math.max(...arr)}`
}