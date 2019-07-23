#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from Affichage_Table import *
from cle_program import *
from config import *

class users:

    def __init__(self):
        """We initializing connexion"""
        code.cle(self)
        
        self.oinput = input("cle ?")
        if self.oinput != self.cle:
            quit()

        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER1,
                                                 password=PASSWORD,
                                                 database=DATABASE)

        self.cursor = self.connexion.cursor()

        self.cursor.execute("""
        SET NAMES 'utf8';
        """)

    def menu(self):

        self.choice = ""
        while self.choice != "i" or self.choice != "p":
            self.choice = input("voir le personnel : p, insérer du personnel: i")
            if self.choice == "i":
                users.question(self)
                users.insertion(self)
            elif self.choice == "p":
                DisplayMysql.show_table_users(self)

    def question(self):

        print("A noter que la categorie 1 est pour le personnel plus")

        self.insertion_name = input("nom ?")
        self.insertion_acces = input("categorie personnel ?")
        self.insertion_password = input("mot de passe ?")
        self.insertion_courriel = input("courriel?")


    def insertion(self):

        user = "jbaw"

        insert = """
        INSERT INTO User (id_categorie_users, name, password, courriel)
        VALUES(%s,%s,%s,%s)"""

        val = (self.insertion_acces,
               self.insertion_name,
               self.insertion_password,
               self.insertion_courriel)

        self.cursor.execute(insert, val)

        self.connexion.commit()


if __name__ == "__main__":

    continu = True
    oinput = ""
    
    while continu:
        run = users()
        while oinput != "o" or oinput != "n":

            run.menu()
            run.question()
            run.insertion()
            oinput = input("continuer a remplir ? o")

            if oinput == "n":
                oinput2 = input("voir la liste du personnel? o / n")

                if oinput2 == "o":
                    DisplayMysql.show_table_users(self)


                elif oinput2 == "n":
                    print("bye")
                    quit()
            
#on doit rendre ca plus ethétique peut etre      
#doit y avoir du bug aussi

























