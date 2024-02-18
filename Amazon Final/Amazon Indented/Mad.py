import mysql.connector as ms
from Sql_Database import *
from JTL_Encry_V3_FA import *
from JTL_Decr_V3_FA import *
from Web_Login_Commands import *
from Creating_Account import *
from Admin_Controls import *
from Filter import *
from Shop_Commands import *
from Filter_Search import *
from Ads import *
sq=ms.connect(user="root",host="localhost",password="Arduino1")
a=sq.cursor()
loggedinstatus=0
def reviewlogo():
     print("\n================================================================================")     
     print(" ____  ______           _______  ______ ")
     print("|    ||       \      /     |    |       \      /\      /")
     print("|____||_____   \    /      |    |_____   \    /  \    /")
     print("|  \  |         \  /       |    |         \  /    \  /")
     print("|   \ |______    \/     ___|___ |______    \/      \/")
     print("================================================================================")
def shoplogo():
     print("\n================================================================================") 
     print("                 _____                    ____ ")
     print("|\    /| \   /  |       |     |  ______  |    |")
     print("| \  / |  \ /   |_____  |_____| |      | |____|")
     print("|  \/  |   |          | |     | |      | | ")
     print("|      |   |     _____| |     | |______| |")
     print("================================================================================")
def profilelogo():
     print("\n================================================================================")     
     print("                  ____   ____           ______  _______         ______    ")
     print("|\    /| \   /   |    | |    |  ______  |          |     |      |      ")
     print("| \  / |  \ /    |____| |____| |      | |_____     |     |      |_____  ")
     print("|  \/  |   |     |      |  \   |      | |          |     |      |    ")
     print("|      |   |     |      |   \  |______| |       ___|___  |_____ |______  ")
     print("================================================================================")
def searchlogo():
     print("\n================================================================================")   
     print(" _____   ______          ____   ______ ")
     print("|       |         /\    |    | |        |     |")
     print("|_____  |____    /  \   |____| |        |_____|")
     print("      | |       /----\  |   \  |        |     |") 
     print(" _____| |_____ /      \ |    \ |______  |     |")
     print("================================================================================")
def adminlogo():
     print("\n================================================================================")
     print("            ____            _______  ")
     print("     /\    |    \  |\    /|    |    |\   |")
     print("    /  \   |     | | \  / |    |    | \  |" )
     print("   /----\  |     | |  \/  |    |    |  \ | ")
     print("  /      \ |____/  |      | ___|___ |   \| \n")
     print("================================================================================\n")

def logo():
     print("\n================================================================================")
     print("                            _____    _____  ")
     print("     /\    |\    /|    /\       /   /     \  |\   |")
     print("    /  \   | \  / |   /  \     /   |       | | \  |")
     print("   /----\  |  \/  |  /----\   /    |       | |  \ |")
     print("  /      \ |      | /      \ /____  \_____/  |   \|\n")
     print("================================================================================\n")

def setaddress():
     print("Please specify a delivery address")
     while True:  
          address=input ('Address :')
          if len(address)!=0:
               fulladdress=address
               return(fulladdress)
          else:
               print("Invalid Address")  
def paymentmethod(price,qty):
     while True:
           print("Your Total Cost Is ",price*qty)
           payment=input('\nSelect a Payment Method: \r\n Press 1 for Cash on Delivery \r\n Press 2 for Internet Banking \r\n Press 3 for Debit/Credit/ATM/UPI ')
           if payment=='2' or payment=='3' :
                   print('\nSorry, This option is temporarily not available')
           elif payment=='1' :
                   print('\nThank you for purchasing from Amazon. Your product will be delivered within 2 working days')
                   break
           else :
                   print('\nSorry. Invalid option')
           
