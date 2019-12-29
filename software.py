import subprocess as sp
import time
import random 
list_of_p=[0,0,0,0]
# 0 INDEX IS FOR CRUST
# 1 INDEX IS FOR CHEESE
# 2 INDEX FOR SAUCE
# 3 INDEX FOR TOPPINGS
list_of_base = ["THIN CRUST" ,"FLATBREAT CRUST","THICK CRUST","WOOD FIRED CRUST"]
list_of_cheese = ["MOZZARELLA CHEESE.","PROVOLONE CHEESE.","CHEDDAR CHEESE"]
list_of_sauce = ["CHICKEN BBQ PLZZA SAUCE.","RANCH SAUCE.","ALFREDO SAUCE."]
list_of_top = ["ONIONS.","BACON.","MUSHROOMS.","PEPPERONI.","SAUSAGE."]
def ask_intent():
    print("WELCOME TO THE AUTOMATED PIZZA ORDERING SYSTEM")
    print("1. ORDER A PIZZA.")
    print("2. DELIVERY CHARGES CALCULATOR.")
    print("3. PIZZA DICTIONARY.")
    n= int(input("ENTER YOUR CHOICE : "))
    if n==1:
        print()
        print("CUSTOMIZE YOUR PIZZA TO YOUR LIKING.")
        print()
        customize_your_pizza()
    elif n==2:
        print()
        print("CALCULATE THE DELIVERY CHARGES BEFORE EVEN ORDERING IT.")
        print()
        charge_calculator()
    elif n==3:
        print()
        print("WELCOME TO OUR VERY OWN PIZZA DICTIONARY.")
        print()
        pizza_dic()
    else:
        print()
        print()
        print("ENTER A VALID INPUT.")
        ask_intent()
def pizza_dic():
    print("1.Margherita")
    print("A hugely popular margherita, with a deliciously tangy single cheese topping")
    print()
    print("2.Farm House")
    print("A pizza that goes ballistic on veggies! Check out this mouth watering overload of crunchy, crisp capsicum, succulent mushrooms and fresh tomatoes")
    print()
    print("3.Peppy Paneer")
    print("A Chunky paneer with crisp capsicum and spicy red pepper - quite a mouthful!")
    print()
    print("4.Mexican Green Wave")
    print("A pizza loaded with crunchy onions, crisp capsicum, juicy tomatoes and jalapeno with a liberal sprinkling of exotic Mexican herbs.")
    print()
    print("5.Deluxe Veggie")
    print("The onions, the capsicum, those delectable mushrooms - with paneer and golden corn to top it all.")
    print()
    print("6.Chicken Golden Delight")
    print("Mmm! Barbeque chicken with a topping of golden corn loaded with extra cheese. Worth its weight in gold!")
    print()
    print("7.Non Veg Supreme")
    print("Bite into supreme delight of Black Olives, Onions, Grilled Mushrooms, Pepper BBQ Chicken, Peri-Peri Chicken, Grilled Chicken Rashers")
    print()
    print("8.Chicken Dominator")
    print("Treat your taste buds with Double Pepper Barbecue Chicken, Peri-Peri Chicken, Chicken Tikka & Grilled Chicken Rashers")
    print()
    print("TAKE A IDEA FROM OUR STANDARD MENU AND CUSTOMIZE YOUR OWN.")
    print()
    ask_intent()
def charge_calculator():
    desti = input("ENTER THE LOCALITY WHERE YOU WANT TO DELIVER THE PIZZA : ")
    r1 = random.randint(0, 1000)
    if r1< 500 :
        print("There is no delivery charges for your locality.")
    else:
        traffic = random.randint(0,4)
        www = random.randint(0,2)
        charges = (r1*(0.3))
        #print(r1)
        print("THIS IS THE DELIVERY CHRAGES APPLICABLE ON YOUR ORDER : " ,charges)
    
def customize_your_pizza():
    print("WHAT KIND OF BASE FOR THE PIZZA IS PREFERED BY YOU?")
    print("1. THIN CRUST")
    print("2. FLATBREAT CRUST")
    print("3. THICK CRUST")
    print("4. WOOD FIRED CRUST")
    crust = int(input("ENTER YOUR CHOICE : "))
    list_of_p[0]=crust
    #print(list_of_p)
    print("WHAT KIND OF CHEESE FOR THE PIZZA IS PREFERED BY YOU?")
    print("1. MOZZARELLA CHEESE.")
    print("2. PROVOLONE CHEESE.")
    print("3. CHEDDAR CHEESE")
    cheese = int(input("ENTER YOUR CHOICE : "))
    list_of_p[1]=cheese
    print("WHAT KIND OF SAUCE FOR THE PIZZA IS PREFERED BY YOU?")
    print("1. CHICKEN BBQ PLZZA SAUCE.")
    print("2. RANCH SAUCE.")
    print("3. ALFREDO SAUCE.")
    sauce = int(input("ENTER YOUR CHOICE : "))
    list_of_p[2]=sauce
    print("WHAT KIND OF TOPPINGS FOR THE PIZZA IS PREFERED BY YOU?")
    print("1. ONIONS.")
    print("2. BACON.")
    print("3. MUSHROOMS.")
    print("4. PEPPERONI.")
    print("5. SAUSAGE.")
    toppings = int(input("ENTER YOUR CHOICE : "))
    list_of_p[3]=toppings
    print("***********  YOUR ORDER IS  ************")
    print("*",list_of_base[list_of_p[0]-1])
    print("*",list_of_cheese[list_of_p[1]-1])
    print("*",list_of_sauce[list_of_p[2]-1])
    print("*",list_of_top[list_of_p[3]-1])
    if input("PRESS (Y) TO PLACE THE ORDER AND (N) TO MAKE CHANGES : ")=='Y':
        print()
        print("ORDER IS BEING PLACED ...")
        print("********  PLEASE WAIT FOR A FEW SECONDS ********")
        time.sleep(1.0)
        print(".")
        time.sleep(1.0)
        print(".")
        time.sleep(1.0)
        print(".")
        time.sleep(1.0)
        print(".")
        time.sleep(1.0)
        print(".")
        print("****** THE PIZZA IS ON ITS WAY ******")
        time.sleep(2.0)
        print()
        print()
        ask_intent()
    else :
        print()
        customize_your_pizza()
    

ask_intent()
