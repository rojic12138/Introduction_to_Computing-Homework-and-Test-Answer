#A. Team https://codeforces.com/problemset/problem/231/A
# n = int(input())
# result = 0
# for i in range(n):
#     line = [int(x) for x in input().split()]
#     if(sum(line) >= 2):
#         result += 1
# print(result)

#A. Theatre Square https://codeforces.com/problemset/problem/1/A
# n,m,a = [int(x) for x in input().split()]
# x,y = n/a,m/a
# if(x != int(x)):
#     x = int(x)+1 
# if(y != int(y)):
#     y = int(y)+1 
# print(int(x*y))

#A. Next Round https://codeforces.com/problemset/problem/158/A
# n,k = [int(x) for x in input().split()]
# marks = [int(x) for x in input().split()]
# result = 0
# for i in range(n):
#     if(marks[i] <= 0):
#         break
#     elif(i == k-1):
#         for j in range(i,n):
#             if(marks[j] == marks[i]):
#                 result += 1
#             else:
#                 break
#         break
#     else:
#         result +=1
# print(result)
    
#A. Domino piling https://codeforces.com/problemset/problem/50/A
# m,n = [int(x) for x in input().split()]
# if m%2 == 0 or n%2 ==0:
#     result = m*n/2
# else:
#     result = (m-1)*(n-1)/2+(m-1)/2+(n-1)/2
# print(int(result))

