import mysql.connector as sq
from Filter import *
s=sq.connect(host="localhost",user="root",passwd="Arduino1")
c=s.cursor()
def myorder(uid,history):
  pid="| Product Id         |"
  qty="Amount Bought         |"
  print("=================================================================================================================================================================")
  print(pid,qty)
  print("=================================================================================================================================================================")
  for g in history:
   for h in g:
    ids="| "+str(g[0])
    qt=str(g[1])
    remainid=len(pid)-len(ids)
    remainqty=len(qty)-len(qt)
    if remainid>0:
     for y in range(0,remainid-1):
      ids+=" "
     ids+="|"
    else:
     ids=ids[0:len(pid)-1]
     ids+="|"
    if remainqty>0:
     for i in range(0,remainqty-1):
      qt+=" "
     qt+="|"
    else:
     qt=qt[0:len(qtya)-3]
     qt+="..|"
    print(ids,qt) 
def productintable(uid,myitems):
  pid="| Product Id         |"
  namesta="Item Name             |"
  catla="Category         |"
  subla="Sub-Category     |"
  stockta="Stock Available         |"
  keyta="Keyword            |"
  costta="Cost    |"
  descta="Description        |"
  print("=================================================================================================================================================================")
  print(pid,namesta,catla,subla,stockta,keyta,costta,descta)
  print("=================================================================================================================================================================")
  for g in myitems:
   ids="| "+str(g[0])
   names=str(g[1])
   cats=g[2]
   sub=g[3]
   stock=str(g[4])
   key=g[5]
   cost=str(g[6])
   desc=g[7]
   remainid=len(pid)-len(ids)
   remainna=len(namesta)-len(names)
   remaincat=18-len(cats)
   remainsub=18-len(sub)
   remainstock=len(stockta)-len(stock)
   remainkey=len(keyta)-len(key)
   remaincost=9-len(cost)
   remaindes=len(descta)-len(desc)
   if remainid>0:
    for g in range(0,remainid-1):
     ids+=" "
    ids+="|"
   else:
    ids=ids[0:len(pid)-1]
    ids+="|"
   if remainna>0:
    for y in range(0,remainna-1):
     names+=" "
    names+="|"
   else:
    names=names[0:len(namesta)-3]
    names+="..|"
   if remaincat>0:
    for t in range(0,remaincat-1):
     cats+=" "
    cats+="|"
   if remainsub>0:
    for a in range(0,remainsub-1):
     sub+=" "
    sub+="|"
   if remainstock>0:
    for i in range(0,remainstock-1):
     stock+=" "
    stock+="|"
   else:
    stock=stock[0:len(stockta)-3]
    stock+="..|"
   if remainkey>0:
    for h in range(0,remainkey-1):
     key+=" "
    key+="|"
   else:   
    key=key[0:len(keyta)-3]
    key+="..|"
   if remaincost>0:
    for a in range(0,remaincost-1):
     cost+=" "
    cost+="|"
   if remaindes>0:
    for h in range(0,remaindes-1):
     desc+=" "
    desc+="|"
   else:
    desc=desc[0:len(descta)-3]
    desc+="..|"
   print(ids,names,cats,sub,stock,key,cost,desc)
  print("=================================================================================================================================================================")

