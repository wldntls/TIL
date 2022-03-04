# 색종이

paper_n = int(input())

paper_start = [list(map(int, input().split())) for i in range(paper_n)]

print(paper_start)

for i in range(paper_n):
    for j in range(2):
        parper_end = paper_start[i][j] + 10
        if paper_start[i][j] < paper_start[i][j] or parper_end[i][j] < parper_end:


