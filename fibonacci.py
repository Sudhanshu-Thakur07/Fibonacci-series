          #fibonacci series
n = int(input("enter no. of terms:\n"))
a = int(input("enter first term of series:\n"))
b = int(input("enter second term of series:\n"))
l =[a,b]
for i in range (2,n):
    x = l[i-2] +l[i-1]
    l.append(x)
print("your fibonacci series is here :",l)