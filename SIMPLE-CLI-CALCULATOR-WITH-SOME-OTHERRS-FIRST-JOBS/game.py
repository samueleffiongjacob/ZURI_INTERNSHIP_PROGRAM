# # first class


user1_number = 100
user1_guess = input("HELLO welcom to this great game : \n")

user1_guess = int(user1_guess)


# <==> >= <=

if user1_guess == user1_number:
    print("CONGRATULATION YOU SUCCESSFULLY " + str(user1_number))

elif user1_guess < user1_number:
    print("YOUR GUESS IS LOWER THAN EXPECTED VALUE PLEASE TRY AGAIN EXPECTED " +
          str(user1_number))
if user1_guess > user1_number:
    print("YOUR GUESS IS HIGHER THAN EXPECTED VALUE PLEASE TRY AGAIN  EXPECTED " + str(user1_number))

# positive inteja
useer_no = input("enter a number : \n")
try:
    useer_no = int(useer_no)
except:
    print("this is not a number")

if useer_no > 1:
    print("this is positive number")
elif useer_no < 1:
    print("false number")