def searchview(c,search,email,items,name,scat,ssub,key):
       while True:
            a.execute("use amazon")
            print()
            ad()
            if len(items)!=0:
                 print("\n0: Go Back To Search ")  
                 for g in range(0,len(items)):
                       print("\nx-x-x-x-x-x-x")
                       print("|           |")
                       print("x           x")
                       print("|           |",g+1,")",items[g][1])
                       print("x           x In",items[g][5])
                       print("|           |")
                       print("x-x-x-x-x-x-x")   
                 y=int(input("Select Item (Index) "))
                 if y==0:
                      return(1)
                 elif y!=0 and y<len(items)+1 and y>-1:
                      while True:
                           print("\n++++++++++++++++++++++++++++++++++++++++")
                           print("Product Id : ",items[y-1][0])
                           print("Name : ",items[y-1][1])
                           print("\nDescription : ",items[y-1][2])
                           print("\nCost : ",items[y-1][3])
                           print("\nAvailable Qty :",items[y-1][4])
                           print("++++++++++++++++++++++++++++++++++++++++")
                           do=int(input("\n1: Buy \n3: Go Back\n2: See Reviews\n3: Write A Review\n4: Go Back\n"))
                           if do==1:
                                qty=int(input("Enter The Qty To Be Added "))
                                if qty>items[y-1][4] or qty<1:
                                     if qty<1:  
                                          print("\nInValid Amount ")
                                     else:
                                          print("The Entered Qty Is Greater Than Available Stock")
                                else:
                                      setaddress()
                                      paymentmethod(items[y-1][3],qty)
                                      a.execute("update total_items set stock={} where id={}".format(items[y-1][4]-qty,items[y-1][0]))
                                      a.execute("select history from users_list where email='{}'".format(email))
                                      urhist=a.fetchone()
                                      his=urhist[0]
                                      his=eval(his)
                                      if len(his)>19:
                                           his.pop(-len(his))
                                      his.append(items[y-1][0])
                                      a.execute("update users_list set history='{}'where email='{}'".format(his,email))
                                      sq.commit()
                                      a.execute(c)
                                      amount=items[y-1][4]
                                      items=a.fetchall()
                                      print("\nTransation Is Succefull ")
                                      if amount-qty==0:
                                           print("\nNo More Stock Available For This Item ")
                                           break
                                      a.execute(c)
                                      items=a.fetchall()
                           elif do==4:
                                break
                           elif do==2:
                                a.execute("select review from total_items where id={}".format(items[y-1][0]))
                                rev=a.fetchone()
                                if rev=="[]":
                                     print("\nNo Reviews Are Present")
                                else:
                                     reviewlogo()   
                                     revs=eval(rev[0])
                                     for g in revs:
                                          print("\n",g)
                           elif do==3:   
                                urev=input("Enter Your Review(Note: Review Should Be Less Than 190 characters And All Special Symbols Would Be Removed) ")
                                urev=af(urev)
                                if len(urev)>0 and len(urev)<191:
                                     a.execute("select review from total_items where id={}".format(items[y-1][0]))
                                     rev=a.fetchone()  
                                     revs=eval(rev[0])
                                     if len(revs)>10:
                                          revs.pop(0)
                                     revs.append(urev)
                                     a.execute('update total_items set review="{}" where id={}'.format(revs,items[y-1][0]))
                                     sq.commit()
                                else:
                                     print("\nYour Review Is Too Long")   
                      backfromsearch=input("\nDo You Want To Search For A New Item y/n ")
                      if backfromsearch=="y":
                           return(1)   
                 else:
                      print("Invalid Entry ")   
            else:
                 print("\nItem Not Found")
                 return(1)
def searchingforitem(email):
     while True:
          searchlogo()  
          a.execute("select email from bannedusers")
          banned=a.fetchall() 
          print("\nDo You Wish To \n1: Search \n2: Perform Filtered Search\n3: Go Back")
          searchmethod=int(input("Enter The Method You Want To Search By "))
          if searchmethod==1:
               search=input("Enter The Name Of The Product ")
               while True:
                    c="select id,item,description,cost,stock,category from total_items where item like '{}' and stock>0 and banned!=1".format("%"+search+"%")
                    a.execute(c)
                    items=a.fetchall()
                    name,scat,ssub,key="","","",""
                    b=searchview(c,search,email,items,name,scat,ssub,key)
                    if b==1:
                         break   
          elif searchmethod==2:
               name,scat,ssub,key=filters()
               a.execute("use amazon")
               while True:
                    c="select id,item,description,cost,stock,category from total_items where item like '{}' and  category like '{}' and sub_category like '{}' and keyword like'{}' and stock>0 and banned!=1".format("%"+name+"%","%"+scat+"%","%"+ssub+"%","%"+key+"%")
                    a.execute(c)
                    items=a.fetchall()
                    search=""
                    b=searchview(c,search,email,items,name,scat,ssub,key)
                    if b==1:
                         break
          elif searchmethod==3:
               break
          else:
               print("Invalid")  

