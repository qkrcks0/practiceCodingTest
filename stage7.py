# 코딩테스트 연습
'''
# 11654
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 
# 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.
# 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.
# 입력으로 주어진 글자의 아스키 코드 값을 출력한다.
n = input()
print(ord(n)) # 문자를 숫자로

# 11720
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 입력으로 주어진 숫자 N개의 합을 출력한다.
n = int(input())
st = input()
s = 0 # n개의 숫자의 합을 담을 변수
for i in range(n): # 0~n-1 번째 인덱스 까지
    s += int(st[i]) # n개의 숫자의 합
print(s)

# 10809
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 
# 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... 
# z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 
# 두 번째 글자는 1번째 위치이다.
s = input()
# ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet = list(map(chr, range(97,123)))
for i in alphabet:
    if i in s: # a-z까지의 알파벳이 단어 s에 존재하면
        print(s.index(i), end=" ") # index값 출력
    else: # 아니면 -1 출력
        print(-1, end=" ")

# 2675
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
# S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. 
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 
# 각 테스트 케이스에 대해 P를 출력한다.

t = int(input()) # 테스트 케이스 개수
for i in range(t):
    r, s = input().split() # r: 반복횟수, s: 문자열
    for j in range(len(s)): 
        print(s[j]*int(r), end="")
    print()

# 1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

s = input().lower() # lower(): 소문자로 변환
ls = [0]*26
for i in range(len(ls)):
    # chr(): 아스키코드/숫자를 문자로
    if s.count(chr(i+97)) != 0: # 97~123: a~z
        # 각 알파벳이 s에 얼마나 쓰였는지 count
        ls[i] += s.count(chr(i+97)) 
if ls.count(max(ls)) >= 2: # 가장 많이 사용된 알파벳이 여러개일 때
    print("?")
else: # 대문자로 출력
    print(chr(ls.index(max(ls))+97).upper()) # upper(): 대문자로 변환

# 1152
# 영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다. 
# 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 
# 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
# 첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문자열이 주어진다. 
# 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 띄어쓰기 한 개로 구분되며, 
# 공백이 연속해서 나오는 경우는 없다. 또한 문자열의 앞과 뒤에는 공백이 있을 수도 있다.
# 첫째 줄에 단어의 개수를 출력한다.

s = input() # 문자열 입력
count = 0 # 단어 개수
for i in s.split(" "): # 띄어쓰기 단위로
    if len(i) == 0: # 공백일 때
        continue
    else:
        count += 1 # 공백이 아닐 때 count+1
print(count)

# 2908
# 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 
# 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 
# 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 
# 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
# 첫째 줄에 상수의 대답을 출력한다.
a,b = input().split()
alist = [i for i in a]
blist = [i for i in b]
alist.reverse()
blist.reverse()
a = int(alist[0]+alist[1]+alist[2])
b = int(blist[0]+blist[1]+blist[2])
print(max(a,b))

# 답
a,b = input().split()
# [::-1]: 처음 부터 끝까지 역순으로
a = a[::-1] 
b = b[::-1]
print(max(a,b))

# 5622
# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 
# 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 
# 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 
# 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어는 2글자~15글자로 이루어져 있다.
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.
s = input().upper()
time = 0
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in range(len(s)):
    for j in dial:
        if s[i] in j:
            time += dial.index(j)+3
print(time)

# 2941
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. 
# lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

s = input()
calph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
for i in calph:
    if i in s:
        count += 1
        s = s.replace(i, "*")
print(len(s))
'''
# 1316
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
# 첫째 줄에 그룹 단어의 개수를 출력한다.
n = int(input())
count = 0
for i in range(n):
    error = 0
    s = input()
    for j in list(set(s)):
        dp = [i for i, value in enumerate(s) if value == j]
        for k in range(len(dp)-1):
            if dp[k+1] - dp[k] != 1:
                error += 1; continue
    if error == 0: count+=1
    else: continue
print(count)



