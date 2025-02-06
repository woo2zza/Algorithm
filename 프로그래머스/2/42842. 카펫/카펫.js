function solution(brown, yellow) {
    let width = brown / 2 
    let height = 2
    let result = -1
    
    while (result !== 0) {
        width--
        height++
        let mul = width * height
        result = mul - brown - yellow
    }
    return [width, height]
}