#12560:生存游戏(matrix) http://cs101.openjudge.cn/practice/12560/
# n,m = [int(x) for x in input().split()]
# matrix = []
# for i in range(n):
#     matrix.append([int(x) for x in input().split()])

# def check(i,j):#检查i,j的细胞邻居情况
#     global matrix
#     live_num = 0#存活邻居数量
#     if i > 0:
#         if j > 0:
#             if matrix[i-1][j-1] == 1:
#                 live_num += 1
#         if matrix[i-1][j] == 1:
#                 live_num += 1   
#         if j < m - 1 :
#             if matrix[i-1][j+1] == 1:
#                 live_num += 1 
#     if j > 0:
#         if matrix[i][j-1] == 1:
#             live_num += 1
#     if j < m - 1 :
#         if matrix[i][j+1] == 1:
#             live_num += 1 
#     if i < n-1:
#         if j > 0:
#             if matrix[i+1][j-1] == 1:
#                 live_num += 1
#         if matrix[i+1][j] == 1:
#                 live_num += 1   
#         if j < m - 1 :
#             if matrix[i+1][j+1] == 1:
#                 live_num += 1 

#     if matrix[i][j] == 1:
#         if live_num == 2 or live_num == 3:
#             return 1
#         else:
#             return 0
#     else:
#         if live_num == 3:
#             return 1
#         else:
#             return 0  

# answer = []
# for i in range(n):
#     answer.append([])
#     for j in range(m):
#         result = check(i,j)
#         answer[-1].append(result)
# for i in range(n):
#     for j in range(m):
#         print(answer[i][j],end=' ')
#     print()
    
#Pasha and Pixels https://codeforces.com/problemset/problem/508/A
# n,m,k = [int(x) for x in input().split()]
# pixels = [[0]*m for i in range(n)]

# def check(i,j):
#     #检查包含i,j的四个2*2方块是否有都是1的
#     if i>0:
#         #i,j是右下
#         if j>0:
#             if pixels[i-1][j-1] + pixels[i-1][j] + pixels[i][j-1] + pixels[i][j] == 4:
#                 return True
#         #左下
#         if j<m-1:
#             if pixels[i-1][j] + pixels[i-1][j+1] + pixels[i][j] + pixels[i][j+1] == 4:
#                 return True
#     if i<n-1:
#         #右上
#         if j>0:
#             if pixels[i][j-1] + pixels[i][j] + pixels[i+1][j-1] + pixels[i+1][j] == 4:
#                 return True
#         #左上
#         if j<m-1:
#             if pixels[i][j] + pixels[i][j+1] + pixels[i+1][j] + pixels[i+1][j+1] == 4:
#                 return True
#     return False

# flag = False
# for i in range(k):
#     x,y = [int(x) for x in input().split()]
#     pixels[x-1][y-1] = 1
#     if check(x-1,y-1):
#         flag = True
#         print(i+1)
#         break
# if not flag:
#     print(0)

#Sereja and Suffixes https://codeforces.com/problemset/problem/368/B
#找a下标li-n之间的不相同的元素个数
#already是list，超时
# n,m = [int(x) for x in input().split()]
# a = [int(x) for x in input().split()]
# answer = [1]*n #answer[i]为li-1对应答案
# already = [a[-1]] #已经有的元素
# for i in range(len(a)-2,-1,-1):#从倒数第二个开始
#     if a[i] not in already:
#         answer[i] = answer[i+1]+1
#         already.append(a[i])
#     else:
#         answer[i] = answer[i+1]
# for i in range(m):
#     x = int(input())
#     print(answer[x-1])

# #already是set，过
# n,m = [int(x) for x in input().split()]
# a = [int(x) for x in input().split()]
# answer = [1]*n #answer[i]为li-1对应答案
# already = {a[-1]} #已经有的元素
# for i in range(len(a)-2,-1,-1):#从倒数第二个开始
#     if a[i] not in already:
#         answer[i] = answer[i+1]+1
#         already.add(a[i])
#     else:
#         answer[i] = answer[i+1]
# for i in range(m):
#     x = int(input())
#     print(answer[x-1]

