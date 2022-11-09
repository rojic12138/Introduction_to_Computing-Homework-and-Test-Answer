#多项式时间复杂度 http://cs101.openjudge.cn/20221103mockexam/E23563/
#用re的findall
# import re
# s = input()+"+"
# # s = s.replace(r"0n\^.*?\+","+") #str的replace不支持re的pattern
# s = re.sub(r"0n\^.*?\+","",s)#去掉系数为0的项
# nums = [int(num) for num in re.findall(r"n\^(.*?)\+",s)]
# print("n^"+str(max(nums)))

#遍历整个str，讨论
# s = input()+"+"
# maxn = 0
# tmp_sum = 0
# is_exponent = False #是否在指数中，因为系数也是数字，而且不一定有系数（1）
# is_zero = False #系数是否为0
# for i in range(len(s)):
#     c = s[i]
#     if c == '+':#结算前一项
#         if not is_zero:
#             maxn = max(maxn,tmp_sum)
#         tmp_sum = 0
#         is_exponent = False
#         is_zero = False
#     elif c == 'n' or c == '^': #跳过^就行
#         is_exponent = True
#     elif not is_exponent:#系数
#         if c == '0' and s[i-1] == '+':
#             is_zero = True
#     else:#指数
#         tmp_sum = tmp_sum*10 + int(c)
# print("n^

#决战双十一 http://cs101.openjudge.cn/20221103mockexam/E23566/
#先满减，再用券
# n,m = [int(x) for x in input().split()]
# shop = [[] for i in range(m)]#m家店铺的商品价格
# for i in range(n):
#     si,pi = [int(x) for x in input().split()]
#     shop[si-1].append(pi)
# #计算m家店各自总价
# price = [sum(x) for x in shop]
# #先满减
# answer = sum(price)
# answer = answer - answer//200*30
# #计算m家店各自的优惠
# for i in range(m):
#     tot,less = [int(x) for x in input().split('-')]
#     if price[i] >= tot:
#         answer -= less
# print(answer)

#因材施教 http://cs101.openjudge.cn/20221103mockexam/H19948/
#差异有n-m个相邻差异组成
# n,m = [int(x) for x in input().split()]
# stu = [int(x) for x in input().split()]
# stu.sort()
# diff = [stu[i]-stu[i-1] for i in range(1,len(stu))]
# diff.sort()
# print(sum(diff[:n-m]))

#贪心？

#生日相同 http://cs101.openjudge.cn/20221103mockexam/M25301/
# birth_dict = {}#"3-2":[00508192]
# n = int(input())
# for i in range(n):
#     id,month,day = input().split()
#     birth = month+"-"+day
#     if birth not in birth_dict.keys():
#         birth_dict[birth] = [id]
#     else:
#         birth_dict[birth].append(id)

# #对birth进行排序，从前往后
# births = list(birth_dict.keys())

# def f(x):
#     return [int(i) for i in x.split('-')]

# births.sort(key = f)

# for key in births:
#     value = birth_dict[key]
#     if len(value) > 1:
#         for k in key.split('-'):
#             print(int(k),end=' ')
#         for v in value:
#             print(v,end=' ')
#         print()

#最大并发量 http://cs101.openjudge.cn/20221103mockexam/M25302/
#对每个事件刻度设置一个值，因为连接范围太大，数组过大，不行
# t = int(input())
# for ti in range(t):
#     n = int(input())
#     load = [0]*int(1e3)
#     for i in range(n):
#         s,e = [int(x) for x in input().split()]
#         for j in range(s,e):
#             load[j] += 1
#     print(max(load))

#对连接按开始时间排序，遍历所有连接的开始时间，用alive存存活的连接id
# t = int(input())
# for ti in range(t):
#     n = int(input())
#     link = []
#     for i in range(n):
#         link.append([int(x) for x in input().split()])
#     link.sort(key = lambda x:(x[0],x[1]))
#     alive = [link[0]]
#     maxn = 0
#     for i in range(1,n):
#         now = link[i][0]
#         delete = []
#         for al in alive:
#             if al[1] <= now:#已经断开
#                 # alive.remove(al)
#                 delete.append(al)
#             # else: 不行
#             #     break #因为是按照开始时间排序的
#         for d in delete:
#             alive.remove(d)
#         alive.append(link[i])    
#         maxn = max(maxn,len(alive))
#     print(maxn)

# Number Game https://codeforces.com/problemset/problem/1749/C
t = int(input())
for ti in range(t):
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    for k in range(n, -1, -1):
        if all(k - 1 + i < n and a[k - 1 + i] <= i + 1 for i in range(k)):
            print(k)
            break

    