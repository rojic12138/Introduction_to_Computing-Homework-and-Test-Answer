#A. IQ test https://codeforces.com/problemset/problem/25/A
# n = int(input())
# nums = [int(x) for x in input().split()]
# evens= []
# for i in range(n):
#     nums[i] = nums[i]%2
#     evens.append(nums[i])
# if sum(evens) == n-1:
#     #全奇数
#     print(nums.index(0)+1)
# else:
#     #全偶数
#     print(nums.index(1)+1)

#A. Bulbs https://codeforces.com/contest/615/problem/A
# n,m = [int(x) for x in input().split()]
# bulbs = [True for i in range(m+1)]
# for i in range(n):
#     num,*ids = [int(x) for x in input().split()]
#     for id in ids:
#         bulbs[id] = False
# if sum(bulbs) == 1:
#     print('YES')
# else:
#     print('NO')

#A: The New Year: Meeting Friends https://codeforces.com/problemset/problem/723/A
# a = [int(x) for x in input().split()]
# a.sort()
# print(a[2]-a[0])

#A. Hulk https://codeforces.com/problemset/problem/705/A
# n = int(input())
# if n%2 == 1:
#     s = 'I hate it'
#     for i in range(1,n):
#         if i%2 == 0:
#             s = "I hate that "+s
#         else:
#             s = "I love that "+s
# else:
#     s = 'I love it'
#     for i in range(1,n):
#         if i%2 == 0:
#             s = "I love that "+s
#         else:
#             s = "I hate that "+s
# print(s)

#B. Drinks https://codeforces.com/problemset/problem/200/B
# n = int(input())
# a = [int(x) for x in input().split()]
# print(sum(a)/len(a))

#A. 2048 Game https://codeforces.com/problemset/problem/1221/A
# times = int(input())
# for t in range(times):
#     n = int(input())
#     nums = [int(x) for x in input().split()]
#     nums = [x for x in nums if x<=2048]
#     if sum(nums) >= 2048:
#         print('YES')
#     else:
#         print('NO')

#A. Fancy Fence
times = int(input())
for t in range(times):
    angle = int(input())
    if ((180-angle)/360)**-1 == int(((180-angle)/360)**-1):
        print('YES')
    else:
        print('NO')