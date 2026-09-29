# print("============Generators ====================")
# def my_generator1(n):
#     count=0
#     while count<=n:
#         yield count
#         count+=1
# for val in my_generator1(10):
#     print(val)
#--------------------------------------------------------------------------------------------------
# def is_prime(n):
#     if n==1 or n<=0:
#         return "not a prime"
#     for i in range(2,(n//2)+1,1):
#         if n%i==0:
#             return "not a prime"
#     return "yes it is prime"
# print(is_prime(1))

#---------Factorial Using a Function-----------------------------------------------------------------------------------------------
# def factorial(n):
#     fact=1
#     if n==0 or n==1:
#         return 1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# print(factorial(5))

#-------------Fibonacci Series------------------------------------------------------------------------
def fibonacci(n):
    f1=0
    f2=1
    while(n>0)
