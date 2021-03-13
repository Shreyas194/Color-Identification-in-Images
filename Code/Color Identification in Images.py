# importing libraries
import pyautogui
import time
import cv2
import tkinter as tk
import webcolors as wc
from webcolors import css3_hex_to_names,hex_to_rgb
from scipy.spatial import KDTree


# function to detect color
def getcolor(color_tuple):
    root = tk.Tk()
    # try and except as every value cannot be converted to a color
    try:
        # get the name of color from rgb value
        color = wc.rgb_to_name(color_tuple)
            
    except ValueError:
        # if value invaild then call getnearestcolor function
        # to find nearest possible color
        color = getnearestcolor(color_tuple)
    
    # displaying color in a small window using tkinter
    if color == "black":
        tk.Label(root,text=color,fg="white",bg=color,font="Times 32").pack()
    else:
        tk.Label(root,text=color,fg="black",bg=color,font="Times 32").pack()
    
    root.after(1700, lambda: root.destroy())
    root.mainloop()


# function to find the nearest possible color if the values
# fails to be put into a color
def getnearestcolor(rgb_tuple):    
    # KDTree finds the closest matched hex code for
    # given RGB values that has a color name
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]


# detect mouse click event in an image
def click_event(event, x, y, flags, params):
    # detect left mouse click and get pixel color
    if event == cv2.EVENT_LBUTTONDOWN:
        x, y = pyautogui.position()
        pixel_tuple = pyautogui.screenshot().getpixel((x, y))
        
        getcolor(pixel_tuple)
        cv2.imshow('image', img)


if __name__ == "__main__":
    
    # storing hex_to_names database into a varible for later use
    css3_db = css3_hex_to_names
    names = []
    rgb_values = []
    
    # append each color name and rgb value in different lists
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
 
    img = cv2.imread('testing 3.jpg', 1) 
 
    cv2.imshow('image', img) 
 
    cv2.setMouseCallback('image', click_event)   # callback function for mouse click event
 
    cv2.waitKey(0) 
 
    cv2.destroyAllWindows()
