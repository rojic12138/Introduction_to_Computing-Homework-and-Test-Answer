#约瑟夫问题 见单独py文件

#完美立方 http://cs101.openjudge.cn/practice/02810
# n = int(input())
# for a in range(2,n+1):
#     for d in range(a-1,1,-1):
#         for c in range(d,1,-1):
#             for b in range(c,1,-1):
#                 if a**3 == b**3+c**3+d**3:
#                     print(f"Cube = {a}, Triple = ({b},{c},{d})")

#圣诞老人的礼物 http://cs101.openjudge.cn/practice/04110
n,w = [int(x) for x in input().split()]
sugars = []
for i in range(n):
    sugars.append([int(x) for x in input().split()])
sugars.sort(key = lambda x:x[0]/x[1],reverse=True)#按单位价值从高到低排列
value = 0
for i in range(n):
    if w>sugars[i][1]:
        w-=sugars[i][1]
        value+=sugars[i][0]
    else:
        value+=sugars[i][0]/sugars[i][1]*w
        break
print(f"{value:.1f}")

#Woodcutters https://codeforces.com/problemset/problem/545/C
#先往左，再往右
# n = int(input())
# trees = []
# for i in range(n):
#     x,h = [int(x) for x in input().split()]
#     trees.append([x,h])

# left = -1e10
# tot = 0
# for i in range(n-1):
#     if trees[i][0]-left>trees[i][1]:
#         tot += 1
#         left = trees[i][0]
#     elif trees[i+1][0]-trees[i][0]>trees[i][1]:
#         tot += 1
#         left = trees[i][0]+trees[i][1]
#     else:
#         left = trees[i][0]
# print(tot+1)

#充实的寒假生活 http://cs101.openjudge.cn/practice/16528
#以活动结束时间来做贪心
# n = int(input())
# s = [[int(x) for x in input().split()] for _ in range(n)]
# s.sort(key = lambda x:x[1])
# m = s[0][1]
# a = 1
# for i in range(1,n):
#     if s[i][0] > m:
#         a += 1
#         m = s[i][1]
# print(a)

#排列 http://cs101.openjudge.cn/practice/01833
#利用permutations，超出空间
# from itertools import permutations
# m = int(input())
# for i in range(m):
#     n,k = [int(x) for x in input().split()]
#     lis = [int(x) for x in input().split()]
#     ori = sorted(lis)
#     perm = list(permutations(ori))
#     index = perm.index(tuple(lis))
#     index_k = (index+k)%len(perm)
#     for x in perm[index_k]:
#         print(x,end=' ')

#每次调整最后几个数字
# m = int(input())
# for i in range(m):
#     n,k = [int(x) for x in input().split()]
#     lis = [int(x) for x in input().split()]
#     for j in range(k):#处理k次
#         flag = False
#         for t in range(n-1,0,-1):
#             if lis[t-1] < lis[t]:
#                 flag = True
#                 left = t-1
#                 break
#         if not flag:
#             lis.reverse()
#             continue
#         min_index,min_num = 0,1e6
#         for t in range(left+1,n):
#             if lis[t]>lis[left]:
#                 if lis[t]<min_num:
#                     min_num = lis[t]
#                     min_index = t
#         #交换min_index与left
#         lis[min_index],lis[left] = lis[left],lis[min_index]
#         lis[left+1:] = lis[-1:left:-1]
#     for x in lis:
#         print(x,end=' ')
#     print()