def admin_controls(email):
     global loggedinstatus
     print("Admin")
     adminlogo()
     loggedinstatus=1
     while loggedinstatus==1:
          a.execute("USe Amazon")  
          a.execute("select email from users_list where admin=1")
          admins=a.fetchall()
          print("\nWhat Do You Want To \n1: Manage Users\n2: Search For Item\n3: Manage Store\n4: Log Out")
          whattodoadmin=int(input())
          if whattodoadmin==1:
                while True:  
                     print("\n1: Grant Admin Access \n2: Revoke Admin Access \n3: Ban User \n4: UnBan User\n5: Delete User\n6: Remove Item \n7: Go Back")
                     usercon=int(input("Select Option "))
                     a.execute("select email from users_list")
                     users=a.fetchall()
                     if usercon==1:
                          a.execute("select email from users_list where admin=1")
                          admins=a.fetchall()
                          a.execute("select email from bannedusers")
                          banned=a.fetchall()
                          grantaccess,ademail=grantadmin(email,admins,banned,users)   
                          if grantaccess==1:
                               a.execute("update users_list set admin=1 where email='{}'".format(ademail))
                               sq.commit() 
                     elif usercon==2:
                          a.execute("select email from users_list where admin=1")
                          admins=a.fetchall()      
                          removeaccess,ademail=removeadmin(email,admins,users)
                          if removeaccess==1:   
                               a.execute("update users_list set admin=0 where email='{}'".format(ademail))
                               sq.commit() 
                     elif usercon==3:
                          a.execute("select email from users_list where admin=1")
                          admins=a.fetchall()      
                          a.execute("select email from users_list")
                          adms=a.fetchall()
                          a.execute("select email from bannedusers")
                          banned=a.fetchall()
                          ban,ademail=banuser(email,admins,adms,banned,users)
                          if ban==1:
                               a.execute("insert into bannedusers values('{}')".format(ademail))
                               a.execute("select user_id from users_list where email='{}'".format(ademail))
                               ids=a.fetchone()
                               sid=ids[0]
                               a.execute("update total_items set banned=1 where sellerid={}".format(sid))
                               sq.commit()
                     elif usercon==4:
                          a.execute("select email from users_list where admin=1")
                          admins=a.fetchall()
                          a.execute("select email from users_list")
                          adms=a.fetchall()
                          a.execute("select email from bannedusers")
                          banned=a.fetchall()
                          unban,ademail=unbanu(email,admins,banned,adms,users)
                          if unban==1:
                               a.execute("select user_id from users_list where email='{}'".format(ademail))
                               ids=a.fetchone()
                               sid=ids[0]
                               a.execute("update total_items set banned=0 where sellerid={}".format(sid))
                               a.execute("delete from bannedusers where email='{}'".format(ademail))
                               sq.commit()
                     elif usercon==5:
                          a.execute("select email from users_list where admin=1")
                          admins=a.fetchall()
                          a.execute("select email from bannedusers")
                          banned=a.fetchall()
                          dele,ademail=deleteuser(email,admins,users)   
                          if dele==1:
                               a.execute("select user_id from users_list where email='{}'".format(ademail))
                               correctpass=a.fetchone()
                               ids=correctpass[0] 
                               a.execute("delete from users_list where email='{}'".format(ademail))
                               a.execute("delete from total_items where sellerid={}".format(ids)) 
                               sq.commit()
                     elif usercon==6:
                          ids=int(input("Enter The Product Id You Want Remove "))
                          a.execute("select id, item from total_items where id={}".format(ids))
                          item=a.fetchone()
                          if item!=None:
                               password=input("Enter Your Password ")
                               a.execute("select password from users_list where email='{}'".format(email))
                               correctpass=a.fetchone()
                               decrpass=decrypt(correctpass[0])
                               if password==decrpass:
                                    print("Do You Want To Remove",item[1])
                                    cf=input("y/n ")
                                    if cf=="y":
                                         a.execute("delete from total_items where id={}".format(item[0]))
                                         sq.commit()
                                         print("\nItem Has Been Removed")
                                    elif cf=="n":
                                         print("Ok")
                                    else:
                                         print("Invalid Entry")
                               else:
                                    print("Invalid Password")
                          else:
                               print("Item Not Found") 
                     elif usercon==7:
                         break
                     else:
                         print("Invalid Entry")   
          elif whattodoadmin==2:
               searchingforitem(email)
          elif whattodoadmin==3:
               storemenu(1)
          elif whattodoadmin==4:
               print("\nLogged Out")   
               loggedinstatus=0
          else:
               print("Invalid Entry")
