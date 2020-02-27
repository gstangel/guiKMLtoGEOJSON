import os
import kml2geojson
import tkinter as tk
from tkinter import messagebox

from tkinter import filedialog
#new tk instance
root = tk.Tk()
root.withdraw()

def getFilePath():
    
    global inputPath
    path = filedialog.askopenfilename()
    if(path != ""):
        inputPath = path
    
    else:
        messagebox.showinfo(title = "Error", message = "file path not specified")
    

def getOutputPath():

    global outputPath
    path = filedialog.askdirectory()
    if(path != ""):
        outputPath = path
    
    else:
        messagebox.showinfo(title = "Error", message = "Output not specified")
    
            


def convertKml():
    global inputPath,outputPath
    kml2geojson.main.convert(inputPath, outputPath)
    messagebox.showinfo(title = "Success", message = "File sucessfully outputted")



#GUI
window = tk.Tk()
window.title("GUI")
window.geometry('400x150')
label = tk.Label(window, text = "Simple KML to geoJson Converter").pack()

kmlOpenButton = tk.Button(window,text="Open KML", command = getFilePath)
destOpenButton = tk.Button(window,text="Choose Destination", command = getOutputPath)
startConvertButton = tk.Button(window,text="Convert KML to geoJson", command = convertKml)

kmlOpenButton.pack()
destOpenButton.pack()
startConvertButton.pack()

window.mainloop()





    