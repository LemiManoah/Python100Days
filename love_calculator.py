print("welcome to the love calculator")
name1 = input("Enter your name:\n ")
name2 = input("Enter their name:\n ")

first_counter = 0

combined_name = name1 + name2

lower_combined_name = combined_name.lower()

t = lower_combined_name.count('t')
r = lower_combined_name.count('r')
u = lower_combined_name.count('u')
e = lower_combined_name.count('e')

true = t+r+u+e

l = lower_combined_name.count('l')
o = lower_combined_name.count('o')
v = lower_combined_name.count('v')
e = lower_combined_name.count('e')

love = l+o+v+e

love_score = str(true) + str(love)

int_score = int(love_score)

if int_score <= 10 or int_score >= 90:
    print(f"your score is {love_score} , you go together like coke and mentos")
elif int_score >= 40 and int_score <= 50:
    print(f"your score is {love_score} , you are alright together")
else:
    print(f"your score is {int_score}")

