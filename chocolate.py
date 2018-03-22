year = input("What is the year?:")
year = int(year)
chocolate = input("pick the number of times a week that you would like to have chocolate. Cannot be 0:")
chocolate = int(chocolate)
print("Multiplying the number by 2")
print(str(chocolate) + " times 2")
print(chocolate * 2)
chocolate = chocolate * 2
print("adding 5...")
chocolate = chocolate + 5
print(chocolate)
print("Multiplying " + str(chocolate) + " by 50")
chocolate = chocolate * 50
print("Have you had your birthday this year? (Use 1 for yes, 0 for no please")
x = input(":")
if x == "1":
    y = -250 + year
    chocolate = chocolate + y
elif x == "0":
    y = -251 + year
    chocolate = chocolate + y
else:
    print("error, forcefully crashing script")
    chocolate = 0
age = input("What was the year you were born?:")
print(str(chocolate) + " - " +str(age))
chocolate = chocolate - int(age)
print(chocolate)
print("Now you have a number.")
print("The first is the amount of chocolate you wanted")
print("The next, is your age.")