def sellitem(uid,item,scat,ssub,sstock,scost,skey,sde):
     print(item,"|",scat,"|",ssub,"|",sstock,"|",scost,"|",skey,"|",sde,"|")
     check=input("Are All The Details Correct y/n ")
     if check=="y":
          a.execute("insert into total_items(item,sellerid,category,sub_category,stock,cost,description,keyword) values('{}',{},'{}','{}',{},{},'{}','{}')".format(item,uid,scat,ssub,sstock,scost,sde,skey))
          sq.commit()
          return(1)

def seefull(uid,ids):
     a.execute("select * from total_items where id={} and sellerid={}".format(ids,uid))
     sitem=a.fetchone()
     if sitem!=None:
          print("\nx-x-x-x-x-x-x")
          print("|           |")
          print("x           x")
          print("|           |")
          print("x           x")
          print("|           |")
          print("x-x-x-x-x-x-x")
          print("\n++++++++++++++++++++++++++++++++++++++++")   
          print("Product Id :",sitem[0])
          print("Name :",sitem[1])
          print("\nCategory :",sitem[3])
          print("\nSub-Category :",sitem[4])
          print("\nAvailable Qty :",sitem[5])
          print("\nCost :",sitem[6])
          print("\nDescription :",sitem[7])
          print("\nKey Word :",sitem[8])
          print("++++++++++++++++++++++++++++++++++++++++")
     else:
          print("No Such Item Is Present")


def storemenu(uid):
     while True:
          shoplogo()  
          print("\n1: Add More Items ")
          print("2: See My Items")
          print("3: Modify Item")
          print("4: Delete Item")
          print("5: Go Back")
          x=int(input("What Do You Want To Do "))
          if x==1:
               item,scat,ssub,sstock,scost,skey,sde=additem()
               if item!=-1:
                    sellitem(uid,item,scat,ssub,sstock,scost,skey,sde)
          elif x==2:
                a.execute("select id,item,category,sub_category,stock,keyword,cost,description from total_items where sellerid={}".format(uid))
                myitems=a.fetchall()  
                productintable(uid,myitems)
                dofull=input("Do You Want To See Full Details Of The Item y/n ")
                if dofull=="y":
                     ids=int(input("Enter The Product Id Of The Item From Above "))  
                     seefull(uid,ids)
          elif x==3:
                a.execute("select id,item,category,sub_category,stock,keyword,cost,description from total_items where sellerid={}".format(uid))
                myitems=a.fetchall()  
                productintable(uid,myitems)
                ids=int(input("Enter Id Of Item You Want To Modify "))
                seefull(uid,ids)
                a.execute("select * from total_items where id={} and sellerid={}".format(ids,uid))
                mit=a.fetchone()
                if mit!=None:
                     name,cat,sub,stock,cost,des,key=modify(mit)
                     a.execute("update total_items set item='{}',category='{}',sub_category='{}',stock={},cost={},description='{}',keyword='{}' where id={}".format(name,cat,sub,stock,cost,des,key,ids))
                     sq.commit()
          elif x==4:
                a.execute("select id,item,category,sub_category,stock,keyword,cost,description from total_items where sellerid={}".format(uid))
                myitems=a.fetchall()  
                productintable(uid,myitems)
                ide=int(input("Enter Id Of Item You Want To Remove "))
                a.execute("select * from total_items where id={} and sellerid={}".format(ide,uid))
                mit=a.fetchone()
                if mit!=None:
                     print("Do You Really Want To Delete",mit[1]) 
                     sure=input("y/n ")
                     if sure=="y":
                          a.execute("delete from total_items where id={}".format(ide))
                          sq.commit()
                          print("Item Removed")
                else:
                     print("Invalid Entry") 
          elif x==5:
                break
          else:
               print("Invalid Entry") 

