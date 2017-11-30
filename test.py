import tkinter as tk
from PIL import Image
from PIL import ImageTk
import numpy as np
from tkinter import filedialog
from tkinter.colorchooser import *
from IntensitySlicing import IntensitySlicing
from ColorTransformations import ColorTransf
from Filtering import Smoothing
class DIP(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Color Image Processing")
        self.pack(fill = tk.BOTH, expand = 1)

        menubar = tk.Menu(self.parent)
        self.parent.config(menu = menubar)
        self.browseButton = tk.Button(self,text = "Browse",command = self.onOpen)
        self.browseButton.grid(row =0,column=0)
        self.var = tk.IntVar()
        self.buttonradio1 = tk.Radiobutton(self, text="ColorTransformations", variable=self.var, value=1,
                                   command=self.ColorTransfer)
        self.buttonradio2 = tk.Radiobutton(self, text="PseudoColoring", variable=self.var, value=2,
                                   command=self.PseudoColor)
        self.buttonradio3 = tk.Radiobutton(self, text="Smoothing & Sharpening", variable=self.var, value=3,
                                           command=self.Filtering)
        self.buttonradio1.grid(row=1, column=0)
        self.buttonradio2.grid(row=1, column=1)
        self.buttonradio3.grid(row=1, column=2)
        self.label1 = tk.Label(self, border = 25)
        self.label2 = tk.Label(self, border = 25)
        self.label1.grid(row = 6, column = 0)
        self.label2.grid(row = 6, column = 1)
        # filename = "C:/Users/Roopa/Documents/GitHub/assignment-2-roopa-rajala/Lenna.png"
        # self.fn = filename
        # self.img = Image.open(self.fn)
        # self.I = np.asarray(self.img)
        # l, h = self.img.size
        # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
        # self.parent.geometry(text)
        # photo = ImageTk.PhotoImage(self.img)
        # self.label1.configure(image=photo)
        # self.label2.configure(image=photo)
        # self.label1.image = photo  # keep a reference!
        # self.label2.image = photo
        self.convertButton = tk.Button(self, text="Convert", bg="green", command=self.setImage)
        self.convertButton.grid(row=5, column=1)


    def ColorTransfer(self):
        self.colorvar = tk.StringVar()
        self.colorvar2 = tk.StringVar()
        self.colorvar.set('RGB')
        self.colorvar2.set('CMYK')
        dropdownFrom = tk.OptionMenu(self,self.colorvar,"RGB","CMYK","HSI")
        dropdownTo = tk.OptionMenu(self,self.colorvar2,"RGB","CMYK","HSI")
        labelTo = tk.Label(self,text="to")
        labelTo.grid(row=3,column=0)
        dropdownFrom.grid(row =2,column=0)
        dropdownTo.grid(row = 4,column=0)
    def PseudoColor(self):
        self.pseudovar = tk.IntVar()
        button3 = tk.Radiobutton(self, text="Intensity Slicing", variable=self.pseudovar, value=1)
        button4 = tk.Radiobutton(self, text="Color Transformation", variable=self.pseudovar, value=2)

        # colorPick = tk.Button(self, text="Color Pick", bg="green", command=self.getColor)

        button3.grid(row=2, column=1)
        button4.grid(row=3, column=1)
        # colorPick.grid(row=2, column=2)

    def getColor(self):
        color = askcolor()
        l = list(color)
        nl = list(l[0])


    def Filtering(self):
        self.filtervar = tk.IntVar()
        button3 = tk.Radiobutton(self, text="Smothing", variable=self.filtervar, value=1)
        button4 = tk.Radiobutton(self, text="Sharpening", variable=self.filtervar, value=2)
        button3.grid(row=2, column=2)
        button4.grid(row=3, column=2)
    def setImage(self):
        ct = ColorTransf()
        i = IntensitySlicing
        f = Smoothing
        if self.var.get()== 1:
            if self.colorvar.get()=='RGB' and self.colorvar2.get()=='CMYK':
                self.output = ct.RGBtoCMYK(self.fn)
                filename = "C:/Users/Roopa/PycharmProjects/ColorImageProc/test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm","ppm")
                # self.I = np.asarray(self.img)
                # l, h = self.img.size
                # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                # self.parent.geometry(text)
                photo = ImageTk.PhotoImage(file = "test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo
            elif self.colorvar.get()=='CMYK' and self.colorvar2.get()=='RGB':
                self.output = ct.CMYKtoRGB(self.fn)
                filename = "C:/Users/Roopa/PycharmProjects/ColorImageProc/test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm","ppm")
                # self.I = np.asarray(self.img)
                # l, h = self.img.size
                # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                # self.parent.geometry(text)
                photo = ImageTk.PhotoImage(file = "test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo
            elif self.colorvar.get()=='RGB' and self.colorvar2.get()=='HSI':
                self.output = ct.RGBtoHSV(self.fn)
                filename = "C:/Users/Roopa/PycharmProjects/ColorImageProc/test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm","ppm")
                # self.I = np.asarray(self.img)
                # l, h = self.img.size
                # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                # self.parent.geometry(text)
                photo = ImageTk.PhotoImage(file = "test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo
        elif self.var.get() == 2:
            if self.pseudovar.get() == 1:
                self.output = i.scale(i,self.fn, 50)
                filename = "C:/Users/Roopa/PycharmProjects/ColorImageProc/test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm", "ppm")
                # self.I = np.asarray(self.img)
                # l, h = self.img.size
                # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                # self.parent.geometry(text)
                photo = ImageTk.PhotoImage(file="test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo
        elif self.var.get() == 3:
            if self.filtervar.get() == 1:
                self.output = f.blurring(f, self.fn)
                filename = "test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm", "ppm")
                # self.I = np.asarray(self.img)
                # l, h = self.img.size
                # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                # self.parent.geometry(text)
                photo = ImageTk.PhotoImage(file="test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo

            elif self.filtervar.get() == 2:
                self.output = f.sharpening(f, self.fn)
                filename = "test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm", "ppm")
                # self.I = np.asarray(self.img)
                # l, h = self.img.size
                # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                # self.parent.geometry(text)
                photo = ImageTk.PhotoImage(file="test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo


    def onOpen(self):
        #Open Callback
        filename = filedialog.askopenfilename(
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
        self.fn = filename
        print()
        #print self.fn #prints filename with path here
        self.img = Image.open(self.fn)
        photo = ImageTk.PhotoImage(self.img)
        self.label1.configure(image=photo)
        self.label1.image = photo
    def setImage1(self):
        self.img = Image.open(self.fn)
        photo = ImageTk.PhotoImage(self.img)
        self.label1.configure(image=photo)
    #def onError(self):
        #box.showerror("Error", "Could not open file")

def main():

    root = tk.Tk()
    DIP(root)
    root.geometry("320x240")
    root.mainloop()


if __name__ == '__main__':
    main()