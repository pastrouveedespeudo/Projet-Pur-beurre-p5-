import PIL.Image
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt


class ImageClass:

    @classmethod
    def conversion(cls):
        img = Image.open("panier.jpg")
        img.save("panier.png")

    @classmethod
    def blackandwhite(cls):

        img = Image.open("panier.png").convert("LA")
        img.save("panier_nb.png")
        
    @classmethod
    def contour(cls):
        im = cv2.imread('panier_nb.png')
        imgray = cv2.cvtColor (im, cv2.COLOR_BGR2GRAY)
        
        ret, thresh = cv2.threshold (imgray, 127,255,0)
        im2, contours, hiérarchie = cv2.findContours (thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        cv2.drawContours (im, contours, -1, (0,0,0), 2)

   
    
        cv2.imshow("self.image", im)

if __name__ == "__main__":
    
    yo = ImageClass()
    yo.conversion()
    yo.blackandwhite()
    yo.contour()