def loggedin(email):
     global loggedinstatus
     loggedinstatus=1
     print("Welcome To Amazon")
     while loggedinstatus==1:
          logo()
          print("\nWhat Do You Want To \n1: Search Items \n2: Manage Your Store\n3: View Your Profile \n4: Log Out\n5: Delete Account ")
          whattodo=int(input())
          if whattodo==1:
               searchingforitem(email) 
          elif whattodo==2:
                a.execute("select user_id from users_list where email='{}'".format(email))
                ids=a.fetchall()
                uid=int(ids[0][0])
                a.execute("select * from total_items where sellerid ={}".format(uid))
                items=a.fetchall()
                a.execute("select id,item,category,sub_category,stock,keyword,cost,description from total_items where sellerid={}".format(uid))
                myitems=a.fetchall()
                if len(items)!=0:
                     storemenu(uid)
                else:
                     while True:
                          a.execute("select * from total_items where sellerid ={}".format(uid))
                          items=a.fetchall()     
                          x=input("You Are Currently Not Selling Anything Do You Want To Start Selling y/n ")
                          if x=="y":
                               done=0
                               item,scat,ssub,sstock,scost,skey,sde=additem()
                               if item!=-1:
                                    done=sellitem(uid,item,scat,ssub,sstock,scost,skey,sde)
                                    if done==1:
                                         storemenu(uid)   
                          break
          elif whattodo==3:
           #make A Logo For Profile
               a.execute("Use Amazon")  
               profilelogo()
               while True:
                    a.execute("select * from users_list where email='{}'".format(email))
                    ad()
                    user=a.fetchone()
                    print("  ______________________")
                    print(" /       __________     \ ")
                    print("/       /          \     \ ")
                    print("|       |          |      |")
                    print("|       |          |      |")
                    print("|       |          |      |")
                    print("|        \________/       |")
                    print("|      ______________     |")
                    print("|     /              \    |")
                    print("|    /                \   |")
                    print("\    |________________|   / ")
                    print(" \_______________________/")
                    print("\n Your Name:",user[1])
                    print("\n Your Mail Id:",user[3])
                    do=int(input("\nWhat Do You Want to Do\n1: Change Your Name \n2: View My Orders \n3: Change Your Password\n4: Go Back \n "))
                    if do==1:
                         name=input("Enter Your New Name ")
                         name=af(name)
                         if len(name)<31 and len(name)>2:
                              a.execute("update users_list set name='{}' where email='{}'".format(name,email))   
                         else:
                              print("Name Must Be Over 3 Characters And Below 30 Characters")
                    elif do==2:
                         a.execute("select history from users_list where email='{}'".format(email))
                         history=a.fetchone()
                         print("Your Last 20 Orders Are ")
                         his=eval(history[0])
                         a.execute("Select id,item from total_items")
                         items=a.fetchall()
                         ids=[]
                         names=[]
                         if len(his)!=0:
                              while True:
                                   print("\nYour History ")
                                   print("Id    |  Name ")
                                   for y in items:
                                        ids.append(y[0])
                                        names.append(y[1])
                                   for g in his:
                                        if g in ids:
                                             print("\n",g,":",names[ids.index(g)])
                                        else:
                                             his.remove(g)
                                   m=input("\nDo You Want To Leave y/n")
                                   if m=="y":
                                        break
                         else:
                              print("\n You Have Not Bought Anything Till Now")
                    elif do==3:
                         a.execute("select password from users_list where email='{}'".format(email))
                         cpassen=a.fetchone()
                         cpass=decrypt(cpassen[0])
                         cpassche=input("Enter Your Current Password ")
                         if cpassche==cpass:
                              npass=input("Enter You New Password (All Special Symbols Would Be Removed) ")
                              npass=af(npass)
                              if len(npass)>3 and len(npass)<21:
                                   npassen=encry(npass)
                                   a.execute("update users_list set password='{}' where email like '{}'".format(npassen,email))
                                   print("Password Has Been Changed")
                                   sq.commit()
                              else:
                                   print("Password Should Be More Than 3 Characters And Less Than 20")
                         else:
                              print("Incorrect Password")  
                    elif do==4:
                          break
                    else:
                         print("Invalid Entry") 
          elif whattodo==4:
               print("Logged Out")   
               loggedinstatus=0
          elif whattodo==5:
               a.execute("Use Amazon")
               password=input("Enter The Password ")
               a.execute("select password,user_id from users_list where email='{}'".format(email))
               correctpass=a.fetchone()
               decrpass=decrypt(correctpass[0])
               ids=correctpass[1]
               if password==decrpass:
                    sure=input("Do You Wish To Delete Account y/n")
                    if sure=="y":
                         a.execute("delete from users_list where email='{}'".format(email))
                         a.execute("delete from total_items where sellerid={}".format(ids))
                         sq.commit()
                         print("Account Has Been Removed")
                         loggedinstatus=0
               else:
                    print("\nIncorrect Password")
          else:
               print("\nInvalid Entry") 
