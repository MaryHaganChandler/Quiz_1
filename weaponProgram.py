import weaponClass as w
import csv


'''
- Create a program that will read the contents of the file 'weapons.txt'. Each record in
    the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the
    number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file
    to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


#Create a file object to open the file in read mode
weapons = open("weapons.csv", "r")


#Create a csv object from the file object
weapon_file = csv.reader(weapons, delimiter=",")


#Skip the header row
next(weapon_file)


#Create an empty dictionary named 'weapons_dict'
weapons_dict = {}



#Use a for loop to iterate through every row of the csv file
for row in weapon_file:
    #use variables for name, speed, and range (optional)
    name = row[0]
    speed = row[1]
    weapon_range = row[2]

    # create an instance of the weapon object using the
    # specs from the csv file (name, speed, and range)
    weapon = w.WeaponClass(name, speed, weapon_range)
    
    weapon.bullet_count()       #Must run this line before appending to dictionary


    # append the name and bullet count to 'weapons_dict'
    weapons_dict["Name:\t\t"] = name
    weapons_dict["Bullet count:\t"] = weapon.get_bullets()

    # print out the name of the weapon using the appropriate method of the object 
    print(weapon.get_name())

    # print out the speed of the weapon using the appropriate method of the object
    print(weapon.get_speed())

    # print out the range of the weapon using the appropriate method of the object
    print(weapon.get_range())

    # print out the number of bullets of the weapon using the appropriate method of the object
    print(weapon.get_bullets())


    #use an input statement to halt the program and wait for the user - 
    input("Press any key to fire the weapon")
    

    # use an appropriate loop to keep firing the weapon until all bullets run out
    bullets = weapon.get_bullets()
    for bullets in range(weapon.get_bullets()):
        # call the appropriate method to fire a bullet
        weapon.fire_bullet()
        # print out the bullet count every time the weapon is fired
        print(weapon.get_bullets(), end = "\r") #doesn't stay at 0??
    

    

#Using a loop, print out the name and number of bullets from the dictionary.
for i, j in weapons_dict.items():
    print(i, j)
