# -*- coding: utf-8 -*-
# pylint: disable = no-member

"""Here we creating tables necessary for our program"""

class Creation_tables:
    """We establish tables who contents products"""

    def create_table_category(self):
        """This is category table"""

        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categorie (

            id_categorie INT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(60) NOT NULL UNIQUE,

            PRIMARY KEY(id_categorie) )

            ENGINE=InnoDB;

            """)

        self.connexion.commit()

        
    def create_food_table(self):
        """We create food table"""

        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Aliment(

            id_produit INT UNSIGNED NOT NULL AUTO_INCREMENT,
            code_product_food VARCHAR(20) NOT NULL,
            id_categorie INT UNSIGNED NOT NULL,
            
            name TINYTEXT NOT NULL,
            description LONGTEXT,
            nutriscore varchar(10),
            

            PRIMARY KEY(id_produit) )

            ENGINE=InnoDB;
            """)

        self.connexion.commit()

        
    def create_table_product_delete(self):
        """We create delete product table"""

        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Product_delete(

            id_produit_substitut INT UNSIGNED NOT NULL AUTO_INCREMENT,
            id_categorie INT UNSIGNED NOT NULL,

            name TINYTEXT NOT NULL,
            brands VARCHAR(30) NOT NULL,
            description LONGTEXT,
            store VARCHAR(50),

            PRIMARY KEY (id_produit_substitut) )

            ENGINE=InnoDB;
            """)

        self.connexion.commit()

    def create_linking_table(self):
        """Here we create linkin table"""

        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE Linking (

            id_categorie INT UNSIGNED NOT NULL,
            id_produit INT UNSIGNED NOT NULL,


            PRIMARY KEY(id_categorie, id_produit),

            FOREIGN KEY (id_categorie)
            REFERENCES Categorie(id_categorie),

            FOREIGN KEY (id_produit)
            REFERENCES Aliment(id_produit) )

            ENGINE=INNODB;
            """)

        self.connexion.commit()

    def create_linking_table2(self):
        """Here we create linkin table"""

        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE Linking2 (

            id_categorie INT UNSIGNED NOT NULL,
            id_produit_substitut INT UNSIGNED NOT NULL,

            PRIMARY KEY(id_categorie, id_produit_substitut),

            FOREIGN KEY (id_categorie)
            REFERENCES Categorie(id_categorie),

            FOREIGN KEY (id_produit_substitut)
            REFERENCES Product_delete(id_produit_substitut) )

            ENGINE=INNODB;
            """)

        self.connexion.commit()


    def create_table_store(self):
        """Here we create store table"""

        user = "jbaw"

        self.cursor.execute("""

        CREATE TABLE Store(

            id_store INT UNSIGNED NOT NULL AUTO_INCREMENT,
            code_product_store VARCHAR(20) NOT NULL,
            name TINYTEXT NOT NULL,
            

            PRIMARY KEY(id_store) )

            ENGINE=InnoDB;
            """)

        self.connexion.commit()


    def create_table_brands(self):
        """Here we create brands table"""
        
        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Brands (

            id_brand INT UNSIGNED NOT NULL AUTO_INCREMENT,
            code_product_brands VARCHAR(20) NOT NULL,
            name VARCHAR(50) NOT NULL,

            
            PRIMARY KEY(id_brand) )

            ENGINE=InnoDB;
            """)
        self.connexion.commit()


    def create_linking_table_brands(self):
        """Here we create brands table"""

        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE Linking_product_brands (

            id_produit INT UNSIGNED NOT NULL,
            id_brand INT UNSIGNED NOT NULL,

            FOREIGN KEY (id_produit)
            REFERENCES Aliment(id_produit),

            FOREIGN KEY (id_brand)
            REFERENCES Brands(id_brand) )


            ENGINE=INNODB;
            """)
        self.connexion.commit()

        
    def create_table_linking_store_product(self):
        """Here we create linking store product table"""
        
        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE Linking_store_product(

            id_produit INT UNSIGNED NOT NULL,
            id_store INT UNSIGNED NOT NULL,

            FOREIGN KEY (id_produit)
            REFERENCES Aliment(id_produit),

            FOREIGN KEY (id_store)
            REFERENCES Store(id_store) )

            ENGINE=InnoDB;
            """)

        self.connexion.commit()


    def create_users(self):
        """Here we create users table"""
        
        user = "jbaw"

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (

            id_user INT UNSIGNED NOT NULL AUTO_INCREMENT,
            id_categorie_users INT UNSIGNED NOT NULL,
            name VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(25) NOT NULL,
            courriel VARCHAR(25) NOT NULL,

            PRIMARY KEY(id_user) )

            ENGINE=InnoDB;

            """)

        self.connexion.commit()
