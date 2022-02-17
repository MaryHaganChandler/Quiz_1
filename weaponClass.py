import random

'''
Create a Weapon Class definition according to the following specs:

Attributes:

name - user supplied
bullets - random number between 10 and 100000
speed - user supplied
range - user supplied
status - 'Active' (this attribute should be changed to 'Inactive' if bullets 
                    run out.)

Methods:

Create accessor methods for each attribute.

Create a method named 'fire_bullet' that will simulate
firing a bullet. This is accomplished by decreasing the number of bullets by 1 
every time the method is called. When the bullet count reaches zero, it should change
the attribute 'status' to 'Inactive'

'''

class WeaponClass:
    def __init__(self, name, speed, weapon_range):
        self.__name = name
        self.__bullets = 0
        self.__speed = speed
        self.__range = weapon_range
        self.__status = "Active"

    #Do we need to create a set method for each one?

    def bullet_count(self):
        self.__bullets = random.randint(10,100000)

    def fire_bullet(self, bullets):
        if self.__bullets > 0:
            self.__bullets -= 1
            self.__status = "Active"
        else:
            self.__status = "Inactive"


    #Accessor methods
    def get_name(self):
        return self.__name

    def get_bullets(self):
        return self.__bullets

    def get_speed(self):
        return self.__speed

    def get_range(self):
        return self.__range

    def get_status(self):
        return self.__status









