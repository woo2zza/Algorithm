# [Bronze III] 팰린드롬인지 확인하기 - 10988

[문제 링크](https://www.acmicpc.net/problem/10988)

### 성능 요약

메모리: 31120 KB, 시간: 36 ms

### 분류

구현, 문자열

### 제출 일자

2024년 7월 16일 17:41:33

### 문제 설명

<p>알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.</p>

<p>팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. </p>

<p>level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.</p>

### 입력

 <p>첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.</p>

### 출력

 <p>첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.</p>

## 추가 내용

내림 사용해서 절반값 구하기

arr = [1,2,3,4,5]

```javascript
S = Math.floor(arr.length / 2);
console.log(S); // 2
```

```python
S = len(arr)//2
print(S) # 2
```
