age=20
height=220
# and
if age >= 8 and height >=135:
    print("You can ride the ride.")

# or
if age >=17 or height >=160:
    print("You can ride the super ride.")

# elif (else if)
if height <120:
    print("You can't ride any rides.")
elif height <135:
    print("You can ride level-1 rides.")
elif height <200:
    print("You can ride any ride!")
else:
    print("Too tall to ride the rides.")


# and + or
age_approved=False
height_approved=False
if age >= 8 and age <=80:
    age_approved = True
if height >=120 and height <=210:
    height_approved = True
if age_approved == True and height_approved == True:
    print("All rides for you.")
elif age_approved == False or height_approved == False:
    print("You can not ride these rides.")

if age % 2 == 0 and age > 100 or age == 0:
    print("You have an intgeresting age.")