from Filter import *
def cateandsub():
 cats={"Gadgets":['Phone', 'Chargers', 'Laptop', 'Watch', 'Printer', 'Game Console', 'Tabs', 'Headsets', 'Other'],"Furniture":['Beds', 'Tables', 'Shelfs', 'Chairs', 'Sofas', 'Other'],"Books":['Fiction', 'Non Fiction', 'Biography', 'Auto Biography', 'Short Stories', 'Study Material', 'Other'],"Mens Clothing":['Shirts', 'Pants', 'Tradional', 'Hoodies', 'T Shirts', 'Boots', 'Shoes', 'Other'],"Womens Clothing":['Shirts', 'Pants', 'Tradional', 'Hoodies', 'T-Shirts', 'Boots', 'Shoes', 'Other'],"Travel And Sports":['Duffle Bag', 'Suitcases', 'Backpacks', 'Rucksacks', 'Footballs', 'Basketballs', 'Volleyballs', 'Cycles', 'Cricket Balls', 'Cricket Bats', 'Hockey Bats', 'Hockey Pucks', 'Skate Boards', 'Tennis Bat', 'Shuttle Bat', 'Other'],"Home-Appliance":['Tv', 'Washing Machines', 'Refrigerator', 'Microwaves', 'Dishwashers', 'Lamps', 'Fans', 'Other'],"Beauty":['Eye Liner', 'Lipstick', 'Foundation', 'Concealer', 'Blush', 'Eyeshadow', 'Other'],"Media":['Movies', 'Songs', 'Games', 'Pendrives', 'Cd', 'Blueray', 'Other'],"Other":["Other"]}
 cat=list(cats.keys())
 while True:
  for g in cat:
   print(cat.index(g)+1,")",g)
  print("0 ) Cancel")  
  scatsel=int(input("Select Category Of The Item From The Given Categories(index) "))
  if scatsel>0 and scatsel<len(cat)+1:
   scat=cat[scatsel-1]
   wantsub=input("Do You Want To Search by Sub-Category y/n ")
   if wantsub=="y":
    subs=cats[scat]
    while True:
     for h in subs:
      print(subs.index(h)+1,")",h)
     print("0 ) Cancel") 
     ssubsel=int(input("Select Sub-Category Of The Item From The Given Sub-Categories(index)) "))
     if ssubsel>0 and ssubsel<len(subs)+1:
      ssub=subs[ssubsel-1]
      return(scat,ssub)
     elif ssubsel==0:
      break 
     else:
      print("Invalide Choice")
   else:
    return(scat,"")
  elif scatsel==0:
   break
  else:
   print("Invalide Choice ")
 return("","")
def filters():
 name=input("Enter The Name Of The Item (Name Should Be Between 4 and 30 Characters And All Special Symbols Are Removed) ")
 name=af(name)
 wantcat=input("Do You Want To Search By Category y/n (Enter y To Search)")
 if wantcat=="y":
  scat,ssub=cateandsub()
 else:
  scat=""
  ssub=""
 wantkey=input("Do You Want To Search By Key y/n  (Enter y to Search)")
 if wantkey=="y":
  key=input("Enter Key Word Through Which People Can Also Search For(Key Words Can Brand Names ,Models etc Also All Special Symbols Are Removed) ")
  key=af(key)
 else:
  key=""
 return(name,scat,ssub,key)
