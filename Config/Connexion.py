# -*- coding: utf-8 -*-

import mysql.connector
from config import *

class Mysql_connexion:
    """Here we make data Mysql"""


    def database(self):
        """We creating database pur_beurre"""

        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER,
                                                 password=PASSWORD)

        self.cursor = self.connexion.cursor()

        user = USER

        self.cursor.execute("""
        CREATE DATABASE pur_beurre""")
 
        
        sql =("""
        CREATE USER %s@'localhost' IDENTIFIED BY %s""")
        values = (USER1, PASSWORD)
        
        self.cursor.execute(sql, values)

        
        sql1 = ("""GRANT ALL PRIVILEGES ON {}.* TO {}@'localhost'""".format(DATABASE, USER1))

        self.cursor.execute(sql1)
        
    def connexion(self):
        """We establish connexion with database with jbaw users"""

        self.connexion = mysql.connector.connect(host=HOST,
                                                 user=USER1,
                                                 password=PASSWORD,
                                                 database=DATABASE)
        self.cursor = self.connexion.cursor()

        user = USER
        self.cursor.execute("""
        USE pur_beurre""")
