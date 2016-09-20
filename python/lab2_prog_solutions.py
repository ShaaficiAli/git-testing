import math 
def repeater(s1,s2,n):
    String=str(s1+s2)*n
    print("_"+String+"_")
    
def roots(a,b,c):
    root1=-b+math.sqrt(b**2-4*a*c)
    root2=-b+math.sqrt(b**2-4*a*c)
    print("The quadratic equation with coefficients a =",a,"b =",b,"c =",c,"has the following solutions (i.e. roots):\n",root1,"and",root2)
def real_roots(a,b,c):
    number=b**2-4*a*c
    if(number>=0):
        return True
    else:
        return False
def reverse(x):
    n =(x%10)*10 + (x//10)
    return n

