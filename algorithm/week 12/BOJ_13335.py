import sys

input = lambda: sys.stdin.readline().rstrip()

# n 트럭의 개수
# w 다리길이
# L 최대하중 -> 동시에 올라가있는 트럭들의 무게의합 <= L
# a1, a2 .. 트럭의 무게 

n, w, l = map(int, input().split()) # 트럭의 개수, 다리길이, 최대 하중
t_weight = list(map(int, input().split())) # 트럭의 각 무게

time = 0 # 시간
bridge_len = [0] * w # 다리의 칸

while bridge_len:
    time += 1 # 시간 재기
    bridge_len.pop(0) # 다리의 칸을 한킨씩 줄인다

    # 모든 트럭을 확인
    if t_weight:

        # 현재 다리에 있는 트럭과 다리를 건너려는 트럭의 무게가 다리의 하중보다 작다면
        if sum(bridge_len) + t_weight[0] <= l: 
            # 현재 다리에 다리를 건너려는 트럭의 무게를 추가한다.
            bridge_len.append(t_weight.pop(0))

        # 다리의 하중보타 크다면 0을 추가
        else:
            bridge_len.append(0)

print(time)







