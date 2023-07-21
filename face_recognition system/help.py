from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,text="HELP DISK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\12871ef5350ddf701ab15c445e9b4ef1.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        

        
        dev_label=Label(f_lbl,text="Email:abc@gmail.com",font=("times new roman",26,"bold"),bg="white")
        dev_label.place(x=1100,y=360)




if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()