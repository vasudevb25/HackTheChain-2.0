import random
def ad1():
    print("=============================================Ad===============================================")
    print("                                        AMA Studios")
    print("      Don't wait anymore and book your movie tickets from AMA Studios today at the best price!")
    print("                 Your access to your favourite movie is only a click away!")
    print("==============================================================================================")
def ad2():
    print("=============================================Ad===============================================")
    print("                                           TAJ Bank")
    print("                        Get Personalised Loans For All Your Dreams Big Or Small ")
    print("                                    Taj Bank With You Always ")
    print("==============================================================================================")

def ad3():
    print("=============================================Ad===============================================")
    print("                      Swiggy Food Delivery - Free Delivery On First Order ")
    print("       You Need No Occasion To Order Delicious Food On Swiggy. Order Now & Get Up To 50% Off")
    print("==============================================================================================")
def ad4():
    print("=============================================Ad===============================================")
    print("                                        Skyline Hotels")
    print("             Your Home Away From Home For All Your Travel Destinations ")
    print("                         20% Off Your First 5 Bookings  !Signup now!")
    print("=============================================================================================")
def ad5():
    print("=============================================Ad==================================================")
    print("                                    Smileplus Dental Clinic")
    print("        Book A  Free Appointment Near Your SmilePlus Dental Clinic Now In All Major Cities")
    print("                      Preserving Your Smiles Since 1990")
    print("================================================================================================")
def ad6():
    print("=============================================Ad==================================================")
    print("                                       Indian Railway")
    print("        Reserve All Your Train Tickets Using The New Indian Railway Network    ")
    print("                      Indian Railway -The Lifeline Of The Nation Since 1875")
    print("================================================================================================")
def ad7():
    print("=============================================Ad==================================================")
    print("                                       Tarun's Qp Bank")
    print("    The Definite Answer To All Your Questions For Classes 1-12.Start Now To Get 15% Off On All ")
    print("                                       Your Purchases")
    print("                            Solving Your Problems Since 2005")
    print("================================================================================================")
def ad():
    ads=random.randrange(1,8)
    if ads==1:
        ad1()
    if ads==2:
        ad2()
    if ads==3:
        ad3()
    if ads==4:
        ad4()
    if ads==5:
        ad5()
    if ads==6:
        ad6()
    if ads==7:
        ad7()
