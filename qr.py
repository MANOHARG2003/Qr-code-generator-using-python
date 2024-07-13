from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x600+200+50")
        self.root.title("QR GENERATOR") 
        title=Label(self.root,text="QR CODE GENERATOR" ,font=("times new roman",40),bg="firebrick4",fg='white').place(x=0,y=0,relwidth=1)

        #___student details window____
        #____variable_______
        self.var_student_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_section=StringVar()
        self.var_mail=StringVar()
        self.var_phno=StringVar()
        self.var_age=StringVar()
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        emp_Frame.place(x=50,y=100,width=600,height=480)

        emp_title=Label(emp_Frame,text="STUDENT DETAILS",font=("goudy old style",15),bg="#043256",fg='white').place(x=0,y=0,relwidth=1)

        #label of student details
        lbl_student_code=Label(emp_Frame,text="STUDENT ID",font=("times new roman",10,"bold"),bg="white").place(x=20,y=60)
        lbl_name_code=Label(emp_Frame,text="NAME",font=("times new roman",10,"bold"),bg="white").place(x=20,y=100)
        lbl_department_code=Label(emp_Frame,text="DEPARTMENT",font=("times new roman",10,"bold"),bg="white").place(x=20,y=140)
        lbl_section_code=Label(emp_Frame,text="SECTION",font=("times new roman",10,"bold"),bg="white").place(x=20,y=180)
        lbl_mail_code=Label(emp_Frame,text="MAIL",font=("times new roman",10,"bold"),bg="white").place(x=20,y=220)
        lbl_phno_code=Label(emp_Frame,text="MOBILE NO",font=("times new roman",10,"bold"),bg="white").place(x=20,y=260)
        lbl_age_code=Label(emp_Frame,text="AGE",font=("times new roman",10,"bold"),bg="white").place(x=20,y=300)


        # text for the student details
        txt_student_code=Entry(emp_Frame,font=("times new roman",10),textvariable=self.var_student_code,bg="lightyellow").place(x=200,y=60)
        txt_name_code=Entry(emp_Frame,font=("times new roman",10),textvariable=self.var_name,bg="lightyellow").place(x=200,y=100)
        txt_department_code=Entry(emp_Frame,font=("times new roman",10),textvariable=self.var_department,bg="lightyellow").place(x=200,y=140)
        txt_section_code=Entry(emp_Frame,font=("times new roman",10),textvariable=self.var_section,bg="lightyellow").place(x=200,y=180)
        txt_mail_code=Entry(emp_Frame,font=("times new roman",10),textvariable=self.var_mail,bg="lightyellow").place(x=200,y=220)
        txt_phno_code=Entry(emp_Frame,font=("times new roman",10),textvariable=self.var_phno,bg="lightyellow").place(x=200,y=260)
        txt_age_code=Entry(emp_Frame,font=("times new roman",10),textvariable=self.var_age,bg="lightyellow").place(x=200,y=300)



        btn_generator=Button(emp_Frame,text="GENERATE",command=self.generate,font=("times new roman",15,"bold"),bg="#2196f3",fg="white").place(x=30,y=350,width=160,height=30)
        btn_clear=Button(emp_Frame,text="CLEAR",command=self.clear,font=("times new roman",15,"bold"),bg="#607d8b",fg="white").place(x=300,y=350,width=160,height=30)

        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20),bg="white",fg="green")
        self.lbl_msg.place(x=0,y=320,relwidth=1)

        
        #___student qr window____
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_Frame.place(x=600,y=100,width=350,height=480)

        STUDENT_title=Label(qr_Frame,text="STUDENT QR CODE",font=("goudy old style",15),bg="#043256",fg='white').place(x=0,y=0,relwidth=1)
        self.qr_code=Label(qr_Frame,text="NO Qr\n available",font=15,bg="#3f51b5",fg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=90,y=100,width=180,height=180)



    def clear(self):
        self.var_student_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_section.set('')
        self.var_mail.set('')
        self.var_phno.set('')
        self.var_age.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_student_code.get()=='' or self.var_name.get()=='' or self.var_department.get()=='' or self.var_section.get()=='' or self.var_section.get()=='' or self.var_phno.get()=='' or self.var_age.get()=='':
            self.msg="All Fields Are Required!!!"
            self.lbl_msg.config(text=self.msg,fg="red")
        else:
            qrdata=(f"student id:{self.var_student_code.get()}\nstduent name:{self.var_name.get()}\nstudent department:{self.var_department.get()}\nstudent section:{self.var_section.get()}\nstudent mail:{self.var_mail.get()}\nstduent mobile no:{self.var_phno.get()}\nstduent age:{self.var_age.get()}\n")
            qr_code=qrcode.make(qrdata)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("QR_CODE_GENERATOR"+str(self.var_student_code.get())+'.png')
            #_______qr code image update_________
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            #_______updating notification_________
            self.msg='QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg,fg="green")

root=Tk()
obj=Qr_Generator(root)
root.mainloop()