#A. Watermelon
# """偶数而且不为2
# """
# n=int(input())
# if n!=2 and n%2==0:
#     print('YES')
# else:
#     print('NO')

#A. Way Too Long Words
# n=int(input())
# for i in range(n):
#     s=input()
#     if len(s) <= 10:
#         print(s)
#     else:
#         print(s[0]+str(len(s)-2)+s[-1])

#02750:鸡兔同笼
# a=int(input())
# if a%2 == 1:
#     print(0,0)
# else:
#     min_num=int(a//4+(a%4)/2)
#     max_num=int(a/2)
#     print(min_num,max_num)

#02733:判断闰年
#a -> Y,N 
year=int(input())
if(year%4 == 0): 
    if year%100 == 0 and year%400 != 0: #or, not bool, not True->False
        print('N')
    elif year%3200 == 0:
        print('N')
    else:
        print('Y')
else:
    print('N')