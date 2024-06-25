import sys

n,m = map(int, input().split())
arr = []
cp = []
result = 0
for _ in range(n):
	arr.append(list(map(int, input().split())))

for _ in range(m):
	x, y = map(int, input().split())
	cp.append([x-1, y-1])

def dfs(route, cnt):
	global result

	x=route[-1][0]
	y=route[-1][1]

	if [x, y] == cp[cnt]:
		cnt+=1

	if cnt == m:
		result += 1
		return

	#왼쪽 체크
	if x - 1 >= 0:
		if [x-1, y] not in route and arr[x-1][y] != 1:
			dfs(route + [[x-1, y]], cnt)
	
	#오른쪽 체크
	if x + 1 < n:
		if [x+1, y] not in route and arr[x+1][y] != 1:
			dfs(route + [[x+1, y]], cnt)

	#위 체크
	if y - 1 >= 0:
		if [x, y-1] not in route and arr[x][y-1] != 1:
			dfs(route + [[x, y-1]], cnt)
	
	#아래 체크
	if y + 1 < n:
		if [x, y+1] not in route and arr[x][y+1] != 1:
			dfs(route + [[x, y+1]], cnt)


dfs([cp[0]], 0)
print(result)