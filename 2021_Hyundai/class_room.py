'''
[백준 1931]
김교수는 강의실 1개에 최대한 많은 강의를 배정하려고 한다. 배정된 강의는 서로 겹치지 않아야 하며 수업시간의 길이와 상관없이 최대한 강의를 많이 배정하라.

단, 두 강의의 시작시간과 종료시간은 겹쳐도 된다.

입력형식
첫 번째 줄에 강의 개수 N이 주어진다. i + 1 (1 ≤ i ≤ N)번째 줄에는 i번째 강의의 시작 시간 Si와 종료 시간 Fi가 주어진다.

입력은 다음 조건을 만족한다.
    1 ≤ N ≤ 106 인 정수
    1 ≤ Si ＜ Fi ≤ 109

출력형식
첫 번째 줄에 최대 강의 수를 출력하라.

입력예제
3
1 3
2 4
3 5

출력예제
2
'''

N = int(input())

time_table = []

for n in range(N):
    time_table.append(list(map(int, input().split())))

time_table.sort(key = lambda x : (x[1], x[0]))

cnt = 1
local_end = time_table[0][1]

for i in range(1, N):
    start, end = time_table[i][0], time_table[i][1]

    if local_end <= start:
        cnt += 1
        local_end = end

print(cnt)
