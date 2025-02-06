function solution(A,B){
    A.sort((a,b) => a - b)
    B.sort((a,b) => b - a)
    
    result = A.reduce((sum, a, i) => sum + a * B[i], 0)
    return result
}