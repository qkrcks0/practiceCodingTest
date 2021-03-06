# 1712
# 월드전자는 노트북을 제조하고 판매하는 회사이다. 노트북 판매 대수에 상관없이 
# 매년 임대료, 재산세, 보험료, 급여 등 A만원의 고정 비용이 들며, 
# 한 대의 노트북을 생산하는 데에는 재료비와 인건비 등 총 B만원의 가변 비용이 든다고 한다.
# 예를 들어 A=1,000, B=70이라고 하자. 이 경우 노트북을 한 대 생산하는 데는 총 1,070만원이 들며, 
# 열 대 생산하는 데는 총 1,700만원이 든다.
# 노트북 가격이 C만원으로 책정되었다고 한다. 일반적으로 생산 대수를 늘려 가다 보면 
# 어느 순간 총 수입(판매비용)이 총 비용(=고정비용+가변비용)보다 많아지게 된다. 
# 최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점(BREAK-EVEN POINT)이라고 한다.
# A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 21억 이하의 자연수이다.
# 첫 번째 줄에 손익분기점 즉 최초로 이익이 발생하는 판매량을 출력한다. 손익분기점이 존재하지 않으면 -1을 출력한다.
'''
a,b,c = map(int, input().split())
BREAK_EVEN_POINT = 0 # 손익 분기점
if c <= b: # 손익 분기점이 존재하지 않을 때
    BREAK_EVEN_POINT = -1
else: # 손익 분기점이 존재할 때
    BREAK_EVEN_POINT = a//(c-b) + 1
print(BREAK_EVEN_POINT)

# 2839
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 
# 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 
# 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 
# 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 
# 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

# 틀린 문제
def sugar(n):
    bag = 0
    while True:
        if n%5 == 0:
            bag = bag + (n//5)
            return bag
        n -= 3
        bag += 1
        if n < 0:
            return -1
print(sugar(int(input())))

# 2292
# 위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 
# 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 
# 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지
# (시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.
# 첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.
# 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.
bh = []
n = int(input())
i = 1
while True:
    # an = 3n(n-1)+1 / an-1 = 3(n-1)(n-2)+1
    final = (3*i*(i-1))+1
    bh.append(final)
    if n <= final:
        break
    i+=1
print(len(bh))

# # 1193
# 이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 
# 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
# 첫째 줄에 분수를 출력한다.

# n,ls = int(input()),[]
# for i in range(1,4473):
#     if i%2 == 0:
#         ls += [j for j in range(1, i+1)]
#     else:
#         ls += [j for j in range(i, 0, -1)]
#     if len(ls) >= n:
#         print(f"{ls[n-1]}/{i+1-ls[n-1]}")
#         break

n,i= int(input()),1
while n > i:
    n -= i
    i += 1
if i%2 == 0:
    print(f"{n}/{i+1-n}")
else:
    print(f"{i+1-n}/{n}")

# 2869
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 
# 또, 정상에 올라간 후에는 미끄러지지 않는다.
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

a,b,v = map(int, input().split())
day = 0
if (v-b) % (a-b) == 0:
    day = (v - b)//(a-b)
else:
    day = (v-b) // (a-b) + 1
print(day)

# while True:
#     v -= a
#     if v <= 0:
#         day += 1
#         break
#     else:
#         v += b
#         day += 1

# 10250
# 각 층에 W 개의 방이 있는 H 층 건물이라고 가정하자
# 모든 인접한 두 방 사이의 거리는 같은 거리(거리 1)라고 가정하고 호텔의 정면 쪽에만 방이 있다고 가정한다.
# 프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 
# T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 
# 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W). 
# 프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데,
# 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    x = n//h + 1
    y = n%h
    if y == 0:
        x -= 1
        y = h
    print(y*100 + x)

# 2775
# 평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 
# 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다. 이 아파트에 거주를 하려면 조건이 있는데, 
# “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 
# 는 계약 조항을 꼭 지키고 들어와야 한다.
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
# 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
# 첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 
# 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다. (1 <= k <= 14, 1 <= n <= 14)
# 각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

t = int(input()) # test case
for i in range(t):
    k = int(input()) # 층
    n = int(input()) # 호
    ls0 = [x for x in range(1,n+1)] # 0층
    for f in range(k):
        for u in range(1,n):
            ls0[u] += ls0[u-1]
    print(ls0[-1])
'''
# 1011
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    d = y-x
    count = 0
    move = 1
    move_plus = 0
    while d - move_plus > 0:
        count += 1
        move_plus += move
        if count % 2 == 0:
            move+=1
    print(count)