def additem():
 cats={"Gadgets":['Phone', 'Chargers', 'Laptop', 'Watch', 'Printer', 'Game Console', 'Tabs', 'Headsets', 'Other'],"Furniture":['Beds', 'Tables', 'Shelfs', 'Chairs', 'Sofas', 'Other'],"Books":['Fiction', 'Non Fiction', 'Biography', 'Auto Biography', 'Short Stories', 'Study Material', 'Other'],"Mens Clothing":['Shirts', 'Pants', 'Tradional', 'Hoodies', 'T Shirts', 'Boots', 'Shoes', 'Other'],"Womens Clothing":['Shirts', 'Pants', 'Tradional', 'Hoodies', 'T-Shirts', 'Boots', 'Shoes', 'Other'],"Travel And Sports":['Duffle Bag', 'Suitcases', 'Backpacks', 'Rucksacks', 'Footballs', 'Basketballs', 'Volleyballs', 'Cycles', 'Cricket Balls', 'Cricket Bats', 'Hockey Bats', 'Hockey Pucks', 'Skate Boards', 'Tennis Bat', 'Shuttle Bat', 'Other'],"Home-Appliance":['Tv', 'Washing Machines', 'Refrigerator', 'Microwaves', 'Dishwashers', 'Lamps', 'Fans', 'Other'],"Beauty":['Eye Liner', 'Lipstick', 'Foundation', 'Concealer', 'Blush', 'Eyeshadow', 'Other'],"Media":['Movies', 'Songs', 'Games', 'Pendrives', 'Cd', 'Blueray', 'Other'],"Other":["Other"]}
 cat=list(cats.keys())
 name=input("Enter The Name Of The Item (Name Should Be Between 4 and 30 Characters And All Special Symbols Are Removed) ")
 name=af(name)
 if len(name)<101 and len(name)>3 :
  while True:
   for g in cat:
    print(cat.index(g)+1,")",g)
   print("0 ) Cancel") 
   scatsel=int(input("Select Category Of The Item From The Given Categories(index) "))
   if scatsel>0 and scatsel<len(cat)+1:
    scat=cat[scatsel-1]
    subs=cats[scat]
    while True:
     for h in subs:
      print(subs.index(h)+1,")",h)
     print("0 ) Cancel") 
     ssubsel=int(input("Select Sub-Category Of The Item From The Given Sub-Categories(index)) "))
     if ssubsel>0 and ssubsel<len(subs)+1:
      ssub=subs[ssubsel-1]
      while True:
       stocksel=int(input("Enter The Available Quantity Of The Item (Enter 0 To Cancel) "))
       if  stocksel>0 and stocksel<100000:
        sstock=stocksel
        while True:
         costsel=int(input("Enter The Selling Price Of This Item (Enter 0 To Cancel) "))
         if  costsel>0 and costsel<1000000:
          scost=costsel
          while True:
           keysel=input("Enter Key Word Through Which People Can Also Search For(Key Words Can Brand Names ,Models etc Also All Special Symbols Are Removed) (enter 'cancel' to Cancel) ")
           keysel=af(keysel)
           if len(keysel)>1 and len(keysel)<26 and keysel!="cancel": 
            skey=keysel.lower()
            while True:
             desel=input("Enter Description Of The Product(Description Should Be Between 2 And 800 Characters All Special Symbols Are Removed) (Enter 'cancel' To Cancel) ")
             desel=af(desel) 
             if len(desel)>1 and len(desel)<801 and desel!="cancel": 
              sde=desel
              return(name,scat,ssub,sstock,scost,skey,sde)
             elif desel=="cancel":
              break
             else:
              print("Description Should Be Between 2 And 800 Characters") 
            break
           elif keysel=="cancel":
            break
           else:
            print("Length Of Keys Should Be Between 2 To 25 Characters")
          break 
         elif costsel==0:
          break
         else:
          print("You Cant Sell This Item At This Selling Price (Selling Price Entered Should Be Between 0 And 1000000)")  
        break
       elif stocksel==0:
        break 
       else:
        print("Invalid Amount Of Stock (Stock Entered Should Be Between 0 And 100000)") 
      break
     elif ssubsel==0:
      break 
     else:
      print("Invalide Choice")
    break
   elif scatsel==0:
    break
   else:
    print("Invalide Choice ")
  print("Name Should Be Between 4 and 100 Characters") 
 name=-1
 scat=-1
 ssub=-1
 sstock=-1
 scost=-1
 skey=-1
 sde=-1
 return(-1,-1,-1,-1,-1,-1,-1)


