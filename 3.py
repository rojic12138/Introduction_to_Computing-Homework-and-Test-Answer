#A. Bit++ https://codeforces.com/problemset/problem/282/A
#有+就加，否则减
# n = int(input())
# ans = 0
# for i in range(n):
#     s = input()
#     if s.find('+') != -1:
#         ans +=1 
#     else:
#         ans -=1
# print(ans)

#A. Beautiful Matrix https://codeforces.com/problemset/problem/263/A
# abs(x-2)+abs(y-2)
# for i in range(5):
#     s = input()
#     lis = s.split()
#     try:
#         a = lis.index('1')
#         ans = abs(i-2)+abs(lis.index('1')-2)
#     except:
#         pass
# print(ans)
            
#A. Petya and Strings https://codeforces.com/problemset/problem/112/A
# a = input().lower()
# b = input().lower()
# if a == b:
#     print(0)
# elif a > b:
#     print(1)
# elif a < b:
#     print(-1)

#A. Helpful Maths https://codeforces.com/problemset/problem/339/A
lis = input().split('+')
lis.sort()
res = ""
for x in lis:
    res += (x+'+')
print(res[:-1])

