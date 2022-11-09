#A. Stones on the Table https://codeforces.com/problemset/problem/266/A
#和前一个一样就移走
# n = int(input())
# s = input()
# last = s[0]
# tot = 0
# for i in range(1,n):
#     if s[i] == last:
#         tot += 1
#     else:
#         last = s[i]
# print(tot)

#A. Football https://codeforces.com/problemset/problem/96/A
# s = input()
# if "1"*7 in s or "0"*7 in s:
#     print('YES')
# else:
#     print('NO')

#A. Young Physicist https://codeforces.com/problemset/problem/69/A
# n = int(input())
# x,y,z = 0,0,0
# for i in range(n):
#     dx,dy,dz = [int(x) for x in input().split()]
#     x += dx
#     y += dy
#     z += dz
# if x == 0 and y == 0 and z == 0:
#     print('YES')
# else:
#     print('NO')

#A. Twins https://codeforces.com/problemset/problem/160/A
# n = int(input())
# coins = [int(x) for x in input().split()]
# coins.sort(reverse=True)
# tot = sum(coins)
# my = 0
# for i in range(n):
#     my += coins[i]
#     if my > tot/2:
#         ans = i+1
#         break
# print(ans)

#M1017:装箱问题 http://cs101.openjudge.cn/20221014mockexam/M1017/
"""
贪心法
0 0 4 0 0 1 
7 5 1 0 0 0 
0 0 0 0 0 0 
0 0 4 0 0 1 
7 5 1 0 0 0 
0 0 0 0 0 0 
"""
# while(True):
#     a,b,c,d,e,f = [int(x) for x in input().split()]
#     if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
#         break
#     ans = f
#     ans += e
#     a -= e*11
#     ans += d
#     b -= d*5
#     ans += c//4
#     if c//4 != c/4:
#         ans += 1
#         if c%4 == 1: 
#             b -= 5
#             a -= 7
#         elif c%4 == 2:
#             b -= 3
#             a -= 6
#         elif c%4 == 3:
#             b -= 1
#             a -= 5
#     if b < 0:
#         a -= -b*4
#     else:
#         ans += b//9
#         if b//9 != b/9:
#             ans += 1
#             a -= (36-b%9*4)
#     b = 0
#     if a > 0 :
#         ans += a//36
#         if a //36 != a/36:
#             ans += 1
#     print(ans)
        

#M2808:校门外的树 http://cs101.openjudge.cn/20221014mockexam/M2808/
#覆盖
# L,M = [int(x) for x in input().split()]
# flags = [True for i in range(L+1)]
# for i in range(M):
#     s,e = [int(x) for x in input().split()]
#     for j in range(s,e+1):
#         flags[j] = False
# print(flags.count(True))
list1 = []
list3 = {}
while True:
    try:
        list1.append(input())
    except EOFError:
        break
print("!")
for word in list1:
    list2 = []
    for aword in list1:
        if aword==word:
            continue
        for i in range(len(word)): #car-> abccar
            if word[:i + 1] != aword[:i + 1]:
                list2.append(i)
                break
    if len(list2) != 0:
        list3[word]=word[:max(list2)+1]
    else:
        list3[word]=word
    print(word,list3[word])

