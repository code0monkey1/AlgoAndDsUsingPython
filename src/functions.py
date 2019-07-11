
def my_sqrt(number):
 if number==0:
     return 0
 root=number/2

 for i in range(20):
     root=(1/2)*(root+number/root)
 return root

ans=my_sqrt(5)

print("The value is %.2f and the longer anser is %f "%(ans,ans))