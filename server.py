from flask import Flask
import tkinter as Tkinter

top = Tkinter.Tk()

def helloCallBack():
   print("pog")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()

# app = Flask(__name__)

# @app.route('/')
# def root():
#     return("test")

# app.run()
