# 코딩 테스트 연습

# 2739 o
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
# 출력형식과 같게 N*1부터 N*9까지 출력한다.
n = int(input(""))
for i in range(1,10):
    print(f"{n} * {i} = {n*i}")

# 10950 o
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 A+B를 출력한다.
tlist = []
t = int(input())
for i in range(1, t+1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    tlist.append(a+b)

for i in tlist:
    print(i)

# 8393 o
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 1부터 n까지 합을 출력한다.
n = int(input())
s = 0
for i in range(1,n+1):
    s += i
print(s)

# 15552 x o
# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 
# 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.
import sys
slist = []
t = int(sys.stdin.readline())
for i in range(1,t+1):
    a, b = (sys.stdin.readline()).split()
    s = 0
    a = int(a)
    b = int(b)
    slist.append(a+b)
for i in slist:
    print(i)

# 2741 o
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
import sys
n = int(sys.stdin.readline())
for i in range(1, n+1):
    print(i)

# 2742 o
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
import sys
n = int(sys.stdin.readline())
for i in range(n,0,-1):
    print(i)

# 11021 o
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 
# 테스트 케이스 번호는 1부터 시작한다.
# tlist = []
t = int(input())
for i in range(1,t+1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(f"Case #{i}: {a+b}")
    # tlist.append(a+b)
# for i in tlist:
#     print(f"Case #{tlist.index(i)+1}: {i}")

# 11022 o
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. 
# x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
t = int(input())
for i in range(1,t+1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(f"Case #{i}: {a} + {b} = {a+b}")

# 2438 o
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()

# 2439 x o
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
n = int(input())
for i in range(1, n+1):
    for j in range(1,n+1):
        if j <= n-i:
            print(" ", end="")
        else:
            print("*", end="")
    print()

# 10871 x
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 
# 10,000보다 작거나 같은 정수이다.
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. 
# X보다 작은 수는 적어도 하나 존재한다.
n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    if i < x:
        print(i, end=" ")


    