def modify(mit):
 name=mit[1]
 cat=mit[3]
 sub=mit[4]
 stock=mit[5]
 cost=mit[6]
 des=mit[7] 
 key=mit[8]
 while True:
  print("\nWhat Do You Want To Modify")
  print("1: Name")
  print("2: Category")
  print("3: Sub-Category")
  print("4: Stock")
  print("5: Cost")
  print("6: Key Word")
  print("7: Description")
  print("0: Confirm Changes")
  cats={"Gadgets":['Phone', 'Chargers', 'Laptop', 'Watch', 'Printer', 'Game Console', 'Tabs', 'Headsets', 'Other'],"Furniture":['Beds', 'Tables', 'Shelfs', 'Chairs', 'Sofas', 'Other'],"Books":['Fiction', 'Non Fiction', 'Biography', 'Auto Biography', 'Short Stories', 'Study Material', 'Other'],"Mens Clothing":['Shirts', 'Pants', 'Tradional', 'Hoodies', 'T Shirts', 'Boots', 'Shoes', 'Other'],"Womens Clothing":['Shirts', 'Pants', 'Tradional', 'Hoodies', 'T-Shirts', 'Boots', 'Shoes', 'Other'],"Travel And Sports":['Duffle Bag', 'Suitcases', 'Backpacks', 'Rucksacks', 'Footballs', 'Basketballs', 'Volleyballs', 'Cycles', 'Cricket Balls', 'Cricket Bats', 'Hockey Bats', 'Hockey Pucks', 'Skate Boards', 'Tennis Bat', 'Shuttle Bat', 'Other'],"Home-Appliance":['Tv', 'Washing Machines', 'Refrigerator', 'Microwaves', 'Dishwashers', 'Lamps', 'Fans', 'Other'],"Beauty":['Eye Liner', 'Lipstick', 'Foundation', 'Concealer', 'Blush', 'Eyeshadow', 'Other'],"Media":['Movies', 'Songs', 'Games', 'Pendrives', 'Cd', 'Blueray', 'Other'],"Other":["Other"]}
  chawan=int(input("What Do You Want To Change "))
  if chawan==1: 
   namesel=input("Enter The New Name (No Special Symbols Allowed) ")
   namesel=af(namesel)
   if len(namesel)>3 and len(namesel)<101: 
    name=namesel
   else:
    print("Name Should Be Between 4 and 100 Characters")
  elif chawan==2:
   print()
   while True:
    k=list(cats.keys())
    for g in k:
     print(k.index(g)+1,")",g)
    scatsel=int(input("Select A Category From Above Options(Indexs) "))
    if scatsel>0 and scatsel<len(k)+1:
     cat=k[scatsel-1]
     subs=cats[cat]
     while True:
      print()
      for h in subs:
       print(subs.index(h)+1,")",h)
      subsel=int(input("Select A Sub-Category From Above Options(Indexs) "))
      if subsel>0 and subsel<len(subs)+1:
       sub=subs[subsel-1]
       break
      else:
       print("\nInvalid Entry")
    else:
     print("\nInvalid Entry") 
    break
  elif chawan==3:
   subs=cats[cat]
   while True:
    print()
    for h in subs:
     print(subs.index(h)+1,")",h)
    subsel=int(input("Select A Sub-Category From Above Options(Indexs) "))
    if subsel>0 and subsel<len(subs)+1:
     sub=subs[subsel-1]
     break
    else:
     print("\nInvalid Entry")
  elif chawan==4:
   stocksel=int(input("Enter The New Amount Of Stock Available "))
   if stocksel>0 and stocksel<100000:
    stock=stocksel
   else:
    print("Invalid Amount Of Stock (Stock Entered Should Be Between 0 And 100000)")
  elif chawan==5:
   costsel=int(input("Enter The New Selling Price "))
   if costsel>0 and costsel<10000000:
    cost=costsel
   else:
    print("Invalid Amount Of Stock (Stock Entered Should Be Between 0 And 1000000)")  
  elif chawan==6: 
   keysel=input("Enter The New Key Word(Like Brand Name etc..) (No Special Symbols Allowed) ")
   keysel=af(keysel)
   if len(keysel)>3 and len(keysel)<26:
    key=keysel 
   else:
    print("Length Of Keys Should Be Between 2 To 25 Characters")
  elif chawan==7:
   dessel=input("Enter The New Description (Description Should Be Between 2 And 800 Characters And No Special Symbols Allowed) ")
   dessel=af(keysel)
   if len(dessel)>1 and len(dessel)<801:
    des=dessel
  elif chawan==0:
   conf=input("Have You Finished The Modifying y/n ")
   if conf=="y":
    return(name,cat,sub,stock,cost,des,key)
   else:
    print("Ok Continue Modifying\n") 
  else:
   print("\nInvalid Entry")
