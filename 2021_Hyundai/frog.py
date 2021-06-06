'''
헬스장에서 N명의 회원이 운동을 하고 있다. 각 회원은 1에서 N사이의 번호가 부여되어 있고, i번 회원이 들 수 있는 역기의 무게는 Wi이다.
회원들 사이에는 M개의 친분관계 (Aj, Bj)가 있다. (Aj, Bj)는 Aj번 회원과 Bj번 회원이 친분 관계가 있다는 것을 의미한다.
i번 회원은 자신과 친분 관계가 있는 다른 회원보다 들 수 있는 역기의 무게가 무거우면 자신이 최고라고 생각한다.
이 헬스장에서 자신이 최고라고 생각하는 회원은 몇 명인가?

입력형식
첫 번째 줄에 두 정수 N,M이 주어진다.
두 번째 줄에 N개의 정수 W1, W2, ... , WN이 주어진다.
다음 M개의 줄의 j번째 줄에는 두 정수 Aj, Bj가 주어진다.

입력은 다음 조건을 만족한다.
    2 ≤ N ≤ 105
    1 ≤ M ≤ 105
    1 ≤ Wi ≤ 109
    1 ≤ Aj, Bj ≤ N
    Aj ≠ Bj

출력형식
첫 번째 줄에 자신이 최고라고 생각하는 회원 수를 출력한다.

입력예제1
5 3
1 2 3 4 5
1 3
2 4
2 5
출력예제1
3

입력예제2
5 3
7 5 7 7 1
1 2
2 3
3 4
출력예제2
2
'''

N, M = map(int, input().split())

weight = list(map(int, input().split()))
check = [0 for _ in range(N)]

cnt = 0

for i in range(M):
    Aj, Bj = map(int, input().split())

    if weight[Aj-1] > weight[Bj-1]:
        check[Aj-1] = 1
        #check[Bj-1] = 0
    elif weight[Aj-1] < weight[Bj-1]:
        #check[Aj-1] = 0
        check[Bj-1] = 1

print(sum(check))