def loginandsignin():
     logo()
     print("1:Sign In\n2:Login\n3:Credits\n")
     x=int(input("Do You Want To Sign In or Login(1 or 2 or 3 for Credits) "))
     if x==2:
          a.execute("Use Amazon")
          a.execute("select email from bannedusers")
          banned=a.fetchall() 
          email=input("Enter Your Email ")
          email=email.lower()
          a.execute("select email from users_list")
          checkuser=a.fetchall()
          if (email,) in checkuser and (email,) not in banned:   
               password=input("Enter Your Password ")
               a.execute("select password from users_list where email='{}'".format(email))
               correctpass=a.fetchone()
               decrpass=decrypt(correctpass[0])
               if password==decrpass:
                    a.execute("select email from users_list where admin=1")
                    admins=a.fetchall()
                    if (email,) in admins:
                         admin_controls(email)
                    else:
                         loggedin(email)
               else:
                    print("Password Is Incorrect")
          else:
               if (email,) in banned:
                    print("You Cannot Log On As You Have Been Banned")
               else:
                    print("User Does Not Exist ")
     elif x==1:
          a.execute("Use Amazon")   
          a.execute("select email from users_list")
          mails=a.fetchall()
          a.execute("select email from bannedusers")
          banned=a.fetchall()
          s,name,passe,email=signin(mails,banned)
          if s!='0':
               a.execute(s)
               sq.commit()
               if email!=None:
                    loggedin(email)
     elif x==3:
          print("\n\n")   
          print("░█████╗░██████╗░███████╗██████╗░██╗████████╗░██████╗")
          print("██╔══██╗██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝")
          print("██║░░╚═╝██████╔╝█████╗░░██║░░██║██║░░░██║░░░╚█████╗░")
          print("██║░░██╗██╔══██╗██╔══╝░░██║░░██║██║░░░██║░░░░╚═══██╗")
          print("╚█████╔╝██║░░██║███████╗██████╔╝██║░░░██║░░░██████╔╝")
          print("░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░╚═╝░░░╚═════╝░")
          print("\n\n")
          print(" ___________________________________________________")
          print("|                                                   ")
          print("| ░░█ █▀█ █░█ █▄░█   █▄█ █▀█ █░█ ▄▀█ █▄░█   ")
          print("| █▄█ █▄█ █▀█ █░▀█   ░█░ █▄█ █▀█ █▀█ █░▀█   ")
          print("|                                                   ")  
          print("| █▄░█ █▀█ █▀▀ █░░   █▀█ ▄▀█ ░░█ █▀▀ █▀▀ █░█|")
          print("| █░▀█ █▄█ ██▄ █▄▄   █▀▄ █▀█ █▄█ ██▄ ██▄ ▀▄▀")
          print("|                                                  ")
          print("|▄▀█ █▄▄ █░█ █ ░░█ █ ▀█▀ █░█")
          print("|█▀█ █▄█ █▀█ █ █▄█ █ ░█░ █▀█")
          print("|___________________________________________________")
     elif x==4:
         break
     else:
          print("Invalid Entry")
while loggedinstatus==0:
     loginandsignin()
a.close()
