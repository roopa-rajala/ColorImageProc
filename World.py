import cv2
import numpy as np
from math import pi, sqrt
import tkinter
from tkinter import Canvas,Label,StringVar,OptionMenu,Radiobutton,IntVar,Frame
from PIL import Image,ImageTk
from tkinter import filedialog
from ColorTransformations import ColorTransf
class GUI:
    def __init__(self):
        self.top = tkinter.Tk()
    def main(self):

        self.top.title("Color Image Processing")
        self.fileName = "C:/Users/Roopa/Documents/GitHub/assignment-2-roopa-rajala/Lenna.png"
        self.outputfileName="C:/Users/Roopa/PycharmProjects/ColorImageProc/Lenna0.jpg"
        self.layout = Canvas(self.top, width=600, height=600, bg='white')
        self.layout2 = Canvas(self.top, width=600, height=600, bg='white')
        self.frame1 = Frame(self.top)
        self.frame1.grid(row=0, column=0)
        browseButton = tkinter.Button(self.frame1, text="Browse", command=self.helloCallBack)
        browseButton.grid(row=0, column=0)
        self.var = IntVar()
        buttonradio1 = Radiobutton(self.frame1, text="ColorTransformations", variable=self.var, value=1, command=self.ColorTransfer)
        buttonradio2 = Radiobutton(self.frame1, text="PseudoColoring", variable=self.var, value=2, command=self.PseudoColor)
        buttonradio1.grid(row=1, column=0)
        buttonradio2.grid(row=1, column=1)

        self.frame2 = Frame(self.top)
        self.frame2.grid(row=1, column=0)
        self.convertButton = tkinter.Button(self.frame1, text="Convert", bg="green", command=self.start)
        self.convertButton.grid(row=5, column=1)
        pic = ImageTk.PhotoImage(Image.open(self.fileName))
        self.inputPic = Label(self.frame1,image = pic)
        self.inputPic.grid(row = 6,column = 0)
        pic1 = ImageTk.PhotoImage(Image.open(self.outputfileName))
        self.outputPic = Label(self.frame1, image=pic1)
        self.outputPic.grid(row=6, column=1)
        # self.layout.grid(row=1, column=0)
        # pic = ImageTk.PhotoImage(file=self.fileName)
        # inputPic = self.layout.create_image(250, 250, image=pic)
        # self.layout2.grid(row=1, column=1)
        # pic2 = ImageTk.PhotoImage(file=self.outputfileName)
        # inputPic2 = self.layout2.create_image(250, 250, image=pic2)
        self.top.mainloop()

    def helloCallBack(self):
        global fileName
        fileName = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"),("JPEG files","*.jpg"),("All files","*.*")])
        #exec(open('code.py').read())
    def ColorTransfer(self):
        global colorvar,colorvar2
        self.colorvar = StringVar()
        self.colorvar2 = StringVar()
        self.colorvar.set('RGB')
        self.colorvar2.set('CMYK')
        dropdownFrom = OptionMenu(self.frame1,self.colorvar,"RGB","CMYK","HSI")
        dropdownTo = OptionMenu(self.frame1,self.colorvar2,"RGB","CMYK","HSI")
        labelTo = Label(self.frame1,text="to")
        labelTo.grid(row=3,column=0)
        dropdownFrom.grid(row =2,column=0)
        dropdownTo.grid(row = 4,column=0)
    def PseudoColor(self):
        pseudovar = IntVar()
        button3 = Radiobutton(self.frame1, text="Experiment1", variable=pseudovar, value=1)
        button4 = Radiobutton(self.frame1, text="Experiment2", variable=pseudovar, value=2)
        button3.grid(row=2, column=1)
        button4.grid(row=3, column=1)
    def start(self):
        global colorvar,colorvar2,fileName,outputfileName
        if self.var.get()== 1:
            if self.colorvar.get()=='RGB' and self.colorvar2.get()=='CMYK':
                output = ColorTransf.RGBtoCMYK(self.fileName)
                print(type(output))

                im = Image.fromarray(output,mode = 'CMYK')
                im.save("test.jpg")
                print(type(im))
                op = ImageTk.PhotoImage(Image.open(self.outputfileName))
                print(type(op))
                # self.layout2.grid(row=1, column=1)
                self.inputPic.configure(image = op)
                #inputPic2 = self.layout2.create_image(250, 250, image=op)
                # inputPic2 = Label(frame2, image=op)
                # inputPic2.grid(row=6, column=2)

if __name__ == '__main__':
    g = GUI()
    g.main()