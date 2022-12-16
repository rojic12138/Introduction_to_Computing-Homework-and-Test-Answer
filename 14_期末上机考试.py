#考试链接http://cs101.openjudge.cn/cs101_2022fe_class13/
#二进制回文的整数
# n = int(input())
# s = bin(n)[2:]
# flag = True
# for i in range(len(s)//2):
#     if s[i] != s[len(s)-i-1]:
#         flag = False
#         print('No')
#         break
# if flag:
#     print('Yes')

#木板掉落
#只需要和排序后下标为n//2的小球同时到达即可
# H,L,n = [int(x) for x in input().split()]
# vs = [float(x) for x in input().split()]
# vs.sort()
# v = vs[n//2]
# time = L/v
# fall = 0.5*10*time**2
# print(f"{H-fall:.2f}")

#螃蟹采蘑菇
#dfs
# n = int(input())
# lst = [[int(x) for x in input().split()] for _ in range(n)]
# gone=[[0 for i in range(n)] for j in range(n)]

# def f(x1,y1,x2,y2,r):
#     if x1<0 or x1>=r or y1<0 or y1>=r or x2<0 or x2>=r or y2<0 or y2>=r:
#         return False
#     if lst[x1][y1]==1 or lst[x2][y2]==1 or gone[x1][y1]==1:
#         return False
#     if lst[x1][y1]==9 or lst[x2][y2]==9:
#         return True
#     gone[x1][y1]=1
#     flag= f(x1-1,y1,x2-1,y2,r) or f(x1+1,y1,x2+1,y2,r) or f(x1,y1+1,x2,y2+1,r) or f(x1,y1-1,x2,y2-1,r)
#     return flag

# tmp=0
# x1=y1=x2=y2=-1
# for i in range(n):
#     for j in range(n):
#         if lst[i][j]==5 and tmp==0:
#             tmp=1
#             x1=i
#             y1=j
#         elif lst[i][j]==5 and tmp==1:
#             x2=i
#             y2=j

# ok=f(x1,y1,x2,y2,n)
# if ok==True:
#     print("yes")
# else:
#     print("no")

#红蓝玫瑰
#greedy + dp
# s = input()
# R,B = [0]*len(s),[0]*len(s)#R[i]表示前i位都是红需要的翻转次数
# for i in range(1,len(s)):
#     if s[i] == 'R':
#         R[i] = R[i-1] 
#         B[i] = min(R[i-1],B[i-1]) + 1 #代表两种魔法
#     else:
#         B[i] = B[i-1]
#         R[i] = min(R[i-1],B[i-1]) + 1
# print(R[-1])

#CPU调度
#以写时间从大到小排序，求和即可
'''
来自zyn：
贪心题，按写文件时间从大到小排序调度，扫一次排序后的任务列表找到最晚完成的时间点即可

性质：一定存在不出现任务交错，即每个任务完整计算完再进行下一个任务的最优调度。
证明：假设有两个交错调度的任务i和j，j后完成计算，可以重新排序为先调度完i，再调度j，
这样对于i来说计算完成时间不变或提前了，对于j来说计算完成时间不变，因为原来j完成时也已经过了i+j个时间，
于是交换后不出现交错的调度方法不会比原来差。对于一个完整的调度序列，可以反复使用该性质将所有任务调整为非交错调度。

贪心性质的正确性：假设两个任务i和j，计算时间分别为ci和cj，写文件时间分别为wi和wj，且wi>wj。
先i后j的完成时间：fij=max(ci+wi, ci+cj+wj)
先j后i的完成时间：fji=max(ci+cj+wi, cj+wj)，由于wi>wj且所有时间为正数，所以ci+cj+wi>cj+wj，fji=ci+cj+wi
对于fij，其两种选择ci+wi和ci+cj+wj均小于ci+cj+wi，于是有fij<fji，即只要满足wi>wj，则优先调度i会使总体完成时间更短
'''
# n = int(input())
# compute, write = [], []
# for i in range(n):
#     c, w = [int(x) for x in input().split()]
#     compute.append(c)
#     write.append(w)
# ans = t = 0
# for c, w in sorted(zip(compute, write), key=lambda x: -x[1]):
#     t += c
#     ans = max(ans, t + w)
# print(ans)

#洋葱
# n = int(input())
# matrix = [[int(x) for x in input().split()] for y in range(n)]
# layer_num = (n-1)//2+1 #0-layer_num
# sums = []
# for i in range(layer_num):
#     sum = 0
#     for j in range(i,n-i):
#         sum += matrix[i][j]
#         sum += matrix[n-i-1][j]
#         sum += matrix[j][i]
#         sum += matrix[j][n-i-1]
#     if not (i == layer_num-1 and layer_num % 2 == 1):
#         sum -= matrix[n-i-1][n-i-1]
#         sum -= matrix[i][n-i-1]
#         sum -= matrix[n-i-1][i]
#         sum -= matrix[i][i]
#     else:
#         sum = int(sum/4)
#     sums.append(sum)
# print(max(sums))