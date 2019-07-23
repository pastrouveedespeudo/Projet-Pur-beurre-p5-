# -*- coding: utf-8 -*-

"""Here we create database, tables and we inserting products"""

from Tables import *            # We importing modules necessary to Mysql data
from Insertion_table import *
from Connexion import *
from cle_program import *
from config import *

class Lunching:
    """This is the first program to lunch for create our database"""

    def __init__(self):

        code.cle(self)
        
        self.oinput = input("cle ?")
        if self.oinput != self.cle:
            quit()

        Mysql_connexion.database(self)

        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER1,
                                                 password=PASSWORD,
                                                 database=DATABASE)
        self.cursor = self.connexion.cursor()

        user = "jbaw"

        self.cursor.execute("""
        SET NAMES 'utf8';
        """)

        print("Database crée")


    def tables(self):
        """We creating Mysql tables"""

        Creation_tables.create_table_category(self)
        Creation_tables.create_food_table(self)
        Creation_tables.create_table_product_delete(self)
        Creation_tables.create_table_store(self)
        Creation_tables.create_linking_table(self)
        Creation_tables.create_table_brands(self)
        Creation_tables.create_linking_table_brands(self)
        Creation_tables.create_table_linking_store_product(self)
        Creation_tables.create_users(self)

        print("Tables crées")


    def insertion_tables(self):
        """We inserting products into tables"""

        Insertion.insert_category(self)
        Insertion.insert_food(self)
        Insertion.insert_user(self)
        print("Produits de base insérés")


if __name__ == "__main__":

    lunch = Lunching()
    lunch.tables()
    lunch.insertion_tables()
