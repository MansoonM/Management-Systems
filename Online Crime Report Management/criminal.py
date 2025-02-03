from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title('CRIMINAL MANAGENET SYSTEM SOFTWARE')

        # Variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()



        lbl_title=Label(self.root,text="CRIMINAL MANAGENET SYSTEM SOFTWARE",font=("times new roman",38,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1530,height=70)

        # logo
        img_logo=Image.open('images/ncrlogo.png')
        img_logo=img_logo.resize((60,60),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=60)
        
        # Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=65,width=1530,height=130)

        # 1st
        img1=Image.open('images/police3.jpg')
        img1=img1.resize((540,160),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)


        # # 2st
        img_2=Image.open('images/police2.jpg')
        img_2=img_2.resize((540,160),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)


        # # 3st
        img_3=Image.open('images/police3.jpg')
        img_3=img_3.resize((540,160),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)

        # Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)

        # upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Criminal Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels and Entry fields
        caseid=Label(upper_frame,text='Case ID:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=("arial",11,"bold"))
        caseentry.grid(row=0,column=1,padx=2,pady=10, sticky=W)
        
       # Criminal NO
        lbl_criminal_no=Label(upper_frame,font=("arial",12,"bold"),text="Criminal NO:",bg="white")
        lbl_criminal_no.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=("arial",11,"bold"))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        # Criminal Name
        lbl_Name=Label(upper_frame,font=("arial",12,"bold"),text="Criminal Name:",bg="white")
        lbl_Name.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_Name.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # NickName
        lbl_nickname=Label(upper_frame,font=("arial",12,"bold"),text="NickName:",bg="white")
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=("arial",11,"bold"))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)

        # Arrest Date
        lbl_arrestDate=Label(upper_frame,font=("arial",12,"bold"),text="Arrest Date:",bg="white")
        lbl_arrestDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=("arial",11,"bold"))
        txt_arrestDate.grid(row=2,column=1,padx=2,pady=7)

        # Date of Crime
        lbl_dateOfCrime=Label(upper_frame,font=("arial",12,"bold"),text="Date of Crime:",bg="white")
        lbl_dateOfCrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dateOfCrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=("arial",11,"bold"))
        txt_dateOfCrime.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        # Address
        lbl_address=Label(upper_frame,font=("arial",12,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=3,column=1,padx=2,pady=7)

        # Age
        lbl_age=Label(upper_frame,font=("arial",12,"bold"),text="Age:",bg="white")
        lbl_age.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=("arial",11,"bold"))
        txt_age.grid(row=3,column=3,padx=2,pady=7)

        # occupution
        lbl_occupution=Label(upper_frame,font=("arial",12,"bold"),text="Occupation:",bg="white")
        lbl_occupution.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_occupution=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=("arial",11,"bold"))
        txt_occupution.grid(row=4,column=1,padx=2,pady=7)

        # birthMark
        lbl_birthMark=Label(upper_frame,font=("arial",12,"bold"),text="Birth Mark:",bg="white")
        lbl_birthMark.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_birthmark=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=("arial",11,"bold"))
        txt_birthmark.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        # Crime Type
        lbl_crimeType=Label(upper_frame,font=("arial",12,"bold"),text="Crime Type:",bg="white")
        lbl_crimeType.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_crimeType=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=("arial",11,"bold"))
        txt_crimeType.grid(row=0,column=5,padx=2,pady=7)

        # # Father Name
        lbl_fatherName=Label(upper_frame,font=("arial",12,"bold"),text="Father Name:",bg="white")
        lbl_fatherName.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_fatherName=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=("arial",11,"bold"))
        txt_fatherName.grid(row=1,column=5,padx=2,pady=7)

        #Radio Frame
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=730,y=90,width=190,height=30)

        lbl_gender=Label(upper_frame,font=("arial",12,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=2,column=5,pady=2,padx=5,sticky=W)
        self.var_gender.set('male')

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=2,column=6,pady=2,padx=5,sticky=W)

        # Most wantes

        lbl_wanted=Label(upper_frame,font=("arial",12,"bold"),text="Most Wanted:",bg="white")
        lbl_wanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)

        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=730,y=130,width=190,height=30)

        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=2,column=5,pady=2,padx=5,sticky=W)
        self.var_wanted.set('yes')

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=2,column=6,pady=2,padx=5,sticky=W)
        
        # backgound image
        img_crime=Image.open('images/backgound.jpg')
        img_crime=img_crime.resize((470,245),Image.LANCZOS)
        self.photocrime=ImageTk.PhotoImage(img_crime)

        self.img_crime=Label(upper_frame,image=self.photocrime)
        self.img_crime.place(x=1000,y=0,width=470,height=245)

        # Button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)

        btn_add=Button(button_frame,text="Record Save",command=self.add_data,font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        btn_update=Button(button_frame,text="Update",command=self.update_data,font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=1,pady=5)

        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=1,pady=5)

        btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=("arial",13,"bold"),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=1,pady=5)


        # down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

        # Search Frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",fg="white",bg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

         # search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("Select Option","Case_id","Criminal_no")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn__search=Button(search_frame,text="Search",command=self.serach_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn__search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(search_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_ShowAll.grid(row=0,column=4,padx=5)

        stayhome=Label(search_frame,text="NATIONAL CRIME AGENCY",font=("times new roman",25,"bold"),fg="crimson",bg="white")
        stayhome.place(x=780,y=0,width=600,height=30)

        # img_logo_mask=Image.open(r"images\backgound.jpg")
        # img_logo_mask=img_logo_mask.resize((50,50),Image.ANTIALIAS)
        # self.photoimg_logo_mask=ImageTk.PhotoImage(img_logo_mask)

        # self.logo=Label(search_frame,image=self.photoimg_logo_mask)
        # self.logo.place(x=900,y=0,width=50,height=30)

        # ============= Criminal table========================
        # Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading("2",text="CrimeNo")
        self.criminal_table.heading("3",text="Criminal Name")
        self.criminal_table.heading("4",text="NickName")
        self.criminal_table.heading("5",text="ArrestDate")
        self.criminal_table.heading("6",text="CrimeOfDate")
        self.criminal_table.heading("7",text="Address")
        self.criminal_table.heading("8",text="Age")
        self.criminal_table.heading("9",text="Occupation")
        self.criminal_table.heading("10",text="Birth Mark")
        self.criminal_table.heading("11",text="Crime Type")
        self.criminal_table.heading("12",text="Father Name")
        self.criminal_table.heading("13",text="Gender")
        self.criminal_table.heading("14",text="Wanted")

        self.criminal_table['show']='headings'

        self.criminal_table.column("1",width=100)
        self.criminal_table.column("2",width=100)
        self.criminal_table.column("3",width=100)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)
        self.criminal_table.column("6",width=100)
        self.criminal_table.column("7",width=100)
        self.criminal_table.column("8",width=100)
        self.criminal_table.column("9",width=100)
        self.criminal_table.column("10",width=100)
        self.criminal_table.column("11",width=100)
        self.criminal_table.column("12",width=100)
        self.criminal_table.column("13",width=100)
        self.criminal_table.column("14",width=100)
      

        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    # *************Function Declarations*******************
    
    def add_data(self):
        if self.var_criminal_no.get()=="" or self.var_nickname.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='mansoon111',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                                self.var_case_id.get(),
                                                                                                                self.var_criminal_no.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_nickname.get(),
                                                                                                                self.var_arrest_date.get(),
                                                                                                                self.var_date_of_crime.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_age.get(),
                                                                                                               
                                                                                                                self.var_occupation.get(),
                                                                                                                self.var_birthMark.get(),
                                                                                                                self.var_crime_type.get(),
                                                                                                                self.var_father_name.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_wanted.get()


                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been added!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='mansoon111',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # Get Cursor

    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])

    def update_data(self):
        if self.var_criminal_no.get()=="" or self.var_nickname.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are sure update this criminal record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='mansoon111',database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(

                                                                                                                                                                                                                               
                                                                                                                                                                                                                                self.var_criminal_no.get(),
                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                self.var_nickname.get(),
                                                                                                                                                                                                                                self.var_arrest_date.get(),
                                                                                                                                                                                                                                self.var_date_of_crime.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_age.get(),                                                                                                                                                               
                                                                                                                                                                                                                                self.var_occupation.get(),
                                                                                                                                                                                                                                self.var_birthMark.get(),
                                                                                                                                                                                                                                self.var_crime_type.get(),
                                                                                                                                                                                                                                self.var_father_name.get(),
                                                                                                                                                                                                                                self.var_gender.get(),                                                                                                                                       
                                                                                                                                                                                                                                self.var_wanted.get(),                                                                                                                                       
                                                                                                                                                                                                                                self.var_case_id.get(),

                                                                                                                                                                                                                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Criminal record successfully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # Delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error',"All fields are required")
        else:
            try:
                Delete=messagebox.askyesno('Delele','Are you sure delete this criminal',parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='mansoon111',database='management')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Criminal record Successfully Deleted',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # reset

    def reset_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        # self.var_occupationcomb.set("Select ID Proof")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    # search 
    def serach_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='mansoon111',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
                
                    



if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
        
