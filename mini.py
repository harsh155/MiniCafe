#Create menu for our restaurant using dictionary 
menu={
    "Cold Coffee":80,
    "Choclate Shake":90,
    "Oreo Shake":100,
    "Cookie'n'Cream Shake":120,
    "Pizza-Puff":70,
    "French Fries":80,
    "Veg. Burger":80,
    "Cheese Burger":90,
    "Grill Sandwich":100,
    "Onion Pizza":100,
    "White Sauce Pasta":120,
    "Red Sauce Pasta":120,
    "Mix-Sauce Pasta":150,
    "Cheesy Pizza":150,
    "Chilli Noodles":150,
    "Chilli Butter Garlic Noodles":180,
    "Combo":220
}

#Welcome text
print("Hello, Welcome to Mini Cafe!\n")
print("What would you like to order!\n")
print("Cold Coffee:Rs.80/-\nChoclate Shake:Rs.90/-\nOreo Shake:Rs.100/-\nCookie'n'Cream Shake:Rs.120/-\nPizza-Puff:Rs.70/-\nFrench Fries:Rs.80/-\nVeg. Burger:Rs.80/-\nCheese Burger:Rs.90/-\nGrill Sandwich:Rs.100/-\nOnion Pizza:Rs.100/-\nWhite Sauce Pasta:Rs.120/-\nRedSauce Pasta:Rs.120/-\nMix-Sauce Pasta:Rs.150/-\nCheesy Pizza:Rs.150/-\nChilli Noodles:Rs.150/-\nChilli Butter Garlic Noodles:Rs.180/-\nCombo(Fires,Burger,Pizza-Puff & Cold Coffee):Rs.220/-\n")

#to disply total of your order
order_total=0

#Add order in cart
item_1=input("Enter the name of item you would like to order: ")
if item_1 in menu:
    order_total+=menu[item_1] #0+item_amt(for example cold coffe:80, 0+80)
else:
    print(f"Order item {item_1} is not available!")

order2=input("Would you like to order anything else? [Yes/No]")
if order2=="Yes":
    item_2=input("Enter the name of second item you would like to order: ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"{item_2} has been added to order")
    else:
        print(f"Order item {item_2} is not available!")
order3=input("Would you like to order anything else? [Yes/No]")
if order3=="Yes":
    item_3=input("Enter the name of third item you would like to order: ")
    if item_3 in menu:
        order_total+=menu[item_3]
        print(f"{item_3} has been added to order")
    else:
        print(f"Order item {item_3} is not available!")

#Showing total amount

print(f"The total amount of the items to pay is: {order_total}")

print("Thank You! Please Visit Again!")
