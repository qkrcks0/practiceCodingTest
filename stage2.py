# 코딩테스트 연습

# 1330 o
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
# 첫째 줄에 다음 세 가지 중 하나를 출력한다.
# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.
a, b = input().split()
a = int(a)
b = int(b)
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")

# 9498 o
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 
# 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 
# 100보다 작거나 같은 정수이다.
# 시험 성적을 출력한다.
grade = int(input())
if 90 <= grade <= 100:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
else:
    print("F")

# 2753 o
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
# 첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 
# 4000보다 작거나 같은 자연수이다.
# 첫째 줄에 윤년이면 1, 아니면 0을 출력한다.
year = int(input())
if year%4 == 0:
    if year%100 != 0 or year%400 == 0:
        print("1")
    else:
        print("0")
else:
    print("0")

# 14681 o
# 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 
# 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. 
# "Quadrant n"은 "제n사분면"이라는 뜻이다.
# 첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 
# 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)
# 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")
                
# 2884 o
# 바로 "45분 일찍 알람 설정하기"이다.
# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 
# 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.
# 입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 
# 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.
h, m = input().split()
h = int(h)
m = int(m)
if h >= 1:
    if 45 <= m <= 59:
        print(str(h), str(m-45))
    else:
        print(str(h-1), str(60+m-45))
else:
    if 45 <= m <= 59:
        print(str(h), str(m-45))
    else:
        print(str(24+h-1), str(60+m-45))








