#Count frequency of elements---------------------------------------------------------------------------
# numbers = [0,1, 2, 2, 3, 1, 2]
# fre={}
# for n in numbers:
#     fre[n]=fre.get(n,0)+1
# print(fre)

#Find even numbers------------------------------------------------------------------------------------------
# numbers = [1, 2, 3, 4, 5, 6]
# print(res:=[n for n in numbers if n%2==0])

#Swap two variables-------------------------------------------------------------------------------------------
# a=10
# b=20
# a,b=b,a
# print(f"a : {a}\nb : {b}")

# Factorial-------------------------------------------------------------------------------------------
# n=3
# res=1
# for i in range(n,0,-1):
#     res*=i
# print(res)

# Find second largest-------------------------------------------------------------------------------------------
# numbers = [10, 20, 5, 30, 25]
# remove_duplicates=list(set(numbers))
# remove_duplicates.sort()
# print(remove_duplicates[-2])

# Sum of numbers in a list---------------------------------------------------------------------------------------------
# numbers = [10, 20, 5, 30, 25]
# # print(res:=sum(numbers))
# res=0;
# for i in numbers:
#     res+=i
# print(res)

# Sum of even numbers in a list---------------------------------------------------------------------------------------------
# numbers = [10, 20, 5, 30, 25]
# res=0
# for n in numbers:
#     if n%2==0:
#         res+=n
# print(res)

# Count how many digits are present in 12345---------------------------------------------------------------------------------------
# num = 12345
# count = 0

# while num > 0:
#     count += 1
#     num //= 10

# print(count)
# Reverse a number---------------------------------------------------------------------------------------------------------------
# num=12345
# rev=0
# while(num>0):
#     rev=rev*10
#     rev+=num%10
#     num//=10
# print(rev)

# Palindrome Number---------------------------------------------------------------------------------------------------------------------------------------------------
# num=125219
# rev=0
# temp=num
# while(temp>0):
#     rev*=10
#     rev+=temp%10
#     temp//=10
# print("yes palindrome") if rev==num else print("not a palindrome")

# Find the Most Frequent Element--------------------------------------------------------------------------------------------------------------------------------------------------
# numbers = [1, 2, 2, 3, 1, 2, 4, 3]
# maxrepKey=0
# maxrepValue=0
# fre={}
# for n in numbers:
#     fre[n]=fre.get(n,0)+1
# for k,v in fre.items():
#     if v>maxrepValue:
#         maxrepValue=v
#         maxrepKey=k
# print("most frequent ele is : ",maxrepKey)

# Check Anagram (same characters with the same frequency)--------------------------------------------------------------------------------------------------
# s1 = "listen"
# s2 = "silent"
# fre1={}
# fre2={}
# flag=0
# for i in s1:
#     fre1[i]=fre1.get(i,0)+1
# for i in s2:
#     fre2[i]=fre2.get(i,0)+1
# # for i in fre1.keys():
# #     if (i not in fre2.keys()) or (fre2.get(i)!=fre1.get(i)):
# #         #print("no")
# #         flag=1
# #         break
# #dictionaries can be compared by their keys and values regardless of insertion order
# # if(flag):
# #     print("NO")
# # else:
# #     print("yes")

# print("yes") if fre1==fre2 else print("no")

# First Non-Repeating Character----------------------------------------------------------------------------------------------------------------
# s = "azabbcde"
# fre={}
# flag=0
# for i in s:
#     fre[i]=fre.get(i,0)+1
# for k,v in fre.items():
#     if v==1:
#         print("first non repeating ele :",k)
#         flag=1
#         break
# if not flag :
#    print("no non repeating eles")

# Find duplicate characters---------------------------------------------------------------------------------------------
# s = "programming"
# fre={}
# for i in s:
#      fre[i]=fre.get(i,0)+1
# print(lis1:=[k for k,v in fre.items() if v>1])

# Find the Missing Number-------------------------------------------------------------------------------------------------------
# numbers = [1, 2, 3, 4, 6]
# n=numbers[-1]
# t=0
# sumOflist=sum(numbers)
# while(n>0):
#     t+=n
#     n-=1
# print("missing num is : ",(t-sumOflist))

# Find Common Elements in Two Lists-----------------------------------------------------------------------------------------------
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# print(res:=[ e for e in list1 if e in list2])

# Second Most Frequent Element----------------------------------------------------------------------------------------------------------
# numbers = [1, 2, 2, 3, 3, 4, 4]
# fre={}
# res=[]
# firstv=0
# firstk=numbers[0]
# secondk=0
# secondv=0
# for i in numbers:
#     fre[i]=fre.get(i,0)+1
# for k,v in fre.items():
#     if v>fre.get(firstk):
#         secondk=firstk
#         firstk=k
#     elif v!=fre.get(firstk) and v>fre.get(secondk):
#         secondk=k
        
# print("Second Most Frequent Element is : ",secondk)

# Find the Longest Word---------------------------------------------------------------------------------------------------------
# sentence = "Python is very powerful"
# lis=sentence.split()
# longest=""
# for i in lis:
#     if len(longest)<len(i):
#         longest=i
# print(longest)

# Reverse Words in a Sentence------------------------------------------------------------------------------------------------------
# sentence = "Python is very powerful"
# lis=sentence.split()
# lis.reverse()
# print(" ".join(lis))

# Reverse a String Without [::-1]------------------------------------------------------------------------------------------------------------
# s = "python"
# rev=""
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
#     #print(i)
# print(rev)






    






    