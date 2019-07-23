# -*- coding: utf-8 -*-

"""From this class, we can run the program"""

import json
import mysql.connector          # We importing the modules necessary to the program

from Question import *       # We importing class for call fonctions
from Connexion import *
from config import *

#bug ca marche pas pour 2 
class Main:
    """We make a connection,
    we call fonctions from others class and we running it"""


    def __init__(self, choice_category):
        """Here we establish connection"""

        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER1,
                                                 password=PASSWORD,
                                                 database=DATABASE)

        self.cursor = self.connexion.cursor()

        self.choice_category = ""

        self.cursor.execute("""
        SET NAMES 'utf8';
        """)


    def program(self):
        """Here we lunch programm according to type of user"""
        
        Ask.users(self)


if __name__ == "__main__":
    """Here we create loop for continue the program"""

    continu = True

    run = Main("")

    while continu:

        run.program()
        ocontinuer = True
        while ocontinuer:
            oinput = input("Voulez vous continuer ?")

            if oinput == "n":
                print("Bye")
                quit()

            elif oinput == "o":
                break
