# -*- coding: utf-8 -*-

"""From this class we can delete database"""

import mysql.connector      #We importing modul necessary to establish Mysql connexion
from cle_program import *
from config import *

class delete_database:
    """Here we can delete database"""


    def __init__(self):
        """We initializing connexion for delete database"""

        code.cle(self)
        
        self.oinput = input("cle ?")
        if self.oinput != self.cle:
            quit()

        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD,
                                                 database=DATABASE)

        self.cursor = self.connexion.cursor()

        user = USER

        self.cursor.execute("""
        SET NAMES 'utf8';
        """)

    def delete_data(self):
        """We delete database"""

        user = USER
        self.cursor.execute("""
        DROP DATABASE pur_beurre""")

        print("data supprimée")

    def delete_user(self):
        user = USER
        self.cursor.execute("""
        drop user {}@localhost""".format(USER1))
    

        
if __name__ == "__main__":

    delete = delete_database()
    delete.delete_data()
    delete.delete_user()
