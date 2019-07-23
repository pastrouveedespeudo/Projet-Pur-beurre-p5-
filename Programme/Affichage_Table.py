# -*- coding: utf-8 -*-
# pylint: disable = no-member

import re
"""Here we make fonction for display tables"""

class DisplayMysql:
    """We calling tables from Mysql and show it with show method"""

    def __init__(self):

        self.rows = self.cursor.fetchall()
        self.parameter = None
        self.product = None



    def show(self):
        """Here we displaying elements from tables"""

        self.rows = self.cursor.fetchall()
        print("\n")
        for i in self.rows:
            print(i)

    def show_category(self, liste):
        self.liste = liste
        c = 0
        self.rows = self.cursor.fetchall()
        for i in self.rows:
            print(i)
            c +=1
            self.liste.append(str(c))

    def show_liste(self, liste):
        """Here we displaying elements from tables"""

        self.liste = liste
        self.rows = self.cursor.fetchall()
        print("\n")
        for i in self.rows:
            print(i)
            liste.append(i)
        
    def not_show_liste(self, liste):
        """Here we displaying elements from tables"""

        self.liste = liste
        self.rows = self.cursor.fetchall()
        for i in self.rows:
            liste.append(i)
            
    def show_food(self):
        """Here we displaying elements from tables"""

        self.rows = self.cursor.fetchall()
        print("\n")
        c = 0
        for i in range(2):
            print(self.rows[c])
            c += 2

    def show_tables_category(self, liste):
        """Here we calling by order ascending categories"""

        self.liste = liste
        self.cursor.execute("""
        SELECT id_categorie, name
        FROM Categorie ORDER BY id_categorie ASC;
        """)

        DisplayMysql.show_category(self, self.liste)
        self.connexion.commit()

    def show_table_food_cat_one(self):
        """Here we calling food categorie one"""

        user = "jbaw"

        self.cursor.execute("""

        SELECT Aliment.id_produit, Aliment.name, Aliment.brands
        FROM Aliment
        INNER JOIN Categorie
        ON Aliment.id_categorie = Categorie.id
        WHERE id_categorie = 1 ;
        """)

        DisplayMysql.show(self)
        self.connexion.commit()

    def show_table_food_cat_two(self):
        """Here we calling food categorie two"""

        user = "jbaw"

        self.cursor.execute("""
        SELECT id_produit, name, id_categorie
        FROM Aliment
        WHERE id_categorie = 2;
        """)

        DisplayMysql.show(self)
        self.connexion.commit()

    def show_table_choice_category(self, parameter):
        """Here we displaying object from aliment, categorie tables
        from choice by user"""

        self.parameter = parameter

        user = "jbaw"

        self.cursor.execute("""SELECT Aliment.id_produit,
        Aliment.name
        FROM Aliment
        INNER JOIN Categorie
        ON Aliment.id_categorie = Categorie.id_categorie
        WHERE Categorie.id_categorie = %s
        """, (self.parameter,))

        DisplayMysql.show(self)
        self.connexion.commit()

    def show_choice_food(self, parameter, liste):
        """Here we displaying id, name, brands and description
        from user choice"""

        self.liste = liste
        self.parameter = parameter

        user = "jbaw"

        self.cursor.execute("""
        SELECT DISTINCT Aliment.id_produit, Aliment.name,
        Brands.name, Store.name 
        FROM Aliment
        
        INNER JOIN Brands 
        ON Aliment.code_product_food = Brands.code_product_brands

        INNER JOIN Store
        ON Aliment.code_product_food = Store.code_product_store

        WHERE id_produit = %s
        """, (self.parameter,))

        DisplayMysql.show_liste(self, self.liste)
        self.connexion.commit()
        
    def show_choice_food2(self, parameter, liste):
        self.liste = liste
        self.parameter = parameter

        user = "jbaw"

        self.cursor.execute(""" 
        SELECT * FROM Aliment
        WHERE id_produit = %s
        """, (self.parameter,))

        DisplayMysql.show_liste(self, self.liste)
        self.connexion.commit()


        
    def show_description(self, parameter, liste):
        self.parameter = parameter
        self.liste = liste
        user = "jbaw"

        self.cursor.execute("""
        SELECT Aliment.name, Aliment.description
        FROM Aliment
        WHERE id_produit = %s
        """, (self.parameter,))

        DisplayMysql.show_liste(self, self.liste)
        self.connexion.commit()
        
    def not_show_description(self, parameter, liste):
        self.parameter = parameter
        self.liste = liste
        user = "jbaw"

        self.cursor.execute("""
        SELECT Aliment.name, Aliment.description
        FROM Aliment
        WHERE id_produit = %s
        """, (self.parameter,))

        DisplayMysql.not_show_liste(self, self.liste)
        self.connexion.commit()
        
    def display_prod(self, parameter):
        """We displaying product from user choice"""

        self.product = []
        self.parameter = parameter

        user = "jbaw"

        self.cursor.execute("""
        SELECT name FROM Aliment
        WHERE id_produit = %s """, (self.parameter,))

        self.rows = self.cursor.fetchall()
        print("\n")
        for i in self.rows:

            self.product.append(i)

    def display_delete_food(self):
        """We displaying delete product table"""

        user = "jbaw"

        self.cursor.execute("""
        SELECT * FROM product_delete;
        """)

        DisplayMysql.show(self)
        self.connexion.commit()

    def reading(self, parameter):
        """We displaying Food from user choice"""

        user = "jbaw"

        self.parameter = parameter

        self.cursor.execute("""
        SELECT * FROM Aliment
        WHERE id_produit = %s""", (self.parameter,))

        self.connexion.commit()

    def display_food_table(self):
        """We displaying food table"""

        user = "jbaw"

        self.cursor.execute("""
        SELECT * FROM Aliment;
        """)
        DisplayMysql.show(self)
        
        self.connexion.commit()

    def search_into_base(self, parameter):

        self.parameter = parameter

        user = "jbaw"

        self.cursor.execute("""SELECT * FROM User
        WHERE name = %s""", (self.parameter,) )

        self.connexion.commit()


    def show_table_users(self):

        user = "jbaw"

        self.cursor.execute("""
        SELECT * FROM User;
        """)

        DisplayMysql.show(self)

        self.connexion.commit()
        


    def show_table_favorite(self):

        user = "jbaw"

        self.cursor.execute("""
        SELECT * FROM Aliment_favorite;
        """)

        DisplayMysql.show(self)

        self.connexion.commit()




















