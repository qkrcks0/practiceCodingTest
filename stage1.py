# 코딩테스트 연습

# 2557 o
# Hello World!를 출력하시오.
print("Hello World!")

# 10718 o
# 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.
print("강한친구 대한육군")
print("강한친구 대한육군")

# 10171 o
# 고양이를 출력한다.
print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

# 10172 o
# 개를 출력한다.
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")

# 1000 x
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A+B를 출력한다.
a, b = input().split() # *
a = int(a)
b = int(b)
print(a+b)

# 1001 o
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A-B를 출력한다.
a, b = input().split()
a = int(a)
b = int(b)
print(a-b)

# 10998 o
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A×B를 출력한다.
a, b = input().split()
a = int(a)
b = int(b)
print(a*b)

# 1008 o
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A/B를 출력한다. 
# 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.
a, b = input().split()
a = int(a)
b = int(b)
print(a/b)

# 10869 o
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
# 첫째 줄에 A+B, 둘째 줄에 A-B, 
# 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

# 10430 o
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 
# 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

# 2588 o
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 
# 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
a = input()
b = input()
print(int(a)*int(b[2]))
print(int(a)*int(b[1]))
print(int(a)*int(b[0]))
print(int(a)*int(b))




