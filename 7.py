#A. Lucky Division https://codeforces.com/problemset/problem/122/A

# def lucky(i):
#     if len(str(i)) == str(i).count('4') + str(i).count('7'):
#         return True
#     return False
# nums = []
# for i in range(1,1001):
#     if lucky(i):
#         nums.append(i)
# for i in range(1,1001):
#     for num in nums:
#         if i%num == 0:
#             nums.append(i)
#             break
# a = int(input())
# if a in nums:
#     print('YES')
# else:
#     print('NO')

#B. Vanya and Lanterns https://codeforces.com/problemset/problem/492/B
#超出空间限度的版本
# n,l = [int(x) for x in input().split()]
# a = [int(x) for x in input().split()]
# lantern = [0]*(l+1)
# for ai in a:
#     lantern[ai] = 1
# maxn = 0
# before = -1
# for i in range(l):
#     if lantern[i] == 1:
#         if before == -1:
#             maxn = i
#         else:
#             maxn = max(maxn,(i-before)/2)
#         before = i
# maxn = max(maxn,l-(before+1))
# print(maxn)

#AC版
# n,l = [int(x) for x in input().split()]
# lanterns = list({int(x) for x in input().split()})
# lanterns.sort()
# maxn = lanterns[0]
# for i in range(1,len(lanterns)):
#     maxn = max(maxn,(lanterns[i]-lanterns[i-1])/2)
# maxn = max(maxn,l-lanterns[-1])
# print(maxn)

#提取实体v0.3 http://cs101.openjudge.cn/practice/19949
#利用re
# import re
# n = int(input())
# sum_str = ""
# for i in range(n):
#     s = input()
#     s = s.replace("### ###","")
#     sum_str = sum_str+s
# print(len(re.findall("###(.*?)###",sum_str)))

#赋值、浅拷贝与深拷贝 http://cs101.openjudge.cn/practice/25274
#抄一遍就行，主要是理解三者的差异
# import copy
# a = [[1, 2, 3], 'abc', [1, 3], 4]
# b = a 
# c = copy.copy(a)
# d = copy.deepcopy(a)
# a[0].append(4)
# a[1] = 'def'
# a.append(5)
# print(b)
# print(c)
# print(d)

#T-primes http://codeforces.com/problemset/problem/230/B
#筛法
# flag = [True]*(10**6+5)
# flag[1] = False
# for i in range(1,10**6+2):
#     if flag[i] == True:
#         k = 2
#         while i*k<=10**6+2:
#             flag[i*k] = False
#             k += 1
 
# n = int(input())
# lis = [int(x) for x in input().split()]
# for i in range(n):
#     a = lis[i]
#     if(a**0.5%1 != 0):
#         print("NO")
#     elif(flag[int(a**0.5)] == True):
#         print("YES")
#     else :
#         print("NO")

# Light It Up https://codeforces.com/problemset/problem/1000/B
# n,m = [int(x) for x in input().split()]
# a = [0]+[int(x) for x in input().split()]+[m]
# #light black light black
# light = [0]
# for i in range(1,n+2):
#     if i%2 == 0:
#         light.append(light[-1])
#     else:
#         light.append(light[-1]+a[i]-a[i-1])
# maxn = light[-1]
# for i in range(1,n+2):#在第i-1个区间（i个开关前）增加开关
#     tot = a[i]-a[i-1]-1+light[i-1]+(a[n+1]-a[i]-(light[n+1]-light[i]))
#     maxn = max(maxn,tot)
# print(maxn)