#Interesting drink https://codeforces.com/problemset/problem/706/B
#二分搜索 超时
# n = int(input())
# a = [int(x) for x in input().split()]
# a.sort()
# def binary_search(money,left=0,right=len(a)-1):
#     #money在a中的位置
#     # print(left,right)
#     if left == right or money == a[left] or left == right-1:
#         return left
#     if money == a[right]:
#         return right
#     mid = (left + right)//2
#     if money < a[mid]:
#         return binary_search(money,left,mid-1)
#     else:
#         return binary_search(money,mid,right)
# q = int(input())
# for i in range(q):
#     money = int(input())
#     find = binary_search(money)
#     while a[find] <= money:
#         find += 1
#         if find == n:
#             break
#     print(find)

#尝试用dict存储价格的次数，也超时
# n = int(input())
# a1 = [int(x) for x in input().split()]
# a1.sort()
# a = []
# for x in a1:
#     if x not in a:
#         a.append(x)
# d = {x:a1.count(x) for x in a}
# last = a[0]
# for x in d.keys():
#     if x == a[0]:
#         continue
#     d[x] += d[last]
#     last = x
# # print(d)
# def binary_search(money,left=0,right=len(a)-1):
#     #money在a中的位置
#     # print(left,right)
#     if left == right or money == a[left] or (left == right-1 and money < a[right]):
#         return left
#     if money == a[right] or (left == right-1 and money >= a[right]):
#         return right
#     mid = (left + right)//2
#     if money < a[mid]:
#         return binary_search(money,left,mid)
#     else:
#         return binary_search(money,mid,right)
# q = int(input())
# for i in range(q):
#     money = int(input())
#     find = binary_search(money)
#     # while a[find] <= money:
#     #     find += 1
#     #     if find == n:
#     #         break
#     if find == 0 and a[0] > money:
#         print(0)
#     else:
#         print(d[a[find]

#参考代码：用bisect_right
# import bisect
# input()
# x=sorted(map(int,input().split()))
# for i in range(int(input())):
# 	m=int(input())
# 	print(bisect.bisect_right(x,m))

#16531:上机考试 v0.3 http://cs101.openjudge.cn/practice/16531/
#纯纯模拟
# m,n=[int(x) for x in input().split()]
# table=[]
# for i in range(m):
#     table.append([int(x) for x in input().split()])
# exam=[]
# score=[]
# num=0
# for i in range(m*n):
#     t=input()
#     if(t==""): 
#         exam.append([-1]*num)
#         score.append(0)
#     else:
#         num=len(t.split())
#         exam.append(t.split())
#         s=0
#         for s1 in t.split():
#             if(s1=='1'):
#                 s+=1
#         score.append(s)
# similar=0
# for i in range(m):
#     for j in range(n):
#         if(i>0):
#             if(exam[table[i-1][j]]==exam[table[i][j]]):
#                 similar+=1
#                 continue
#         if(i<m-1):
#             if(exam[table[i+1][j]]==exam[table[i][j]]):
#                 similar+=1
#                 continue
#         if(j>0):
#             if(exam[table[i][j-1]]==exam[table[i][j]]):
#                 similar+=1
#                 continue
#         if(j<n-1):
#             if(exam[table[i][j+1]]==exam[table[i][j]]):
#                 similar+=1
#                 continue

# max_good=m*n*0.4
# good=0
# score_set=list(set(score))
# score_set.sort(reverse=True)
# for s in score_set:
#     tot=score.count(s)
#     if(good+tot>max_good):
#         break
#     else:
#         good+=tot
# print(similar,good)

#Cut Ribbon https://codeforces.com/problemset/problem/189/A
#动态规划，每步只有3个选择，取最大值
n,a,b,c = [int(x) for x in input().split()]
answer = [0]+[-1e5]*4001
for i in range(1,n+1):
    #这里从1开始，answer[i-a]是answer倒数的某个数，设成绝对值很大的负数才不会影响正确性
    #比如初始值为-10，a=2,那么answer[21] = 0
    answer[i] = max(answer[i-a],answer[i-b],answer[i-c]) + 1
print(answer[n])