#图的拉普拉斯矩阵 http://cs101.openjudge.cn/practice/19943/
# n,m = [int(x) for x in input().split()]
# adjacent = [[0]*n for _ in range(n)]
# for i in range(m):
#     a,b = [int(x) for x in input().split()]
#     adjacent[a][b] = adjacent[b][a] = 1
# degree = [[0]*n for _ in range(n)]
# for i in range(n):
#     degree[i][i] = sum(adjacent[i])
# laplac = [[0]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         laplac[i][j] = degree[i][j] - adjacent[i][j]  
# for lis in laplac:
#     print(*lis)

#二维矩阵上的卷积运算v0.2 http://cs101.openjudge.cn/practice/19942/
# m,n,p,q = [int(x) for x in input().split()]
# matrix = []
# for i in range(m):
#     matrix.append([int(x) for x in input().split()])
# kernel = []
# for i in range(p):
#     kernel.append([int(x) for x in input().split()])
# def calc(i,j):
#     #output的[i,j]，对应matrix左上角为i,j时与kernel的卷积
#     ans = 0
#     for x in range(p):
#         for y in range(q):
#             ans += matrix[i+x][j+y] * kernel[x][y]
#     return ans
# output = [[0]*(n+1-q) for _ in range(m+1-p)]
# for i in range(m+1-p):
#     for j in range(n+1-q):
#         output[i][j] = calc(i,j)
# for lis in output:
#     print(*lis)

#螺旋矩阵 http://cs101.openjudge.cn/practice/18106/
"""
1 1 1 1 n n-1 n-1 n-2 n-2 n-3 n-3
0 0 0 1 
0 0 0 1 
0 0 0 1 
"""
# n = int(input())
# matrix = [[0]*n for i in range(n)]
# x,y,face = 0,0,"right"

# face_dict = {"right":"down","down":"left","left":"up","up":"right"}
# move_dict = {"right":[0,1],"down":[1,0],"left":[0,-1],"up":[-1,0]}
# count = 1
# oneway_sum = 0
# oneway_up = n
# even = True
# while(count <= n**2):
#     #填入一个元素
#     matrix[x][y] = count
#     oneway_sum += 1
#     if oneway_sum == oneway_up:
#         face = face_dict[face]
#         oneway_sum = 0
#         if even:#转弯前是第几次直行
#             oneway_up -= 1
#             even = False
#         else:
#             even = True
#     #更新x,y
#     x,y = x+move_dict[face][0],y+move_dict[face][1]
#     count += 1
# for lis in matrix:
#     print(*lis)
    
#最大上升子序列和 http://cs101.openjudge.cn/practice/03532/
# n = int(input())
# num = [int(x) for x in input().split()]
# dp = [x for x in num]
# answer = dp[0]
# for i in range(1,n):
#     for j in range(i):
#         if num[j]<num[i]:
#             dp[i] = max(dp[i],dp[j]+num[i])
#     answer = max(answer,dp[i])
# print(answer)
 
#数字三角形 http://cs101
# import copy
# n = int(input())
# num = []
# for i in range(n):
#     num.append([int(x) for x in input().split()])
# answer = 0
# dp = copy.deepcopy(num)
# for i in range(1,n):
#     for j in range(i+1):
#         if j >0 :
#             dp[i][j] = max(dp[i][j],dp[i-1][j-1]+num[i][j])
#         if j < i:
#             dp[i][j] = max(dp[i][j],dp[i-1][j]+num[i][j])
#         answer = max(answer,dp[i][j])
# print(answer)

#Ilya and Queries https://codeforces.com/contest/313/problem/B
# s = input()
# dp = [0]+[0]*len(s)
# for i in range(1,len(s)):
#     dp[i+1] = dp[i]+(s[i] == s[i-1])
# m = int(input())
# for i in range(m):
#     s,e = [int(x) for x in input().split()]
#     print(dp[e]-dp[s])

#Boredom https://codeforces.com/problemset/problem/455/A
# n = int(input())
# N = 10**5+1
# d = [0]*N
# for x in map(int,input().split()):
#     d[x] += x #[0, 2, 10, 6]
# dp = [x for x in d]
# dp[1] =  max(dp[0],dp[1])
# for i in range(2,N):
#     #要么继承前一个，要么继承前两个+自己
#     dp[i] = max(dp[i-1],dp[i-2]+d[i])
# print(dp[-1])



