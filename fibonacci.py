n=int(input("Enter the no of terms:"))
n1,n2=0,1
print("Fibonacci series:")
print(n1)
print(n2)
for i in range(2,n):
    t=n1+n2
    n1=n2
    n2=t
    print(t)


n=int(input("Enter the no of terms:"))
n1,n2=0,1
print("Fibonacci series:")
print(n1)
print(n2)
i=2
while i<n:
    t=n1+n2
    n1=n2
    n2=t
    print(t)
    i+=1
