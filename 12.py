#矩阵运算 http://cs101.openjudge.cn/practice/18161/
#模拟即可
# a,b,c = [],[],[]
# r,_ = [int(x) for x in input().split()]
# for j in range(r):
#     a.append([int(x) for x in input().split()])
# r,_ = [int(x) for x in input().split()]
# for j in range(r):
#     b.append([int(x) for x in input().split()])
# r,_ = [int(x) for x in input().split()]
# for j in range(r):
#     c.append([int(x) for x in input().split()])
# if len(a[0]) != len(b) or (len(a) != len(c) or len(b[0]) != len(c[0])):
#     print('Error!')
# else:
#     tmp = [[0]*len(b[0]) for _ in range(len(a))]
#     for i in range(len(a)):
#         for j in range(len(b[0])):
#             for k in range(len(a[0])):
#                 tmp[i][j] += a[i][k]*b[k][j]
#             c[i][j] += tmp[i][j]
#     for i in range(len(c)):
#         print(*c[i])

#波兰表达式 http://cs101.openjudge.cn/practice/02694/
#TODO
# stack = []
# tokens = input().split()
# tokens.reverse()
# mid = "+-*/"
# for token in tokens:
#     if token in mid:
#         tmp1 = stack.pop()
#         tmp2 = stack.pop()
#         stack.append(str(float(eval(tmp1+token+tmp2))))
#     else:
#         stack.append(token)
#     print(token,stack)
# print(float(stack[0]))

#最大连通域面积 http://cs101.openjudge.cn/practice/18160
# for _ in range(int(input())):
# 	N,M=map(int,input().split())
# 	c=[]
	
# 	for i in range(N):
# 		c.append(list(input()))

# 	co=[]
# 	dire=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
# 	for i in range(N):
# 		for j in range(M):
# 			if c[i][j]=='W':
# 				count=0
# 				count+=1
# 				que=[[i,j]]
# 				c[i][j]='.'
# 				while que:
# 					q=que.pop(0)
# 					for d in dire:
# 						x=q[0]+d[0]
# 						y=q[1]+d[1]
# 						if x>=0 and y>=0 and x<=N-1 and y<=M-1:
# 							if c[x][y]=='W':
# 								count+=1
# 								que.append([x,y])
# 								c[x][y]='.'
# 				co.append(count)
# 	if len(co)!=0:
# 		print(str(max(co)))
# 	else:
# 		print(0)
						
#你和你比较熟悉的同学 http://cs101.openjudge.cn/practice/21608
#TODO
# n = int(input())
# know = {}
# for i in range(n):
#     start,ends = input().split(' : ')
#     know[int(start)] = []
#     if ends[0] == '-1':
#         continue
#     for end in ends.split():
#         know[int(start)].append(int(end))
#         if int(end) not in know.keys():
#             know[int(end)] = []
# tots = {}#存dfs的结果，用集合表示
# def dfs(n):
#     #id为n的同学的最大有向子树
#     if n in tots.keys():
#         return tots[n]
#     tot = {n,}
#     tots[n] = tot
#     if know[n] == [-1]:
#         return tot
#     for end in know[n]:
#         tot |= dfs(end)
#     tots[n] = tot
#     return tot
# ans = 1
# del know[-1]
# for id in know.keys():
#     ans = max(ans,len(bfs(id)))
# #tots包括一个-1:[-1]，不影响结果
# print(ans)

#bfs，用queue存还没搜索的node
# d,ans={-1:set()},[]
# for _ in range(int(input())):
#     l=input().split()
#     d[int(l[0])]=set([int(i) for i in l[2:]])
# def bfs(i):
#     queue,visited=[i],{i}
#     while queue:
#         node=queue.pop(0)
#         visited.add(node)
#         queue=queue+list(d.get(node,set())-visited)
#     ans.append(len(visited-{-1}))
# for i in d.keys():
#     bfs(i)
# print(max(ans))

#Tian Ji -- The Horse Racing http://cs101.openjudge.cn/practice/02287
#TODO田忌每次拿最大值来换国王的最大值。比田忌最大值还大的国王马就用田忌最小的马来换
# while(1):
#     n = int(input())
#     if n == 0:
#         break
#     tj = [int(x) for x in input().split()]
#     king = [int(x) for x in input().split()]
#     tj.sort(reverse=True)
#     king.sort(reverse=True)
#     answer = 0
#     while(len(tj) != 0):
#         tj_horse = tj[0]
#         flag = False
#         for i in range(len(king)):
#             if king[i] < tj_horse:
#                 flag = True
#                 break
#         if i == 0:
#             answer = n 
#             break
#         if flag == False:
#             break
#         tj = tj[1:-i]
#         king = king[i:-1]
#         answer += 1
#     print((answer-(n-answer))*200)

#双指针法
# while True:
#     n = int(input())
#     if n==0:
#         break
#     *Tian, = map(int, input().split())
#     *King, = map(int, input().split())
#     Tian.sort()
#     King.sort()
#     lTian = 0; rTian = n - 1
#     lKing = 0; rKing = n - 1
#     ans = 0
#     while lTian <= rTian:
#         if Tian[lTian] > King[lKing]:
#             ans += 1;
#             lTian += 1
#             lKing += 1
#         elif Tian[rTian] > King[rKing]:
#             ans += 1
#             rTian -= 1
#             rKing -= 1
#         else:
#             if Tian[lTian] < King[rKing]:
#                 ans -= 1
#             lTian += 1
#             rKing -= 1
#     print(ans*200)

#八皇后 http://cs101.openjudge.cn/practice/02754
#先找出所有可能的排列
a=[]
def q(l,n):
    for i in "12345678":
        if not(i in n or sum(abs(int(i) - int(n[j])) == l - j for j in range(l))):
            if l == 7:
                a.append(n + i)
            else:
                q(l + 1, n + i)
q(0, "")
for _ in range(int(input())):
    print(a[int(input()) - 1])