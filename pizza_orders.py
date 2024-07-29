print("Welcome to Lemi Pizzas!")
size = input("what pizza size do you want? S, M or L ").lower()
add_pepperoni = input("do you want to add a pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese on it? Y or N ").lower()

bill = 0
if size == "S":
    if add_pepperoni == "N":
        bill += 15
    else:
        bill = 15 + 2
elif size == "M":
    if add_pepperoni == "N":
        bill += 20
    else:
        bill = 20 + 3
else:
    if add_pepperoni == "N":
        bill += 25
    else:
        bill = 25 + 3
        
if extra_cheese == "Y":
    total_bill = bill + 1
    
print(f"your total bill is${total_bill}")