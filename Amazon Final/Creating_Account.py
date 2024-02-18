import mysql.connector as mssign
from Filter import *
from JTL_Encry_V3_FA import *
sqsign=mssign.connect(user="root",host="localhost",password="Arduino1")
csign=sqsign.cursor()
csign.execute("use amazon")   
def signin(mails,banned):
 name=input("Enter Your Name ")
 name=af(name)
 if len(name)>3 and len(name)<30:
  password=input("Enter Your Password (All Special Symbols Would Be Removed) ")
  password=af(password)
  if len(password)>3 and len(password)<11:
   passe=encry(password)
   email=input("Enter Your Mail Id ")
   if (email,) not in mails and (email,) not in banned:
    if len(email)>5 and len(email)<50:
     s="Insert Into Users_list (name,password,email) Values('{}','{}','{}')".format(name,passe,email)
     return(s,name,passe,email)   
     print("\nAccount Has Been Succesfully Created")
    else:
     print("\nMail Must Atleast Be 6 Characters And Below 50 Characters")
   else:
    if (email,) in mails:  
     print("\nThis Email Id Is Being Used By Anther Account Please Enter Anther Email Id")   
    else:
     print("You Cannot Create A Account With This Mail As This Mail Id Has Been Banned")
  else:
   print("\nPassword Must Atleast Be 4 Characters And Below 10 Characters")
 else:
  print("\nName Must Be Over 3 Characters And Below 30 Characters")   
 return("0",0,0,0)
