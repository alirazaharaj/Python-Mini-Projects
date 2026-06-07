# import os
# # Problem 1
# user= int(input('Enter a number :'))
# print(user**2)

# # Problem 2
# user=input('Enter a string: ')
# print(user[::-1])

# # Problem 3
# user=[]
# n=0
# userr= int(input('Enter a list length :'))
# for i in range(0,userr):
#     us=int(input('Enter number: '))
#     user.append(us)
# sum=0
# for i in user:
#     sum+=i
# os.system('cls')
# print('Sum of list will be ',sum)

# # Problem 4
# user= int(input('Enter a number :'))
# if (user%2==0)|(user%3==0)|(user%5==0):
#     print('Other number......')
# else:
#     print('Prime number......')

# # Problem 5
# user=input('Enter a string: ')
# print(user.upper())

# # Problem 6
# user=[]
# n=0
# userr= int(input('Enter a list length :'))
# for i in range(0,userr):
#     us=int(input('Enter number: '))
#     user.append(us)
# sum=0
# for i in user:
#     sum+=i
# os.system('cls')
# print('Average of list will be ',sum/len(user))

# # Proble 7
# n= int(input('Enter a number whosenfactorial you want to calculate: '))
# user+=1
# fac=1
# for i in range(1,user):
#     fac*=i
# print("Factorial will be ",fac)

# # Problem 8
# user =input('Enter a string: ')
# print(len('Length of given string will be ',user))

# # Problem 9
# user=[]
# userr= int(input('Enter a list length :'))
# for i in range(0,userr):
#     us=int(input('Enter number: '))
#     user.append(us)
# max=0
# min=10000
# for i in user:
#     if (max<i):
#         max=i
#     if (min>i):
#         min=i
# print(f'Minimum value in list will be {min} and max value will be {max}')

# # Problem 10 
# user= int(input('Enter a list length :'))
# for i in range(1,11):
#     print(f'{user}*{i}={user*i}')

# # Problem 11
# user=input('Enter a string: ')
# print("".join(sorted(user)))

## Problem 12
# user=[];even=[];odd=[]
# userr= int(input('Enter a list length :'))
# for i in range(0,userr):
#     us=int(input('Enter number: '))
#     user.append(us)
# for i in user:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print('Even List....')
# for i in even:
#     print(i)
# print('Odd List....')
# for i in odd:
#     print(i)
