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
    weapon_range = [2]

    # create an instance of the weapon object using the
    # specs from the csv file (name, speed, and range)
    weapon = w.WeaponClass(name, speed, weapon_range)

    # append the name and bullet count to 'weapons_dict'
    weapons_dict["weapon"] = [name, weapon.bullet_count()]


    # print out the name of the weapon using the appropriate method of the object 
    print(weapon.get_name())

    # print out the speed of the weapon using the appropriate method of the object
    print(weapon.get_speed())

    # print out the range of the weapon using the appropriate method of the object
    print(weapon.get_range())

    # print out the number of bullets of the weapon using the appropriate method of the object
    print(weapon.bullet_count())


    #use an input statement to halt the program and wait for the user - 
    input("Press any key to fire the weapon")
    

    # use an appropriate loop to keep firing the weapon until all bullets run out

        # call the appropriate method to fire a bullet
    weapon.fire_bullet(weapon.bullet_count())
        # print out the bullet count every time the weapon is fired
    print(weapon.bullet_count())

    


#Using a loop, print out the name and number of bullets from the dictionary.
for i in weapons_dict:
    print("Name: ", i)
    print("Number of bullets: ", weapons_dict[i])
