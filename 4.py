#A. Word Capitalization https://codeforces.com/problemset/problem/281/A
# s = input()
# if s[0].lower() == s[0]:
#     print(chr(ord(s[0])-32)+s[1:])
# else:
#     print(s)

#A. Boy or Girl https://codeforces.com/problemset/problem/236/A
# s = list(input())
# lis = set(s)
# if len(lis)%2 == 0:
#     print('CHAT WITH HER!')
# else:
#     print('IGNORE HIM!')

#A. String Task https://codeforces.com/problemset/problem/118/A
# s = list(input())
# lis = []
# for x in s:
#     x = x.lower()
#     if x not in ['a','o','y','e','u','i']:
#         lis.append(x)
# print("."+".".join(lis))

#19944:这一天星期几v0.3(math) http://cs101.openjudge.cn/practice/19944/
#重复用的list不需要每次循环都初始化一遍
# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# for i in range(int(input())):
#     a = input()
#     c = int(a[0:2])
#     y = int(a[2:4])
#     m = int(a[4:6])
#     d = int(a[6:])

#     #处理特殊情况
#     if m <= 2:
#         m += 12
#         if y == 0:
#             c -= 1
#             y = 99
#         else:
#             y -= 1
#     #套公式
#     w = y + y // 4 + c // 4 - 2*c + (26 * (m + 1)) // 10 + d - 1
#     w = w % 7
#     print(days[w])

#04015:邮箱验证 http://cs101.openjudge.cn/practice/04015/
while(1):
    try:
        s = input()
    except:
        break
    if s.count('@') > 1:
        print('NO')
    elif s[0]=='@' or s[0]=='.' or s[-1]=='@' or s[-1]=='.':
        print('NO')
    elif s[s.find('@'):].count('.')<1 or s.find('.@')!=-1 or s.find('@.')!=-1:
        print('NO')
    else:
        print('YES')
