# -*- coding: utf-8 -*-

"""Here we can insert into Mysql tables products"""

import mysql.connector  # We importing module necessary to Mysql.
import requests
from bs4 import BeautifulSoup
import json
from config import *
from Tables import *    # We importing Tables from insert our products
                        # into Mysql tables.
from Affichage_Table import *
from cle_program import *

class Insertion:
    """We can insert products into tables"""

    def __init__(self, oinput):
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


    def insert_category(self):
        """Here we inserting category table"""
        
        user = "jbaw"
        
        self.liste = []

        path = "https://fr.openfoodfacts.org/categories"
        
        requete = requests.get(path)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")
        for tag in soup.find_all("td"):
            self.liste.append(tag.text)

        c = 0
        for i in range(3):
            a = self.liste[c]
            self.cursor.execute("""
            SET NAMES 'utf8';""")

            self.cursor.execute("""
            INSERT INTO Categorie(name)
            VALUES (%s)
            """, (a,))

            self.connexion.commit()

            c+=3


    def insert_food(self):

        """Here we run api and we take informations necessary for tables insertion"""
        c = 0
        d = 1
        self.liste_store = []
        self.liste_store1 = [[], [], [], [], [], [], [], [],
                             [], [], [], [], [], [], [], [],
                             [], [], [], [], [], [], [], []]
        
        self.liste_brands = []
        self.liste_brands1 = [[], [], [], [], [], [], [], [],
                              [], [], [], [], [], [], [], [],
                              [], [], [], [], [], [], [], []]
        
        
        self.liste2 = []
        
        for i in range(3):

            print(self.liste[c])
            print("\n")
            
            path2 = "https://fr.openfoodfacts.org/categorie/{}".format(self.liste[c])
            requete = requests.get(path2)
            page = requete.content
            soup = BeautifulSoup(page, "html.parser")
            for tag in soup.find_all("span"):
                self.liste2.append(tag.text)

            for i in self.liste2[6:]:
                print(i)
                a = str(i).find(" - ")
                i = i[0:a]
                print(i)
                path3 = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms={}&json=1"
                search = path3.format(i)
                r = requests.get(search)
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
                    if self.store_product == '':
                        self.liste_store.append("None")
                    else:
                        self.liste_store.append(self.store_product)
                except:
                    self.store_product = "None"
                    self.liste_store.append("None")
                    
                try:
                    self.brandss = data["products"][0]["brands"]
                    if self.brandss == '':
                        self.liste_brands.append(self.brandss)
                    else:
                        self.liste_brands.append(self.brandss)
                except:
                    self.brandss = "None"
                    self.liste_brands.append("None")
                    
                try:
                    self.nutriscore = data["products"][0]["nutrition_grades"]
                except:
                    self.nutriscore = "None"

                    
                sql_product = ("""
                INSERT INTO Aliment (id_categorie, name, description, code_product_food, nutriscore )
                VALUES(%s,%s,%s,%s,%s)
                """)
                values = (d, i, self.description_product, self.number_product, self.nutriscore)
                self.cursor.execute(sql_product, values)
                self.connexion.commit()

                if self.number_product == "None":
                    pass
                else:
                    Insertion.insertion_brands(self)
                    Insertion.insertion_store(self)
 
            d+=1
            c+=3
            self.liste2 = []



    def insertion_brands(self):
        """Here we insert into table multiples informations into brands"""
        
        print(self.liste_brands)
        c = 0
        for i in self.liste_brands:#on parcours la liste avant on a mis les info json, avec api
                                    #marqueur
            for j in i:
                if j == ",":            #si virgule alors on fait c + 1 faut mettre ca en anglais
                    c+=1
                else:
                    self.liste_brands1[c].append(j)
                
            for i in self.liste_brands1:
                if i == [] or i == [ ] or i == [""] or i == [" "]:
                    pass
                else:
                    print("".join(i))
                    Insertion.insert_brands(self, "".join(i), self.number_product)
                
            c = 0

            self.liste_brands1 = [[], [], [], [], [], [], [], [],
                                  [], [], [], [], [], [], [], [],
                                  [], [], [], [], [], [], [], []]
        
            self.liste_brands = []
            break

        
    def insertion_store(self):
        """Here we insert into table multiples informations into store"""
        print(self.liste_store)
        c = 0
        for i in self.liste_store:
            for j in i:
                if j == ",":
                    c+=1
                else:
                    self.liste_store1[c].append(j)
                
            for i in self.liste_store1:
                if i == [] or i == [ ] or i == [""] or i == [" "]:
                    pass
                else:
                    print("".join(i))
                    Insertion.insert_store(self, "".join(i), self.number_product)
                
            c = 0

            self.liste_store1 = [[], [], [], [], [], [], [], [],
                                 [], [], [], [], [], [], [], [],
                                 [], [], [], [], [], [], [], []]
            self.liste_store = []
            break  


    def insert_store(self, store_product, number_product):
        """Here we insert into store table informations"""

        self.store_product = store_product
        self.number_product = number_product
        
        sql_store = ("""
        INSERT INTO Store (name, code_product_store)
        VALUES(%s, %s)
        """)
        values2 = (self.store_product, self.number_product)
        self.cursor.execute(sql_store, values2)
        self.connexion.commit()


    def insert_brands(self, brandss, number_product):
        """Here we insert into brands table informations"""
        
        self.brandss = brandss
        self.number_product = number_product

        sql_brands = ("""
        INSERT INTO Brands (name, code_product_brands)
        VALUES(%s, %s)
        """)
        values3 = (self.brandss, self.number_product)
        self.cursor.execute(sql_brands, values3)
        self.connexion.commit()


    def insert_user(self):
        """Here we insert into table users informations"""
        
        self.cursor.execute("""
        INSERT INTO User (id_categorie_users, name, password, courriel )
        VALUES(2, 'jb', '123', 'leroidesloutres@hotmal.fr'),
        (1,'jbs','123','salut@hotmail.com');
        """)

        self.connexion.commit()           
                
