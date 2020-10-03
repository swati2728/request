# (print max and mini from the list)

# list1=[1,6,7,9]
# i=0
# max1=0
# min1=list1[i]
# while i<len(list1):
#     if list1[i]>max1: 
#         max1=list1[i] 
#     # if list1[i]<min1:
#     #     min1=list1[i]
#     i=i+1
# print("maximum is",max1)  
# print("minimum is",min1)

# (mistake was i  was doing )
 
# list1=[1,6,7,9]
# i=0
# max1=0
# min1=0
# while i<len(list1):
#     j=0
#     while j<len(list1):
#         if list1[i]>max1: 
#             max1=list1[i] 
#         if list1[i]<min1:
#             min1=list1[i]
#         j=j+1
#     i=i+1
# print("maximum is",max1)  
# print("minimum is",min1)

# (print the list,index of the list,typ of the list and print the numbers whixh are old and even from the list)

# var=[1,2,3,4,5,6]
# print(var)
# print(type(var))
# print(var[0]) 
# index=0
# while index<len(var):
#     if index%2==0:
#        print(index)
#     index=index+1   

# prime_numbers=[1,2,3,4,5,6,7,8,9,10]
# new_list=[]
# i=0
# while i < len(prime_numbers):
#     j=0
#     while j<len(prime_numbers):
#         if prime_numbers[i]

# sum of the list

# student_marks = [23, 45, 89, 90, 56, 80] 
# i=0
# sum=0
# while i<len(student_marks):
#     sum=sum+student_marks[i]
#     i=i+1
# print(sum)    

# ount of the list which are more and less than the 50

# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# index=0
# more_than=0
# less_than=0
# count1=0
# count2=0
# while index<len(student_marks):
#     if student_marks[index]<50:
#         less_than=less_than+1    
#         count1+=1
#     if student_marks[index]>50:
#         more_than=more_than+1
#         count2+=1
#     index=index+1
# print("total less than 50 are:",count1)    
# print("total more than 50 are:",count2)



# split=input("enter a word:")
# string=""
# new_list=[]
# i=0
# while i<len(split):
#     b=split+string
#     new_list.append(b[i])
#     i=i+1
# print(new_list)    

# split=input("enter a word:")
# new_list=[]
# string=''
# i=0
# while i<len(split):
#     if split[i]==' ':
#         new_list.append(string)
#         string=''
#     else:
#         string+=split[i]
#     i=i+1
# new_list.append(string)
# print(new_list)


# user=["i","am","swati"]
# length=len(user)
# string=''
# index=0
# # new=[]
# while index<len(user):      
#     if index<length-1:
#         string=string+user[index]+"-"
#     else:
#         string=string+user[index]
#     # new.append(string)
#     index=index+1
# print(string)

# numbers=[[1,2,3,5,22],
#         [4,50,4,66],
#         [7,8,9,6]]
# sum=0
# index=0
# new=[]
# # new2=[]
# while index<len(numbers):
#     j=0
#     while j<len(numbers[index]):
#         s = numbers[index][j] 
#         if s >= 4:
#             new.append(s)
#         j+=1
#     index=index+1
# i=0
# while i<len(new):
#     sum=sum+new[i]
#     # if sum>100:
#     #     print(sum,"it grether than 100")
#     # else:
#     #     print(sum,"it is not grether")
#     i=i+1
# print(new) 
# print(sum)
# if sum>100:
#     print(sum,"it grether than 100")
# else:
#     print(sum,"it is not grether")

# # print(new2)              

# numbers=[[1,2,3,5,22],
#         [4,50,4,66],
#         [7,8,9,6]]
# sum=0
# index=0
# while index<len(numbers):
#     j=0
#     while j<len(numbers[index]):
#         s = numbers[index][j] 
#         if s >= 4:
#            sum=sum+s
#         j=j+1
#     index=index+1
# print(sum)
# if sum>100:
#     print(sum,"it grether than 100")
# else:
#     print(sum,"it is not grether")

# num = int(input("Enter a number: "))  
# def prime():  
#     if num > 1:  
#         for i in range(2,num):  
#             if (num % i) == 0:  
#                 print(num,"is not a prime number") 
#                 break  
#         else:  
#             print(num,"is a prime number")  
                
#     else:  
#         print(num,"is not a prime number")  
# prime()


# new=[1,5,2,6,7,8,9]
# i=0
# while i<len(new):
#     if new[i] > 1:  

#         for j in range(2,new[i]):  
#             if (new[i] % j) == 0:  
#                 print(new[i],"is not a prime number") 
#                 break  
#         else:  
#             print(new[i],"is a prime number")  
                
#     else:  
#         print(new[i],"is not a prime number") 
#     i=i+1


# num = int(input("Enter a number:"))  
# i=0
# while i<num:
#     if i>1:
#         for z in range(2,i):
#             if i%z==0:
#                 break
#         else:
#             print(i) 
#     i=i+1        


# num=30
# sum=0
# while num>1:
#     sum=sum+num
#     num-=1
# print(sum)    

# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print(sum)     



 
# def my_function():
#     if 4>5:
#         print("bada hai")
#     else:
#         print("chotha hai")
# my_function()
    

# a=[1,2,3,4,5]
# max=0
# i=0
# min=a[i]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     if a[i]<min:
#         min=a[i]
#     i=i+1
# print(max)  
# print(min)      

new_list=[[0,1,0],
        [0,1,0],
        [1,2,1]]
index=0
zero=0
sum=0
while index<len(new_list):
    j=0
    while j<len(new_list):
        sum=new_list[index][j]==new_list[1][0]
        sum=sum+1
        j=j+1
    index=index+1
print(sum)           



