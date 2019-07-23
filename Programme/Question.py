# -*- coding: utf-8 -*-
# pylint: disable = no-member

"""This is core of our program"""


import json
import requests

from Affichage_Table import *



class Ask:
    """This is the core of the program, here we ask question and call tables"""


    def __init__(self):

        self.primary_choice = ""
        self.choice = ""
        self.choice_category = ""
        self.choice_food = ""

        self.choice_food = ""
        self.choice_category = ""
        self.brands = ""
        self.description_product = ""
        self.store_product = ""

        self.oinput = ""
        self.oinput3 = ""
        self.substitut = ""
        self.url_product = ""
        self.choice_for_off = ""
        self.number_product = ""


    def users(self):

        self.liste = []
        
        self.id = input("rentrez votre id")
        self.nom = input("inserer votre nom")
        self.password = input("inserer votre mot de passe")

        user = "jbaw"

        self.cursor.execute("""SELECT * FROM User
        WHERE id_user = %s""", (int(self.id),) )
        
        self.rows = self.cursor.fetchall()

        for i in self.rows:
            self.liste.append(i)
        try:
            if self.liste[0][3] == self.password\
                and self.liste[0][1] == 1 and self.nom == self.liste[0][2]:

                    print("bonjour", self.nom)

                    Ask.menu1(self)

            elif self.liste[0][3] != self.password:
                print("mot de passe ou nom erronées")

            elif self.liste[0][3] == self.password\
                and self.liste[0][2] == self.nom and self.liste[0][1] == 2\
                or self.liste[0][1] == 1:
                    print("bonjour !\n", self.nom)
                    Ask.user2(self)
        except:
            pass
        

    def user2(self):


        what_for = ""
        while what_for != "1" or what_for != "2" or what_for != "3"\
            or what_for != "4":
        
            print("table produit : 1\n"
              "chercher un produit via l'API : 2\n"
              "table produit substitut : 3\n"
              "stop ? s")
            
            what_for = input("Que voulez vous faire ?")
            
            if what_for == "1":
                DisplayMysql.display_food_table(self)
                
            elif what_for == "2":
                Ask.searching(self)
                    
            elif what_for == "3":
                DisplayMysql.display_delete_food(self)

            elif what_for == "s":
                break


    def searching(self):
        
        food = input("quel aliment cherchez vous ?")
        food = str(food)
        path = "https://world.openfoodfacts.org/cgi/search.pl?search_terms={0}&nutrition_grades=a&json=1"
        search = path.format(food)
        r = requests.get(search)
        print(search)
        data = json.loads(r.text)
        
        try:
            self.number_product = data["products"][0]['code']
        except:
            self.number_product = "None"
        try:
            self.description_product = data["products"][0]["ingredients_text_fr"]
        except:
            self.description_product = "None"
        try:
            self.url_product = "https://world.openfoodfacts.org/product/" + self.number_product
        except:
            self.url_product = "None"
        try:
            self.store_product = data["products"][0]["stores"]
        except:
            self.store_product = "None"
        try:
            self.brandss = data["products"][0]["brands"]
        except:
            self.brandss = "None"
        try:
            self.nutriscore = data["products"][0]["nutrition_grades"]
        except:
            self.nutriscore = "None"

        print(self.number_product)
        print(self.description_product)
        print(self.url_product)
        print(self.store_product)
        print(self.brandss)
        print(self.nutriscore)
             
        


    def return_menu(self, oinput):
        """We ask to user if he wants return into menu"""

        self.oinput = oinput

        if self.oinput == "m":
            Ask.menu1(self)
            

    def choice_menu(self):
        """We display message"""

        print("\n------MENU------ \n")
        print(" 1 - Quel aliment souhaites tu remplacer ?")
        print(" 2 - Retrouver mes aliments substitués ")
        print(" 3 - Consulter la table produit")
        print(" 4 - chercher un produit via l'API")
        print(" 5 - Voir les utilisateurs ?")
        print(" q - Quitter ?\n")


    def menu1(self):
        """We ask to user if he wants replace food or consult
        delete table"""

        Ask.choice_menu(self)

        oContinuer = True
        self.liste_category = []
        while oContinuer:

            self.choice_primary = input("Veuillez choissir! Choix : ")

            if self.choice_primary == "1":

                print("\n------Selection de la Catégorie------")
                DisplayMysql.show_tables_category(self, self.liste_category)
                Ask.choice_category(self)
                print(" \nMenu: 'm' ")
                break

            elif self.choice_primary == "2":
                print("----Aliment substitué----")
                DisplayMysql.display_delete_food(self)
                oinput = input("Menu: m")
                Ask.return_menu(self, oinput)
                


            elif self.choice_primary == "3":
                DisplayMysql.display_food_table(self)
                print(" \nMenu: 'm' or q pour quitter")
                ocontinuer = True
                while ocontinuer:
                    oInput_menu = input("Retourner au menu ? Quitter ?")
                    if oInput_menu == "m":
                        Ask.menu1(self)
                    elif oInput_menu == "q":
                        quit()
                    
            elif self.choice_primary == "4":
                Ask.searching(self)
                ocontinuer = True
                while ocontinuer:
                    print("m,  q,  c")
                    oInput_menu = input("Retourner au menu ? Quitter ? Continuer ?")
                    if oInput_menu == "m":
                        Ask.menu1(self)
                    elif oInput_menu == "q":
                        quit()
                    elif oInput_menu == "c":
                        Ask.searching(self)

            elif self.choice_primary == "5":
                Ask.see_users(self)
                    
            elif self.choice_primary == "q":
                quit()

            
    def choice_category(self):
        """User must choose a category"""

        ocontinuer = True

        while ocontinuer:
            
            self.choice_category = input("Selectionner la catégorie : ")
            self.choice_category = str(self.choice_category)
            self.choice = "{}".format(self.choice_category)
            self.choice_for_off = self.choice_category

            for i in self.liste_category:
                if self.choice_category == i:
                    print("\n------Selection du Produit------")
                    DisplayMysql.show_table_choice_category(self, self.choice_category)
                    Ask.choice_food(self)
                    

            if self.choice_category == "m":
                Ask.menu1(self)
                
                


    def choice_food(self):
        """Here user must choose food"""

        self.liste_description = []
        self.liste_substitute = []
        
        ocontinuer = True
        while ocontinuer:
        
            print("\nMenu : m")
    
            self.choice_food = input("Selectionnez un produit")
            self.choice_food = str(self.choice_food)

            self.choice = "{}".format(self.choice_food)
            if self.choice_food == "m":
                Ask.return_menu(self, self.choice_food)


            if self.choice_food == self.choice:
                DisplayMysql.show_choice_food(self, self.choice, self.liste_substitute)
                
                ocontinuer2 = True
                while ocontinuer2:
                    oInput_description = input("Voir la description ? o/n")
                    oInput_description = str(oInput_description)
                    
                    if oInput_description == "o":
                        DisplayMysql.show_description(self, int(self.choice_food), self.liste_description)
                        
                        continuer3 = True
                        while continuer3:
                            self.substitut = input("Voulez vous ajouter ce produit ? o/ n")
                            self.substitut = str(self.substitut)

                            if self.substitut == "n":
                                Ask.see_food_table(self)
                                Ask.menu1(self)
                            
                            elif self.substitut == "o":
                                Ask.select(self)
                                print(self.liste_substitute)
                                print(self.liste_description)
                                Ask.see_food_table(self)
                                Ask.menu1(self)
                                
 
                    elif oInput_description == "n":
                        DisplayMysql.not_show_description(self, int(self.choice_food), self.liste_description)
                        
                        continuer3 = True
                        while continuer3:
                            self.substitut = input("Voulez vous remplacer par ce produit ? o/ n")
                            self.substitut = str(self.substitut)

                            if self.substitut == "o":
                                Ask.select(self)
                                print(self.liste_substitute)
                                print(self.liste_description)
                                Ask.see_food_table(self)
                                Ask.menu1(self)
                                
                            
                            elif self.substitut == "n":
                                Ask.see_food_table(self)
                                Ask.menu1(self)
                                
                    
    def select(self):
        """Here we ask user if he wants change food"""

        sql = ("""
        INSERT INTO Product_delete (id_categorie, name, description, brands, store)
        VALUES(%s,%s,%s,%s,%s)
        """)
        values = (self.choice_category, str(self.liste_substitute[0][1]),
                  str(self.liste_description[0]), str(self.liste_substitute[0][2]),
                  str(self.liste_substitute[0][3]))

        self.cursor.execute(sql, values)

        self.connexion.commit() 
            
        print("Le produit a été remplacé")
        

    def see_food_table(self):

        ocontinuer2 = True
        while ocontinuer2:

            print("Quitter : q, Menu : m")

            oinpuut = input("souhaitez vous voir vos aliments actuels ? o/n")

            if oinpuut == "o":
                DisplayMysql.display_delete_food(self)
                ocontinuer = False
                break

            elif oinpuut == "n":
                break

            elif oinpuut == "q":
                print("aurevoir")
                quit()

            if oinpuut == "m":

                Ask.menu1(self)




    def see_users(self):
        DisplayMysql.show_table_users(self)
        ocontinuer = True
        while ocontinuer:
            oInput = input("Quitter ? Menu ? q, m")
            if oInput == "m":
                Ask.menu1(self)
            elif oInput == "q":
                quit()
            



    def see_nutriscore(self):
        pass
