# list =[]
# for number in range(1500,2701):
#     if number%5==0 and number %7==0:
#         list.append(number)

# for  number in list:
#     print(number)
# # 2nd program

# def celcius_TO_F(celcius):
#     F=(celcius*9/5)+32
#     return F
# celcius=float(input("enter Celcius"))
# print(celcius_TO_F(celcius))

# def F_TO_Celcius(F):
#     return (F-32)*5/9
# Foenight=float(input("enter Frenghit:"))
# print(f"Foreign to celcius:{Foenight:.2f}  {F_TO_Celcius(Foenight):.1f}")

# # 3 Q
# import random
# num=int(input("Enter guess:"))
# guess_Target=random.randint(1, 9)

# while True:
#     if num==guess_Target:
#         print("Well guess")
#         break
#     else :
#         print("guess again!")
#         num=int(input("Enter guess:"))


# 4 Q
# # 5Q
# def reverse(inpute):
#     return inpute[::-1]
# inpute=input("Enter a string:")
# print(reverse(inpute))

# number=(1,2,3,4,5,6,7,8,9)
# even_Count=0
# odd_Cont=0
# for i in number:
#     if i%2==0:
#         even_Count+=1
#     else :
#         odd_Cont+=1
# print(f"Even counts: {even_Count} \n ans odd Count: {odd_Cont}")
# # 7Q
# dataList=[1452,11.23,1+2j,True,'w3school',(0,1),[5,12],{"class":"V","section":'A'}]
# for i in dataList:
#     print(f"{i} - {type(i)} ")

# for i in range(0,7):
#     if i==3 or i==6:
#         continue
#     else:
#        print(i,end=" ")
# def fibonacci_fizzbuzz(n):
#     a,b=0,1
#     while a <= n:
#         if a % 15 == 0:
#             print("FizzBuzz")
#         elif a % 3 == 0:
#             print("Fizz")
#         elif a % 5 == 0:
#             print("Buzz")
#         else:
#           print(a)
#         a,b=b,a+b

# # Generate Fibonacci series up to 50
# fibonacci_fizzbuzz(50)

# 2D array
# def Two_D_array(n,m):
#   array=[]
#   for i in range(n):
#     row=[]
#     for j in range(m):
#       row.append(i*j)
#     array.append(row)
#   return array

# array=Two_D_array(3,4)
# for i in array:
#   print(i,end=" ")

# # blank lines
# lines=[]
# print("\nËnter line")
# while True:
#   line=input()
#   if line:
#     lines.append(line.lower())
#   else:
#     break


 
# print(','.join(lines))
# import re
# def valid_password(password):
#    if len(password )>=6:
#         if re.search('[A-Z]',password) and re.search('[a-z]',password) and re.search('[0-9]',password) and re.search('[$#@]',password):
#            return True
#         else : return False
#    else: 
#        return False

# print("Enter password")
# password=input()
# if valid_password(password):
#     print("Correct")
# else: print("Not correct")
# import re
# inpute=input("Enter a string:")
# letters=0
# digits=0
# for i in inpute:
#     if re.search('[A-Z]',i) or re.search("[a-z]",i):
#         letters+=1
#     elif re.search('[0-9]',i):
#         digits+=1
# print(f"digits: {digits} letters:{letters}")
# Accepts a sequence of binary numbers and prints those divisible by 5
# list=input("Ënter comma seprated value:").split(',')
# binaryarray=[]
# for i in list:
#     if int(i,2)%5==0:
#         binaryarray.append(i)
# for i in binaryarray:
#  print(i)



class Stack:
   def __init__(self) :
      self.data=[]
   def push(self,data):
    
      self.data.append(data)
   def pop(self):
      if not self.is_empty :
         return self.data.pop()
      else: return "Stack is empty"
   def is_empty(self):
       return len(self.data)==0
         
   def display(self):
        for i in range(len(self.data)):  # Loop from 0 to len(self.data) - 1
            print(self.data[i])  # Access the data using self.dat
   def  peeK(self):
      if not self.is_empty:
         return self.data[-1]
      else : return "Stack empty"
stack1 =Stack()
stack1.push(12)
stack1.push(13)
stack1.display()
print(stack1.peeK())
print(stack1.pop())

#Lab4
#Question1
# class Stack:
#     def __init__(self):
#         self.items = []
    
#     def push(self, item):
#         self.items.append(item)
    
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             return "Stack is empty"
    
#     def is_empty(self):
#         return len(self.items) == 0
    
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             return "Stack is empty"

#     def size(self):
#         return len(self.items)
# # Example usage
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop()) 
# print(stack.peek()) 
# print(stack.is_empty()) 

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print(" ")
    
for i in range(6,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print(" ")
    