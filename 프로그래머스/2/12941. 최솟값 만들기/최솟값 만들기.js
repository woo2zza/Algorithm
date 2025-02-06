function solution(A,B){
    arr1 = A.sort((a,b) => a-b)
    arr2 = B.sort((a,b) => b-a)
    let result = 0
    for(i=0; i < A.length; i++ ){
        result += (arr1[i] * arr2[i])
    }
    return result;
}