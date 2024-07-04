# [Bronze V] 아스키 코드 - 11654

[문제 링크](https://www.acmicpc.net/problem/11654)

### 성능 요약

메모리: 9336 KB, 시간: 148 ms

### 분류

구현

### 제출 일자

2024년 7월 5일 01:40:20

### 문제 설명

<p>알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.</p>

### 입력

 <p>알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.</p>

### 출력

 <p>입력으로 주어진 글자의 아스키 코드 값을 출력한다.</p>

## 추가 내용

자바스크립트<br> 문자 -> 아스키코드 / 아스키코드 -> 문자

```javascript
const str = A;
result = str.charCodeAt();
console.log(result);
// 65

const num = 66;
result = String.fromCharCode(num);
console.log(result);
// B
```

파이썬<br> 문자 -> 아스키코드 / 아스키코드 -> 문자

```python
N = 'A'
print(ord(N))
// 65

M = 66
print(chr(M))
// B
```
