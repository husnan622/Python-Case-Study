#We aren't using all of the libraries right now
#but we will use them later in the post

from tkinter import *
import pymysql as mdb
import pandas as pd
import time
from tkinter import messagebox
import datetime
import re
import os

#Define a class to set up our GUI
class App(object):
    def __init__(self, window):
    	 #Set the window title
        window.wm_title("Database Interface")

#In our main function, create the GUI and pass it to our App class
def main():
	window= Tk()
	start= App(window)
	window.mainloop()

#Run the main function
if __name__ == "__main__":
    main()

