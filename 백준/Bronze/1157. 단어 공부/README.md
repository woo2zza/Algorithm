# [Bronze I] 단어 공부 - 1157

[문제 링크](https://www.acmicpc.net/problem/1157)

### 성능 요약

메모리: 34952 KB, 시간: 220 ms

### 분류

구현, 문자열

### 제출 일자

2024년 7월 18일 00:35:32

### 문제 설명

<p>알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.</p>

### 입력

 <p>첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.</p>

### 출력

 <p>첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.</p>

## 추가 내용

대소문자 변환 / 아스키코드, 문자 변환 / index구하기

```markdown
arr = [64, 65, 66]
num = 65
string1 = A
string2 = a
```

```javascript
string2.toUpperCase(); // A
string1.toLowerCase(); // a

string1.codeCharAt(); // 65
String.fromCharCode(num); // A

arr.indexOf(num); // 2
```

```python
string2.upper() # A
string1.lower() # a

ord(string1) # 65
chr(num) # A

arr.index(num) # 2
```
