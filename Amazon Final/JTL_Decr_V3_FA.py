def decr(s,sign,ad):
 ad=ad[:len(ad)-2]
 if sign==1:
  return(chr(int(s)-int(ad)))
 if sign==2:
  return(chr(int(s)+int(ad)))
 if sign==3:
  return(chr(int(s)//int(ad)))
def decrypt(x):
 x+=" "
 s=""
 ad=""
 n=0 
 f=""
 for g in x:
  if g=="^":
   n=1
  elif n==0:
   s+=g
  elif n==1:
   ad+=g
   if g==" ":
    n=0
    sign=int(ad[-2])
    d=decr(s,sign,ad)
    f+=str(d)
    s=""
    ad=""
 return(f)
