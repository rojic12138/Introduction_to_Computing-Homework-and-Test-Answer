#Ants http://cs101.openjudge.cn/20221201mockexam/E01852/
#相遇之后的1s交换位置，相当于没有相遇
# n = int(input())
# for i in range(n):
#     length,number = [int(x) for x in input().split()]
#     ants = [int(x) for x in input().split()]
#     max_ans = 0
#     min_ans = 0
#     for i in range(number):
#         max_ans = max([max_ans,ants[i],length-ants[i]])
#         min_ans = max([min_ans,min(ants[i],length-ants[i])])
#     print(min_ans,max_ans)

#计算鞍点 http://cs101.openjudge.cn/20221201mockexam/E03670/
# table = []
# for i in range(5):
#     table.append([int(x) for x in input().split()])
# flag_table = [] #flag=2表示鞍点
# for i in range(5):
#     flag_table.append([0]*5)
# #行
# for i in range(5):
#     index = table[i].index(max(table[i]))
#     flag_table[i][index] += 1
# #列
# for i in range(5):
#     col = [table[j][i] for j in range(5)]
#     index = col.index(min(col)) 
#     flag_table[index][i] += 1
# flag = False
# for i in range(5):
#     for j in range(5):
#         if flag_table[i][j] == 2:
#             print(i+1,j+1,table[i][j])
#             flag = True
# if not flag:
#     print ('not found')

#滑雪 http://cs101.openjudge.cn/20221201mockexam/H01088/
#经典dfs
# r,c = [int(x) for x in input().split()]
# table = []
# for i in range(r):
#     table.append([int(x) for x in input().split()])
# vis = [[0]*len(table[0]) for i in range(len(table))]#vis[i,j]!=0表示i,j处已被搜过

# def dfs(i,j):
#     #从i，j处开始滑的最长距离
#     if vis[i][j]:
#         return vis[i][j]
#     ans = 1
#     if i>0 and table[i][j]>table[i-1][j]:
#         ans = max(ans,dfs(i-1,j)+1)
#     if i<r-1 and table[i][j]>table[i+1][j]:
#         ans = max(ans,dfs(i+1,j)+1)
#     if j>0 and table[i][j]>table[i][j-1]:
#         ans = max(ans,dfs(i,j-1)+1)
#     if j<c-1 and table[i][j]>table[i][j+1]:
#         ans = max(ans,dfs(i,j+1)+1)
#     vis[i][j] = ans
#     return ans

# for i in range(r):
#     for j in range(c):
#         dfs(i,j)
# print(max([max(vis[i]) for i in range(r)]))
 
#月度开销 http://cs101.openjudge.cn/20221201mockexam/H04135/
#二维背包，MLE
# n,m = [int(x) for x in input().split()]
# num = []
# for i in range(n):
#     num.append(int(input()))
# #dp[i][j]:i天，用j个财政月
# dp = [[max(num)+1]*m for i in range(n)]
# #边界条件
# dp[0][0] = num[0]
# for i in range(1,m):
#     dp[i][i] = max(num[i],dp[i-1][i-1])
# for i in range(n):
#     dp[i][0] = sum(num[:i+1])
# for i in range(n):
#     for j in range(min(i,m)):
#         for k in range(j,i):#k表示上一个财政月的最后一天
#             dp[i][j] = min(dp[i][j],max(sum(num[k+1:i+1]),dp[k][j-1]))
# print(dp[n-1][m-1])

#找每个月的开销为expense时是否可以，如果可以就减少expense，否则增加expense。通过二分来找expense。
# n,m = [int(x) for x in input().split()]
# nums = []
# for i in range(n):
#     nums.append(int(input()))
# def check(expense):
#     #expense：开销上限
#     fajo_num = 1
#     expense_sum = 0
#     for num in nums:
#         if num > expense: #一个月的开销就高于开销上限
#             return False
#         if num + expense_sum <= expense: #加到前一个fajo月
#             expense_sum += num
#         else: #新的fajo月
#             fajo_num += 1
#             expense_sum = num
#             if fajo_num > m:
#                 return False
#     return True

# #用二分搜索的方法找expense
# left, right,res = 0,1e6,0
# while(left <= right):
#     mid = (left+right)//2
#     if check(mid):
#         res = mid
#         right = mid -1
#     else:
#         left = mid + 1
# print(int(res))

#阿尔法星人翻译官 http://cs101.openjudge.cn/20221201mockexam/M12757/
words = input().split()
if words[0] == 'negative':
    negative = -1
    del words[0]
else:
    negative = 1

dic = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5,
 "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "eleven":11, 
 "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16,
  "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "thirty":30,
  "ninety":90, "hundred":100, "thousand":1000, "million":1000000}
# unit = ["hundred", "thousand", "million"]
unit = ["hundred"]

#将words按million,thousand分成三部分
million,thousand = [],[]
if "million" in words:
    million,words = words[:words.index("million")],words[words.index("million")+1:]
if "thousand" in words:
    thousand,words = words[:words.index("thousand")],words[words.index("thousand")+1:]
ans = 0
parts = [million,thousand,words]
multiple = [1000000,1000,1]
for i in range(3):
    part_sum = 0
    for word in parts[i]:
        if word in unit:
            part_sum *= dic[word]
        else:
            part_sum += dic[word]
    ans += part_sum*multiple[i]
print(negative*ans)