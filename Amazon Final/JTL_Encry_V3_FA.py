import random
def ran(x):
 s=random.randint(1,3)
 r=random.randint(-20,20)
 while r<10 and r>-10:
  r=random.randint(-20,20)
 if s==1:
  return(x+r,r,s)
 if s==2:
  return(x-r,r,s)
 if s==3:
  return(x*r,r,s)
def encry(x):
 f=""
 for g in x:
  a,n,si=ran(ord(g))
  f+=str(a)+"^"+str(n)+str(si)+" "
 return(f)
