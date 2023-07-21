from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\boruto.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        
        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"college_images\b36e4d6b172c911e8614f7f90323e15f.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        # Developer info
        dev_label=Label(main_frame,text="DIVYANSH VASHISTHA",font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=0,y=5)


        dev_label2=Label(main_frame,text="YOGITA BISHIT",font=("times new roman",18,"bold"),bg="white")
        dev_label2.place(x=25,y=40)


        dev_label3=Label(main_frame,text="PALAK SHUKLA",font=("times new roman",18,"bold"),bg="white")
        dev_label3.place(x=25,y=70)


        dev_label4=Label(main_frame,text="NIKITA BHATT",font=("times new roman",18,"bold"),bg="white")
        dev_label4.place(x=25,y=100)


        dev_label=Label(main_frame,text="BCA-CORE(DITU)",font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=25,y=130)

        img2=Image.open(r"college_images\596879eeac284.jpg")
        img2=img2.resize((500,390),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)

        


if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()