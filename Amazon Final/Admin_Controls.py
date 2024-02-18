import mysql.connector as ms
from JTL_Encry_V3_FA import *
from JTL_Decr_V3_FA import *
sq=ms.connect(user="root",host="localhost",password="Arduino1")
def admincursor():
 a=sq.cursor()
 return(a)

def grantadmin(email,admins,banned,users):
 a=admincursor()
 a.execute("use Amazon")
 ademail=input("Enter Email Id Of The User ")
 if (ademail,) in users and (ademail,) not in banned:
  if (ademail,) not in admins:
   password=input("Enter Your Password ")
   a.execute("select password from users_list where email='{}'".format(email))
   correctpass=a.fetchone()
   decrpass=decrypt(correctpass[0])
   if password==decrpass:
    print("Do You Want To Confirm User",ademail,"As A Admin")
    cf=input("y/n ")
    if cf=="y":
      print("\nUser Has Been Made A Admin")
      return(1,ademail)
   else:
    print("\nIncorrect Password")
  else:
   print("\nUser Is Already An Admin")   
 else:
  if (ademail,) in banned:
   print("You Cant Make Banned Users Admins")
  else:   
   print("\nUser Does Not Exist")
 a.close() 
 return(0,0)

def removeadmin(email,admins,users):
 a=admincursor()
 a.execute("use Amazon")
 ademail=input("Enter Email Id Of The Admin ")
 if ademail!="admin101@admin1" and ademail!=email :
  if (ademail,) in admins:
   password=input("Enter Your Password ")
   a.execute("select password from users_list where email='{}'".format(email))
   correctpass=a.fetchone()
   decrpass=decrypt(correctpass[0])
   if password==decrpass:
    print("Do You Want To Remove",ademail,"As A Admin")
    cf=input("y/n ")
    if cf=="y":
     print("\nUser Has Been Removed As An Admin")
     return(1,ademail)
   else:
    print("\nIncorrect Password")
  else:
   print("\nUser Is Not An Admin")
 else:
  print("You Cant Remove That Admin")
 return(0,0)

def banuser(email,admins,adms,banned,users):
 a=admincursor()
 a.execute("use Amazon")  
 ademail=input("Enter Email Id Of The User ")
 if ademail!="admin101@admin1" and ademail!=email:
  if (ademail,) not in admins and (ademail,) not in banned:
   if (ademail,) in adms:
    password=input("Enter Your Password ")
    a.execute("select password from users_list where email='{}'".format(email))
    correctpass=a.fetchone()
    decrpass=decrypt(correctpass[0])
    if password==decrpass:
     print("Do You Want To Ban",ademail)
     cf=input("y/n ")
     if cf=="y":   
      print("\nUser Has Been Banned")
      return(1,ademail)
    else:
     print("\nIncorrect Password")
   else:
    print("\nUser Does Not Exist")
  else:   
   if (ademail,) in banned:   
    print("User Is Already Banned ")
   elif (ademail,) not in user:
    print("User Does Not Exist")
   else:
    print("\nYou Cant Ban Admins")
 else:
  print("You Cant Ban That Admin")
 return(0,0)


def unbanu(email,admins,banned,adms,users):
 a=admincursor()
 a.execute("use Amazon")  
 ademail=input("Enter Email Id Of The User ")
 if (ademail,) in adms:
  if (ademail,) in banned:
   password=input("Enter Your Password ")
   a.execute("select password from users_list where email='{}'".format(email))
   correctpass=a.fetchone()
   decrpass=decrypt(correctpass[0])
   if password==decrpass:
    print("Do You Want To Unban",ademail)
    cf=input("y/n ")
    if cf=="y":   
     print("\nUser Has Been UnBanned")
     return(1,ademail)
   else:
    print("\nIncorrect Password")
  else:  
   print("\nUser Is Not Banned")
 else:
  print("\nUser Does Not Exist")
 return(0,0)

def deleteuser(email,admins,users):
 a=admincursor()
 a.execute("use Amazon")
 ademail=input("Enter Email Id Of The User ")
 if (ademail,) in users:
  if (ademail,) not in admins:
   password=input("Enter Your Password ")
   a.execute("select password from users_list where email='{}'".format(email))
   correctpass=a.fetchone()
   decrpass=decrypt(correctpass[0])
   if password==decrpass:
    print("Do You Want To Delete",ademail)
    cf=input("y/n ")
    if cf=="y":
      print("\nUser Has Been Deleted")
      return(1,ademail)
   else:
    print("\nIncorrect Password")
  else:
   print("\nYou Cant Remove Admins")   
 else:  
  print("\nUser Does Not Exist")
 return(0,0)
 a.close() 
