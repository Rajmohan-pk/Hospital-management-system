from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
#view_Appoinment_Details
def view_Appoinment_Details():
    doctor_name25=input_user_name24.get()
    input_password24.delete(0,END)
    input_user_name24.delete(0,END)
    input_user_name24.focus_set()
    
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res4=con.cursor()
    sql4="SELECT * FROM login WHERE username=%s"
    val4=(doctor_name25,)
    res4.execute(sql4,val4)
    a28=res4.fetchall()
    if len(a28)!=0:
        root26=Tk()
        root26.geometry("1200x800")
        root26.title("Appoinment details")
        root26.resizable(False,False)
        #title label
        label26=Label(root26,text="Appoinment Details",fg="black",bg="lightgreen",font=("times new roman",30))
        label26.place(x=450,y=10)
        con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
        res2=con.cursor()
        sql2="SELECT patient_aadhar_number,pname,page,pgender,pnumber,pbgroup FROM appoinment_details"
        res2.execute(sql2)
        alldata27=res2.fetchall()
        col27=["patient aadhar number","patient name","patient age","patient gender","patient phone number","patient blood group"]
        con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
        res3=con.cursor()
        sql3="SELECT doctor_name,doctor_roomno,doctor_department,doctor_id,appoinment_date,appointment_time FROM appoinment_details"
        res3.execute(sql3)
        alldata28=res3.fetchall()
        col28=["doctor name","doctor roomno","doctor department","doctor id","appoinment date","appointment time"]
        table27=ttk.Treeview(root26,columns=col27,show="headings")   
        for de in table27.get_children():
            table27.delete(de)
        for cols in col27:
            table27.heading(cols,text=cols)
            table27.grid(row=1,column=0)    
        for h,(patient_aadhar_number,pname,page,pgender,pnumber,pbgroup) in enumerate(alldata27,start=1):
            table27.insert("","end",values=(patient_aadhar_number,pname,page,pgender,pnumber,pbgroup))
            table27.place(x=10,y=70)
        table28=ttk.Treeview(root26,columns=col28,show="headings")   
        for de in table28.get_children():
            table28.delete(de)
        for cols in col28:
            table28.heading(cols,text=cols)
            table28.grid(row=1,column=0)    
        for h,(doctor_name,doctor_roomno,doctor_department,doctor_id,appoinment_date,appointment_time) in enumerate(alldata28,start=1):
            table28.insert("","end",values=(doctor_name,doctor_roomno,doctor_department,doctor_id,appoinment_date,appointment_time))
            table28.place(x=10,y=350)
        #exit button
        button_exit26=Button(root26,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root26.destroy)
        button_exit26.place(x=500,y=650)
        con.close()
        root26.mainloop()
    else:
        con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
        res=con.cursor()
        sql="SELECT patient_aadhar_number,pname,page,pgender,pnumber,pbgroup FROM appoinment_details WHERE doctor_name=%s"
        val=(doctor_name25,)
        res.execute(sql,val)
        alldata25=res.fetchall()
        a25=[]
        for i25 in alldata25:
            a25.append(i25)
        if len(a25)==0:
            messagebox.showwarning("Warning","No Appoinment")
        else:
            root25=Tk()
            root25.geometry("1200x800")
            root25.title("Appoinment details")
            root25.resizable(False,False)
            #title label
            label25=Label(root25,text="Appoinment Details",fg="black",bg="lightgreen",font=("times new roman",30))
            label25.place(x=450,y=10)
            col25=["patient aadhar number","patient name","patient age","patient gender","patient phone number","patient blood group"]
            con=mysql.connector.connect(host="localhost",user="root",password="Karthika@98",database="HMS")
            res1=con.cursor()
            sql1="SELECT doctor_name,doctor_roomno,doctor_department,doctor_id,appoinment_date,appointment_time FROM appoinment_details WHERE doctor_name=%s"
            val1=(doctor_name25,)
            res1.execute(sql1,val1)
            alldata26=res1.fetchall()
            col26=["doctor name","doctor roomno","doctor department","doctor id","appoinment date","appointment time"]
            table25=ttk.Treeview(root25,columns=col25,show="headings")   
            for de in table25.get_children():
                table25.delete(de)
            for cols in col25:
                table25.heading(cols,text=cols)
                table25.grid(row=1,column=0)    
            for h,(patient_aadhar_number,pname,page,pgender,pnumber,pbgroup) in enumerate(alldata25,start=1):
                table25.insert("","end",values=(patient_aadhar_number,pname,page,pgender,pnumber,pbgroup))
                table25.place(x=10,y=70)
            table26=ttk.Treeview(root25,columns=col26,show="headings")   
            for de in table26.get_children():
                table26.delete(de)
            for cols in col26:
                table26.heading(cols,text=cols)
                table26.grid(row=1,column=0)    
            for h,(doctor_name,doctor_roomno,doctor_department,doctor_id,appoinment_date,appointment_time) in enumerate(alldata26,start=1):
                table26.insert("","end",values=(doctor_name,doctor_roomno,doctor_department,doctor_id,appoinment_date,appointment_time))
                table26.place(x=10,y=350)
            #exit button
            button_exit25=Button(root25,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root25.destroy)
            button_exit25.place(x=500,y=650)
            con.close()
            root25.mainloop()
#Vist_doctor_data_Login_sql
def Vist_doctor_data_Login_sql():
    username24=input_user_name24.get()
    password24=input_password24.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="SELECT * FROM login_doctors WHERE username=%s AND password=%s"
    val=(username24,password24)
    res.execute(sql,val)
    a24=[]
    for i24 in res:
        a24.append(i24)
    if len(a24)>0:
        messagebox.showinfo("login","Login successfully")
        res.close()
        con.close()
        view_Appoinment_Details()
    else:
        messagebox.showwarning("Warning","username and password are incorrect")
        res.close()
        con.close()
        input_password24.delete(0,END)
        input_user_name24.delete(0,END)
        input_user_name24.focus_set()

#Visit_Doctor_Data_Login
def Visit_Doctor_Data_Login():
    root24=Tk()
    root24.geometry("500x500")
    root24.title("Login Form")
    root24.resizable(False,False)

    #title label
    label24=Label(root24,text="Login Form",fg="black",bg="lightgreen",font=("times new roman",30))
    label24.pack()
    #info label
    label_info24=Label(root24,text="**Use Doctors only **",fg="black",font=("times new roman",15,"bold"))
    label_info24.place(x=20,y=80)

    # Label
    label_user_name24=Label(root24,text="USER NAME",fg="black",font=("times new roman",12))
    label_user_name24.place(x=20,y=120)

    label_password24=Label(root24,text="PASSWORD",fg="black",font=("times new roman",12))
    label_password24.place(x=20,y=170)

    global input_user_name24
    global input_password24
    #entry
    input_user_name24=Entry(root24,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_user_name24.place(x=180,y=120)

    input_password24=Entry(root24,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30,show="*")
    input_password24.place(x=180,y=170)


     #login button
    button_login24=Button(root24,text="LOGIN",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=Vist_doctor_data_Login_sql)
    button_login24.place(x=200,y=250)

    #exit button
    button_exit24=Button(root24,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root24.destroy)
    button_exit24.place(x=180,y=350)


    root24.mainloop()

#view_doctor_data()
def view_doctor_data():
    adnumber15=input_aadhar_number15.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="Select * from doctor_new_registration_details where aadhar_number=%s"
    val=(adnumber15,)
    res.execute(sql,val)
    alldata=res.fetchall()
    a=[]
    for i in alldata:
        a.append(i)
    if len(a)==0:
        messagebox.showerror("Error","No data found")
        input_aadhar_number15.delete(0,END)
        input_aadhar_number15.focus_set()
    else:
        messagebox.showinfo("Info",f"Details: id={i[0]},\n aadhar number={i[1]},\n name={i[2]},\n age={i[3]},\n gender={i[4]},\n phone number={i[5]},\n blood group={i[6]},\n Department={i[7]},\n username={i[8]},\n password={i[9]} ")
    input_aadhar_number15.delete(0,END)
    input_aadhar_number15.focus_set()
    res.close()
    con.close()

#view_doctor_data_page
def view_doctor_data_page():
    root15=Tk()
    root15.geometry("600x400")
    root15.title("View Data")
    root15.resizable(False,False)

    #title label
    label15=Label(root15,text="View Doctor Data",fg="black",bg="lightgreen",font=("times new roman",30))
    label15.pack()

    #label
    label_aadhar_card15=Label(root15,text="AADHAR CARD",fg="black",font=("times new roman",15))
    label_aadhar_card15.place(x=20,y=130)

    global input_aadhar_number15
    #enters
    input_aadhar_number15=Entry(root15,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=40)
    input_aadhar_number15.place(x=180,y=130)

    #submit button
    button_submit15=Button(root15,text="SUBMIT",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=view_doctor_data)
    button_submit15.place(x=290,y=200)

    #exit button
    button_exit15=Button(root15,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root15.destroy)
    button_exit15.place(x=220,y=280)

    root15.mainloop()

#View_doctor_data_Login_sql
def View_doctor_data_Login_sql():
    username14=input_user_name14.get()
    password14=input_password14.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="SELECT * FROM login_doctors WHERE username=%s AND password=%s"
    val=(username14,password14)
    res.execute(sql,val)
    a=[]
    for i in res:
        a.append(i)
    if len(a)>0:
        messagebox.showinfo("login","Login successfully")
        res.close()
        con.close()
        input_password14.delete(0,END)
        input_user_name14.delete(0,END)
        input_user_name14.focus_set()
        view_doctor_data_page()
    else:
        messagebox.showwarning("Warning","username and password are incorrect")
        res.close()
        con.close()
        input_password14.delete(0,END)
        input_user_name14.delete(0,END)
        input_user_name14.focus_set()

#View_doctor_data_Login_page
def View_doctor_data_Login_page():
    root14=Tk()
    root14.geometry("500x500")
    root14.title("Login Form")
    root14.resizable(False,False)

    #title label
    label14=Label(root14,text="Login Form",fg="black",bg="lightgreen",font=("times new roman",30))
    label14.pack()
    #info label
    label_info14=Label(root14,text="**Use Admin And Doctors **",fg="black",font=("times new roman",15,"bold"))
    label_info14.place(x=20,y=80)

    # Label
    label_user_name14=Label(root14,text="USER NAME",fg="black",font=("times new roman",12))
    label_user_name14.place(x=20,y=120)

    label_password14=Label(root14,text="PASSWORD",fg="black",font=("times new roman",12))
    label_password14.place(x=20,y=170)

    global input_user_name14
    global input_password14
    #entry
    input_user_name14=Entry(root14,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_user_name14.place(x=180,y=120)

    input_password14=Entry(root14,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30,show="*")
    input_password14.place(x=180,y=170)


     #login button
    button_login14=Button(root14,text="LOGIN",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=View_doctor_data_Login_sql)
    button_login14.place(x=200,y=250)

    #exit button
    button_exit14=Button(root14,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root14.destroy)
    button_exit14.place(x=180,y=350)


    root14.mainloop()
#Doctor_Update_Account_Details
def Doctor_Update_Account_Details():
    dusername18=input_new_username17.get()
    dpassword18=input_new_password17.get()
    danumber18=input_doctor_aadhar_number17.get()
    dname18=input_doctor_name17.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res1=con.cursor()
    sql1="update Login_Doctors set username=%s,password=%s,name=%s where aadhar_number=%s"
    val1=(dusername18,dpassword18,dname18,danumber18)
    res1.execute(sql1,val1)
    con.commit()
    messagebox.showinfo("Update","Account Details Updated successfully...")
    res1.close()
    con.close()
    input_doctor_aadhar_number17.delete(0,END)
    input_doctor_name17.delete(0,END)
    input_doctor_age17.delete(0,END)
    input_doctor_gender17.delete(0,END)
    input_phone_number17.delete(0,END)
    input_blood_group17.delete(0,END)
    input_department17.delete(0,END)
    input_new_username17.delete(0,END)
    input_new_password17.delete(0,END)
    input_doctor_aadhar_number17.focus_set()

#Doctor_Details_Update
def Doctor_Details_Update():
    danumber17=input_doctor_aadhar_number17.get()
    dname17=input_doctor_name17.get()
    dage17=input_doctor_age17.get()
    dgender17=input_doctor_gender17.get()
    dpnumber17=input_phone_number17.get()
    dbgroup17=input_blood_group17.get()
    ddept17=input_department17.get()
    dusername17=input_new_username17.get()
    dpassword17=input_new_password17.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="update doctor_new_registration_details set dname=%s,dage=%s,dgender=%s,dnumber=%s,dbgroup=%s,ddepartment=%s,dusername=%s,dpassword=%s where aadhar_number=%s"
    val=(dname17,dage17,dgender17,dpnumber17,dbgroup17,ddept17,dusername17,dpassword17,danumber17)
    res.execute(sql,val)
    con.commit()
    messagebox.showinfo("Update","Details Updated successfully...")
    res.close()
    con.close()
    Doctor_Update_Account_Details()

#Change_doctor_data_Submit
def Change_doctor_data_Submit_Sql():
    adnumber16=input_aadhar_number16.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="Select * from doctor_new_registration_details where aadhar_number=%s"
    val=(adnumber16,)
    res.execute(sql,val)
    alldata17=res.fetchall()
    a17=[]
    for j in alldata17:
        a17.append(j)
    if len(a17)==0:
        messagebox.showerror("Error","No data found")
        input_aadhar_number16.delete(0,END)
        input_aadhar_number16.focus_set()
    else:
        input_aadhar_number16.delete(0,END)
        input_aadhar_number16.focus_set()
       # messagebox.showinfo("Info",f"Details: id={i[0]},\n aadhar number={i[1]},\n name={i[2]},\n age={i[3]},\n gender={i[4]},\n phone number={i[5]},\n blood group={i[6]},\n Department={i[7]},\n username={i[8]},\n password={i[9]} ")
        root17=Tk()
        root17.geometry("500x900")
        root17.title("Doctor Updation Form")
        root17.resizable(False,False)
        # title label
        label17=Label(root17,text="Doctor Change Detail",fg="black",bg="lightgreen",font=("times new roman",30))
        label17.pack()

        #labels
        label_doctor_aadhar_card17=Label(root17,text="AADHAR CARD",fg="black",font=("times new roman",12))
        label_doctor_aadhar_card17.place(x=20,y=150)
        label_list17=["NAME","AGE","GENDER M/F","PHONE NUMBER","BLOOD GROUP","DEPARTMENT","NEW USERNAME","NEW PASSWORD"]
        count17=150
        for i in label_list17:
            count17=count17+50
            l17=Label(root17,text=i,fg="black",font=("times new roman",12))
            l17.place(x=20,y=count17)

        global input_doctor_aadhar_number17
        global input_doctor_name17
        global input_doctor_age17
        global input_doctor_gender17
        global input_phone_number17
        global input_blood_group17
        global input_department17
        global input_new_username17
        global input_new_password17
        #enters
        input_doctor_aadhar_number17=Entry(root17,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_doctor_aadhar_number17.place(x=180,y=150)

        input_doctor_name17=Entry(root17,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_doctor_name17.place(x=180,y=200)

        input_doctor_age17=Entry(root17,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_doctor_age17.place(x=180,y=250)

        input_doctor_gender17=Entry(root17,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_doctor_gender17.place(x=180,y=300)

        input_phone_number17=Entry(root17,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_phone_number17.place(x=180,y=350)

        input_blood_group17=Entry(root17,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_blood_group17.place(x=180,y=400)

        input_department17=Entry(root17,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_department17.place(x=180,y=450)

        input_new_username17=Entry(root17,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_new_username17.place(x=180,y=500)

        input_new_password17=Entry(root17,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30,show="*")
        input_new_password17.place(x=180,y=550)
        
        input_doctor_aadhar_number17.insert(0,f"{j[1]}")
        input_doctor_aadhar_number17.config(state="disabled")
        input_doctor_name17.insert(1,f"{j[2]}")
        input_doctor_age17.insert(2,f"{j[3]}")
        input_doctor_gender17.insert(3,f"{j[4]}")
        input_phone_number17.insert(4,f"{j[5]}")
        input_blood_group17.insert(5,f"{j[6]}")
        input_department17.insert(6,f"{j[7]}")
        input_new_username17.insert(7,f"{j[8]}")
        input_new_password17.insert(8,f"{j[9]}")

        
        #buttons
        #update
        button_submit17=Button(root17,text="UPDATE",bg="green",fg="white",height=1,width=10,font=("times new roman",15),command=Doctor_Details_Update)
        button_submit17.place(x=300,y=650)
        #exit
        button_exit17=Button(root17,text="Exit",bg="red",fg="white",height=1,width=10,font=("times new roman",15),command=root17.destroy)
        button_exit17.place(x=50,y=650)
        root17.mainloop()
        
    res.close()
    con.close()

#change_doctor_data_page
def change_doctor_data_page():
    root16=Tk()
    root16.geometry("600x400")
    root16.title("Change Details")
    root16.resizable(False,False)

    #title label
    label16=Label(root16,text="Change Details",fg="black",bg="lightgreen",font=("times new roman",30))
    label16.pack()

    #label
    label_aadhar_card16=Label(root16,text="AADHAR CARD",fg="black",font=("times new roman",15))
    label_aadhar_card16.place(x=20,y=130)

    global input_aadhar_number16
    #enters
    input_aadhar_number16=Entry(root16,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=40)
    input_aadhar_number16.place(x=180,y=130)

    #submit button
    button_submit16=Button(root16,text="SUBMIT",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=Change_doctor_data_Submit_Sql)
    button_submit16.place(x=290,y=200)

    #exit button
    button_exit16=Button(root16,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root16.destroy)
    button_exit16.place(x=220,y=280)

    root16.mainloop()

#Change_Doctor_Data_Login_Sql
def Change_Doctor_Data_Login_Sql():
    username121=input_user_name12.get()
    password121=input_password12.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="SELECT * FROM login WHERE username=%s AND password=%s"
    val=(username121,password121)
    res.execute(sql,val)
    a=[]
    for i in res:
        a.append(i)
    if len(a)>0:
        messagebox.showinfo("login","Login successfully")
        input_password12.delete(0,END)
        input_user_name12.delete(0,END)
        input_user_name12.focus_set()
        res.close()
        con.close()
        change_doctor_data_page()        
    else:
        messagebox.showwarning("Warning","username and password are incorrect")
        input_password12.delete(0,END)
        input_user_name12.delete(0,END)
        input_user_name12.focus_set()
        res.close()
        con.close()       

#Change_ doctor_Data_login
def Change_Doctor_Data_Login():
    root12=Tk()
    root12.geometry("500x500")
    root12.title("Login Form")
    root12.resizable(False,False)

    #title label
    label12=Label(root12,text="Login Form",fg="black",bg="lightgreen",font=("times new roman",30))
    label12.pack()

    #info label
    label_info12=Label(root12,text="**Use Admin Only **",fg="black",font=("times new roman",15,"bold"))
    label_info12.place(x=20,y=80)

    # Label
    label_user_name12=Label(root12,text="USER NAME",fg="black",font=("times new roman",12))
    label_user_name12.place(x=20,y=120)

    label_password12=Label(root12,text="PASSWORD",fg="black",font=("times new roman",12))
    label_password12.place(x=20,y=170)

    global input_user_name12
    global input_password12
    #entry
    input_user_name12=Entry(root12,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_user_name12.place(x=180,y=120)

    input_password12=Entry(root12,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30,show="*")
    input_password12.place(x=180,y=170)


     #login button
    button_login12=Button(root12,text="LOGIN",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=Change_Doctor_Data_Login_Sql)
    button_login12.place(x=200,y=250)

    #exit button
    button_exit12=Button(root12,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root12.destroy)
    button_exit12.place(x=180,y=350)

    root12.mainloop()

# Doctor_Account_details_sql   
def Doctor_Account_details_sql():
    dadnumber1=input_doctor_aadhar_number.get()
    dname1=input_doctor_name.get()
    duser1=input_new_username.get()
    dpassword1=input_new_password.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res1=con.cursor()
    sql1="insert into Login_Doctors (username,password,aadhar_number,name) values(%s,%s,%s,%s)"
    val1=(duser1,dpassword1,dadnumber1,dname1)
    res1.execute(sql1,val1)
    con.commit()
    res1.close()
    con.close()
    input_doctor_aadhar_number.delete(0,END)
    input_doctor_name.delete(0,END)
    input_doctor_age.delete(0,END)
    input_doctor_gender.delete(0,END)
    input_phone_number1.delete(0,END)
    input_blood_group1.delete(0,END)
    input_department.delete(0,END)
    input_new_username.delete(0,END)
    input_new_password.delete(0,END)
    input_doctor_aadhar_number.focus_set()


#Doctor_registration_page_Submit
def Doctor_registration_page_Submit():
    dadnumber=input_doctor_aadhar_number.get()
    dname=input_doctor_name.get()
    dage=input_doctor_age.get()
    dgender=input_doctor_gender.get()
    dpnumber=input_phone_number1.get()
    dbgroup=input_blood_group1.get()
    ddept=input_department.get()
    duser=input_new_username.get()
    dpassword=input_new_password.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="insert into doctor_new_registration_details(aadhar_number,dname,dage,dgender,dnumber,dbgroup,ddepartment,dusername,dpassword)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(dadnumber,dname,dage,dgender,dpnumber,dbgroup,ddept,duser,dpassword)
    res.execute(sql,val)
    con.commit()
    res.close()
    con.close()
    messagebox.showinfo("Submit",f'registration successfully "welcome Dr.{dname}"')
    Doctor_Account_details_sql()
    
#Create_Doctor_registration_page
def Create_Doctor_registration_page():
    root10=Tk()
    root10.geometry("500x900")
    root10.title("Doctor Registration Form")
    root10.resizable(False,False)
    # title label
    label10=Label(root10,text="Doctor New Registration",fg="black",bg="lightgreen",font=("times new roman",30))
    label10.pack()

    #labels
    label_doctor_aadhar_card=Label(root10,text="AADHAR CARD",fg="black",font=("times new roman",12))
    label_doctor_aadhar_card.place(x=20,y=150)
    label_list1=["NAME","AGE","GENDER M/F","PHONE NUMBER","BLOOD GROUP","DEPARTMENT","NEW USERNAME","NEW PASSWORD"]
    count=150
    for i in label_list1:
        count=count+50
        l4=Label(root10,text=i,fg="black",font=("times new roman",12))
        l4.place(x=20,y=count)
    global input_doctor_aadhar_number
    global input_doctor_name
    global input_doctor_age
    global input_doctor_gender
    global input_phone_number1
    global input_blood_group1
    global input_department
    global input_new_username
    global input_new_password
    #enters
    input_doctor_aadhar_number=Entry(root10,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_doctor_aadhar_number.place(x=180,y=150)

    input_doctor_name=Entry(root10,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_doctor_name.place(x=180,y=200)

    input_doctor_age=Entry(root10,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_doctor_age.place(x=180,y=250)

    input_doctor_gender=Entry(root10,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_doctor_gender.place(x=180,y=300)

    input_phone_number1=Entry(root10,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_phone_number1.place(x=180,y=350)

    input_blood_group1=Entry(root10,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_blood_group1.place(x=180,y=400)

    input_department=Entry(root10,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_department.place(x=180,y=450)

    input_new_username=Entry(root10,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_new_username.place(x=180,y=500)

    input_new_password=Entry(root10,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30,show="*")
    input_new_password.place(x=180,y=550)
  
    #buttons
    #submit
    button_submit1=Button(root10,text="SUBMIT",bg="green",fg="white",height=1,width=10,font=("times new roman",15),command=Doctor_registration_page_Submit)
    button_submit1.place(x=300,y=650)
    #exit
    button_exit11=Button(root10,text="Exit",bg="red",fg="white",height=1,width=10,font=("times new roman",15),command=root10.destroy)
    button_exit11.place(x=50,y=650)
    root10.mainloop()

#Doctor_New_Account_Login_Sql
def Doctor_New_Account_Login_Sql():
        username9=input_user_name9.get()
        password9=input_password9.get()
        con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
        res=con.cursor()
        sql="SELECT * FROM login WHERE username=%s AND password=%s"
        val=(username9,password9)
        res.execute(sql,val)
        a=[]
        for i in res:
            a.append(i)
        if len(a)>0:
            messagebox.showinfo("login","Login successfully")
            input_password9.delete(0,END)
            input_user_name9.delete(0,END)
            input_user_name9.focus_set()
            res.close()
            con.close()
            Create_Doctor_registration_page()
        else:
            messagebox.showwarning("Warning","username and password are incorrect")
            input_password9.delete(0,END)
            input_user_name9.delete(0,END)
            input_user_name9.focus_set()
            res.close()
            con.close()

# Doctor_New_Account_Login
def Doctor_New_Account_Login():
    root9=Tk()
    root9.geometry("500x500")
    root9.title("Login Form")
    root9.resizable(False,False)

    #title label
    label9=Label(root9,text="Login Form",fg="black",bg="lightgreen",font=("times new roman",30))
    label9.pack()

    #info label
    label_info9=Label(root9,text="**Admin only use**",fg="black",font=("times new roman",15,"bold"))
    label_info9.place(x=20,y=80)



    # Label
    label_user_name9=Label(root9,text="USER NAME",fg="black",font=("times new roman",12))
    label_user_name9.place(x=20,y=120)

    label_password9=Label(root9,text="PASSWORD",fg="black",font=("times new roman",12))
    label_password9.place(x=20,y=170)

    global input_user_name9
    global input_password9
    #entry
    input_user_name9=Entry(root9,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_user_name9.place(x=180,y=120)

    input_password9=Entry(root9,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30,show="*")
    input_password9.place(x=180,y=170)


     #login button
    button_login9=Button(root9,text="LOGIN",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=Doctor_New_Account_Login_Sql)
    button_login9.place(x=200,y=250)

    #exit button
    button_exit10=Button(root9,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root9.destroy)
    button_exit10.place(x=180,y=350)


    root9.mainloop()
#admin main page
def admin_mainpage():
    root8=Tk()
    root8.geometry("800x800")
    root8.title("Hospital Admin")
    root8.resizable(False,False)
    #title label
    label10=Label(root8,text="Admin",fg="black",bg="lightgreen",font=("times new roman",30))
    label10.pack()

    #doctor reg button
    button_create=Button(root8,text="Create Doctor Account",bg="blue",fg="white",height=2,width=18,font=("times new roman",20),command=Doctor_New_Account_Login)
    button_create.place(x=100,y=100)

    #change doctor data
    button_change_data1=Button(root8,text="Change Doctor Data",bg="green",fg="white",height=2,width=15,font=("times new roman",20),command=Change_Doctor_Data_Login)
    button_change_data1.place(x=400,y=100)
   
    #doctor appoinment visit
    button_visit=Button(root8,text="Appoinment details",bg="green",fg="white",height=2,width=15,font=("times new roman",20),command=Visit_Doctor_Data_Login)
    button_visit.place(x=400,y=300)
    
    #view doctor data
    button_view_data1=Button(root8,text="view Doctor Data",bg="green",fg="white",height=2,width=15,font=("times new roman",20),command=View_doctor_data_Login_page)
    button_view_data1.place(x=100,y=300)

    #exit button
    button_exit9=Button(root8,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root8.destroy)
    button_exit9.place(x=350,y=650)


    root8.mainloop()

#Admin Login
def Admin_Login_Sql():
    username=input_user_name.get()
    password=input_password.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="SELECT * FROM login_doctors WHERE username=%s AND password=%s"
    val=(username,password)
    res.execute(sql,val)
    a=[]
    for i in res:
        a.append(i)
    if len(a)>0:
        messagebox.showinfo("login","Login successfully")
        res.close()
        con.close()
        input_password.delete(0,END)
        input_user_name.delete(0,END)
        input_user_name.focus_set()
        admin_mainpage()
    else:
        messagebox.showwarning("Warning","username and password are incorrect")
        res.close()
        con.close()
        input_password.delete(0,END)
        input_user_name.delete(0,END)
        input_user_name.focus_set() 
    
def Admin_Login():
    root7=Tk()
    root7.geometry("500x500")
    root7.title("Login Form")
    root7.resizable(False,False)

    #title label
    label8=Label(root7,text="Login Form",fg="black",bg="lightgreen",font=("times new roman",30))
    label8.pack()
    #info label
    label_info8=Label(root7,text="**Use Admin And Doctors **",fg="black",font=("times new roman",15,"bold"))
    label_info8.place(x=20,y=80)

    # Label
    label_user_name=Label(root7,text="USER NAME",fg="black",font=("times new roman",12))
    label_user_name.place(x=20,y=120)

    label_password=Label(root7,text="PASSWORD",fg="black",font=("times new roman",12))
    label_password.place(x=20,y=170)

    global input_user_name
    global input_password
    #entry
    input_user_name=Entry(root7,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_user_name.place(x=180,y=120)

    input_password=Entry(root7,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30,show="*")
    input_password.place(x=180,y=170)


     #login button
    button_login=Button(root7,text="LOGIN",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=Admin_Login_Sql)
    button_login.place(x=200,y=250)

    #exit button
    button_exit8=Button(root7,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root7.destroy)
    button_exit8.place(x=180,y=350)


    root7.mainloop()

#registration-submit
def Reg_Submit():
    adnumber14=input_aadhar_number.get()
    pname=input_patient_name.get()
    page=input_patient_age.get()
    pgender=input_patient_gender.get()
    pnumber=input_phone_number.get()
    pbgroup=input_blood_group.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="INSERT INTO patient_new_registration_details(aadhar_number,pname,page,pgender,pnumber,pbgroup)values(%s,%s,%s,%s,%s,%s)"
    val=(adnumber14,pname,page,pgender,pnumber,pbgroup)
    res.execute(sql,val)
    messagebox.showinfo("Submit",f'registration successfully "welcome {pname}"')
    con.commit()
    res.close()
    con.close()
    input_aadhar_number.delete(0,END)
    input_patient_name.delete(0,END)
    input_patient_age.delete(0,END)
    input_patient_gender.delete(0,END)
    input_phone_number.delete(0,END)
    input_blood_group.delete(0,END)
    input_aadhar_number.focus_set()

#check_aadhar
def check_aadhar():
    adnumber1=input_aadhar_number.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql='SELECT * FROM patient_new_registration_details WHERE aadhar_number=%s'
    val=(adnumber1,)
    res.execute(sql,val)
    a=[]
    for i in res:
        a.append(i)
    if(len(a)>0):
        messagebox.showwarning("warning",f"Aadhar Number {a} already exits ")
        input_aadhar_number.delete(0,END)
    else:
        messagebox.showinfo("Info","Aadhar number not exists")
    res.close()
    con.close()

def Patient_Registration():
    root1=Tk()
    root1.geometry("700x700")
    root1.title("Patient Registration Form")
    root1.resizable(False,False)
    # title label
    label2=Label(root1,text="Patient New Registration",fg="black",bg="lightgreen",font=("times new roman",30))
    label2.pack()

    #labels
    label_aadhar_card=Label(root1,text="AADHAR CARD",fg="black",font=("times new roman",12))
    label_aadhar_card.place(x=20,y=150)
    label_list=["NAME","AGE","GENDER M/F","PHONE NUMBER","BLOOD GROUP"]
    count=150
    for i in label_list:
        count=count+65
        l1=Label(root1,text=i,fg="black",font=("times new roman",12))
        l1.place(x=20,y=count)
    #enters
    global input_aadhar_number
    global input_patient_name
    global input_patient_age
    global input_patient_gender
    global input_phone_number
    global input_blood_group


    input_aadhar_number=Entry(root1,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_aadhar_number.place(x=180,y=150)

    input_patient_name=Entry(root1,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_patient_name.place(x=180,y=215)

    input_patient_age=Entry(root1,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_patient_age.place(x=180,y=280)

    input_patient_gender=Entry(root1,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_patient_gender.place(x=180,y=345)

    input_phone_number=Entry(root1,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_phone_number.place(x=180,y=410)

    input_blood_group=Entry(root1,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
    input_blood_group.place(x=180,y=475)
  
    #buttons
    #check
    button_check=Button(root1,text="check",bg="green",fg="white",height=1,width=10,font=("times new roman",15),command=check_aadhar)
    button_check.place(x=363,y=175)

    #submit
    button_submit=Button(root1,text="SUBMIT",bg="green",fg="white",height=1,width=10,font=("times new roman",15),command=Reg_Submit)
    button_submit.place(x=300,y=600)
    #exit
    button_exit2=Button(root1,text="Exit",bg="red",fg="white",height=1,width=10,font=("times new roman",15),command=root1.destroy)
    button_exit2.place(x=50,y=600)
    root1.mainloop()

def List_of_Doctors():
    root2=Tk()
    root2.title("List of Doctors")
    root2.geometry("800x800")
    root2.resizable(False,False)
    
    #title label
    label3=Label(root2,text="Doctors Details",fg="black",bg="lightgreen",font=("times new roman",30))
    label3.place(x=300,y=10)

    #data labels
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="select dname,id,ddepartment,droomno from doctor_new_registration_details"
    res.execute(sql)
    alldata2=res.fetchall()
    col=["NAME","ID","DEPARTMENT","ROOM NUMBER"]
    table=ttk.Treeview(root2,columns=col,show="headings")   
    for de in table.get_children():
        table.delete(de)
    for cols in col:
        table.heading(cols,text=cols)
        table.grid(row=1,column=0)    
    for h,(dname,id,ddepartment,droomno) in enumerate(alldata2,start=1):
        table.insert("","end",values=(dname,id,ddepartment,droomno))
    table.pack(pady=110, padx=10, fill="both", expand=True)
    res.close()
    con.close()
    #contact label
    label_contact_no1=Label(root2,text="Any help please contact: 9876543210.",fg="black",font=("times new roman",15,"bold"))
    label_contact_no1.place(x=30,y=650)
    #exit button
    button_exit3=Button(root2,text="Exit",bg="red",fg="white",height=2,width=15,font=("times new roman",15),command=root2.destroy)
    button_exit3.place(x=300,y=700)
    
    root2.mainloop()
    

def Services_Available():
    root3=Tk()
    root3.geometry("500x700")
    root3.title("Services Available")
    root3.resizable(False,False)

    #title label

    label4=Label(root3,text="Services Available",fg="black",bg="lightgreen",font=("times new roman",30))
    label4.pack()

    #heading,data labels

    service_depatment_available=["SERVICES AVAILABLE","ULTRASOUND","X-RAY","CT-SCAN","MRI","BLOOD COLLECTION","DIALYSIS","ECG","CHEMIST","LAB"]
    count2=100
    for i in service_depatment_available:
        count2=count2+40
        l5=Label(root3,text=i,fg="black",font=("times new roman",12))
        l5.place(x=30,y=count2)
    
    service_room_no=["ROOM NUMBER",1,2,3,4,5,6,7,8,9]
    count2=100
    for i in service_room_no:
        count2=count2+40
        l6=Label(root3,text=i,fg="black",font=("times new roman",12))
        l6.place(x=300,y=count2)
    #contact label
    label_contact_no2=Label(root3,text="Any help please contact: 9876543210.",fg="black",font=("times new roman",15,"bold"))
    label_contact_no2.place(x=30,y=500)

    #exit button
    button_exit4=Button(root3,text="Exit",bg="red",fg="white",height=2,width=15,font=("times new roman",15),command=root3.destroy)
    button_exit4.place(x=150,y=580)

    root3.mainloop()

#search submit
def Search_Submit():
    adnumber=input_aadhar_number1.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="Select * from patient_new_registration_details where aadhar_number=%s"
    val=(adnumber,)
    res.execute(sql,val)
    alldata=res.fetchall()
    a=[]
    for i in alldata:
        a.append(i)
    if len(a)==0:
        messagebox.showerror("Error","No data found")
    else:
        messagebox.showinfo("Info",f"Details: id={i[0]},\n aadhar number={i[1]},\n name={i[2]},\n age={i[3]},\n gender={i[4]},\n phone number={i[5]},\n blood group={i[6]} ")
    input_aadhar_number1.delete(0,END)
    res.close()
    con.close() 

def View_Data():
    root4=Tk()
    root4.geometry("600x400")
    root4.title("View Data")
    root4.resizable(False,False)

    #title label
    label5=Label(root4,text="Search Data",fg="black",bg="lightgreen",font=("times new roman",30))
    label5.pack()

    #label
    label_aadhar_card1=Label(root4,text="AADHAR CARD",fg="black",font=("times new roman",15))
    label_aadhar_card1.place(x=20,y=130)

    global input_aadhar_number1
    #enters
    input_aadhar_number1=Entry(root4,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=40)
    input_aadhar_number1.place(x=180,y=130)

    #submit button
    button_submit1=Button(root4,text="SUBMIT",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=Search_Submit)
    button_submit1.place(x=290,y=200)

    #exit button
    button_exit5=Button(root4,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root4.destroy)
    button_exit5.place(x=220,y=280)

    root4.mainloop()
#Appointment_Details_Submit
def Appointment_Details_Submit():
    doctor_department20=input_doctor_department.get()
    doctor_id20=input_doctor_id.get()
    Appointment_time20=input_time.get()
    Appointment_date20=input_date.get()
    doctor_name20=input_doctor_name.get()
    doctor_roomno20=input_doctor_roomno.get()
    patient_id20=patient_id
    patient_aadhar_number20=patient_aadhar_number
    patient_name20=patient_name
    patient_age20=patient_age
    patient_gender20=patient_gender
    patient_mobile_number20=patient_mobile_number
    patient_blood_group20=patient_blood_group
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="insert into appoinment_details (patient_aadhar_number,patient_id,pname,page,pgender,pnumber,pbgroup,doctor_name,doctor_roomno,doctor_department,doctor_id,appoinment_date,appointment_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"  
    val=(patient_aadhar_number20,patient_id20,patient_name20,patient_age20,patient_gender20,patient_mobile_number20,patient_blood_group20,doctor_name20,doctor_roomno20,doctor_department20,doctor_id20,Appointment_date20,Appointment_time20)
    res.execute(sql,val)
    con.commit()
    messagebox.showinfo("Appoinment details",f" patient name={patient_name20}\n appoinment date={Appointment_date20}\n appoinment time={Appointment_time20}\n Doctor name={doctor_name20}\n Doctor department={doctor_department20}\n Doctor room no={doctor_roomno20}")
    res.close()
    con.close()

#Appointment_page
def Appointment_page():
    root20=Tk()
    root20.title("Appoinment page")
    root20.geometry("1200x800")
    root20.resizable(False,False)
    
    #title label
    label20=Label(root20,text="Appoinment",fg="black",bg="lightgreen",font=("times new roman",30))
    label20.place(x=500,y=10)

    #data labels
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="select dname,id,ddepartment,droomno from doctor_new_registration_details"
    res.execute(sql)
    alldata2=res.fetchall()
    col=["NAME","ID","DEPARTMENT","ROOM NUMBER"]
    table=ttk.Treeview(root20,columns=col,show="headings")   
    for de in table.get_children():
        table.delete(de)
    for cols in col:
        table.heading(cols,text=cols)
        table.grid(row=1,column=0)    
    for h,(dname,id,ddepartment,droomno) in enumerate(alldata2,start=1):
        table.insert("","end",values=(dname,id,ddepartment,droomno))
    table.pack(pady=70, padx=10, fill="both", expand=True)
    def Value(event):
        input_doctor_department.delete(0,END)
        input_doctor_id.delete(0,END)
        input_time.delete(0,END)
        input_date.delete(0,END)
        row=table.selection()
        if row:
            select=row[0]
            values = table.item(select, "values")
            input_doctor_department.insert(0,values[2])
            input_doctor_id.insert(0,values[1])
            input_doctor_name.insert(0,values[0])
            input_doctor_roomno.insert(0,values[3])
    table.bind('<Double-Button-1>',Value)
    
    res.close()
    con.close()
    
    global input_doctor_department
    global input_doctor_id
    global input_doctor_roomno
    global input_doctor_name
    global input_time
    global input_date

    label_information=Label(root20,text="** Appoinment time 07:00(07:00 AM)  to 13:00(01:00 PM) And 16:00(04:00 PM) to 20:00(08:00 PM) **",fg="black",font=("times new roman",15))
    label_information.place(x=20,y=400)
    

    label_doctor_department=Label(root20,text="Enter doctor department",fg="black",font=("times new roman",15))
    label_doctor_department.place(x=20,y=450)
    input_doctor_department=Entry(root20,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=25)
    input_doctor_department.place(x=250,y=450)

    label_doctor_name=Label(root20,text="Enter doctor Name",fg="black",font=("times new roman",15))
    label_doctor_name.place(x=600,y=450)
    input_doctor_name=Entry(root20,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=25)
    input_doctor_name.place(x=800,y=450)

    label_doctor_roomno=Label(root20,text="Enter doctor Room No",fg="black",font=("times new roman",15))
    label_doctor_roomno.place(x=600,y=500)
    input_doctor_roomno=Entry(root20,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=25)
    input_doctor_roomno.place(x=800,y=500)

    label_doctor_id=Label(root20,text="Enter doctor id",fg="black",font=("times new roman",15))
    label_doctor_id.place(x=20,y=500)
    input_doctor_id=Entry(root20,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=25)
    input_doctor_id.place(x=250,y=500)

    label_time=Label(root20,text="Appoinment Time",fg="black",font=("times new roman",15))
    label_time.place(x=20,y=550)
    input_time=Entry(root20,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=25)
    input_time.place(x=250,y=550)
    label_time_format=Label(root20,text="Format=HH:MI  24 hr format",fg="black",font=("times new roman",15))
    label_time_format.place(x=650,y=550)

    label_date=Label(root20,text="Appoinment Date",fg="black",font=("times new roman",15))
    label_date.place(x=20,y=600)
    input_date=Entry(root20,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=25)
    input_date.place(x=250,y=600)
    label_date_format=Label(root20,text="Format=YYYY-MM-DD",fg="black",font=("times new roman",15))
    label_date_format.place(x=650,y=600)
    #submit
    button_submit20=Button(root20,text="SUBMIT",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=Appointment_Details_Submit)
    button_submit20.place(x=350,y=650)
    #exit button
    button_exit3=Button(root20,text="Exit",bg="red",fg="white",height=2,width=15,font=("times new roman",15),command=root20.destroy)
    button_exit3.place(x=500,y=700)
    
    root20.mainloop()
    
#appoinment submit
def Appointment_Submit():
    adnumber5=input_aadhar_number2.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="Select * from patient_new_registration_details where aadhar_number=%s"
    val=(adnumber5,)
    res.execute(sql,val)
    alldata=res.fetchall()
    a=[]
    for i in alldata:
        a.append(i)
    if len(a)==0:
        messagebox.showerror("Error","No data found")
    else:
        global patient_id
        global patient_aadhar_number
        global patient_name
        global patient_age
        global patient_gender
        global patient_mobile_number
        global patient_blood_group

        patient_id=i[0]
        patient_aadhar_number=i[1]
        patient_name=i[2]
        patient_age=i[3]
        patient_gender=i[4]
        patient_mobile_number=i[5]
        patient_blood_group=i[6]
        messagebox.showinfo("Info","data found")
        input_aadhar_number2.delete(0,END)
        Appointment_page()
        
    res.close()
    con.close()

def Appointment():
    root5=Tk()
    root5.geometry("600x400")
    root5.title("Appoinment")
    root5.resizable(False,False)

    #title label
    label6=Label(root5,text="Appoinment",fg="black",bg="lightgreen",font=("times new roman",30))
    label6.pack()

    #label
    label_aadhar_card2=Label(root5,text="AADHAR CARD",fg="black",font=("times new roman",15))
    label_aadhar_card2.place(x=20,y=130)
    global input_aadhar_number2
    #enters
    input_aadhar_number2=Entry(root5,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=40)
    input_aadhar_number2.place(x=180,y=130)

    #submit button
    button_submit2=Button(root5,text="SUBMIT",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=Appointment_Submit)
    button_submit2.place(x=290,y=200)

    #exit button
    button_exit6=Button(root5,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root5.destroy)
    button_exit6.place(x=220,y=280)

    root5.mainloop()
#Change_data_Update
def Change_data_Update():
    adnumber18=input_aadhar_number18.get()
    pname18=input_patient_name18.get()
    page18=input_patient_age18.get()
    pgender18=input_patient_gender18.get()
    pnumber18=input_phone_number18.get()
    pbgroup18=input_blood_group18.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="update patient_new_registration_details set pname=%s,page=%s,pgender=%s,pnumber=%s,pbgroup=%s where aadhar_number=%s"
    val=(pname18,page18,pgender18,pnumber18,pbgroup18,adnumber18)
    res.execute(sql,val)
    con.commit()
    messagebox.showinfo("Update","Patient Details Updated successfully...")
    res.close()
    con.close()
    input_aadhar_number18.delete(0,END)
    input_patient_name18.delete(0,END)
    input_patient_age18.delete(0,END)
    input_patient_gender18.delete(0,END)
    input_phone_number18.delete(0,END)
    input_blood_group18.delete(0,END)
#Change data Submit
def Change_data_Submit():
    adnumber3=input_aadhar_number3.get()
    con=mysql.connector.connect(host="localhost",user="root",password="abc",database="HMS")
    res=con.cursor()
    sql="Select * from patient_new_registration_details where aadhar_number=%s"
    val=(adnumber3,)
    res.execute(sql,val)
    alldata3=res.fetchall()
    a3=[]
    for j in alldata3:
        a3.append(j)
    if len(a3)==0:
        messagebox.showerror("Error","No data found")
        input_aadhar_number3.delete(0,END)
        input_aadhar_number3.focus_set()
    else:
        input_aadhar_number3.delete(0,END)
        input_aadhar_number3.focus_set()
        root18=Tk()
        root18.geometry("500x700")
        root18.title("Patient Updation Form")
        root18.resizable(False,False)
        # title label
        label18=Label(root18,text="Patient Change Details",fg="black",bg="lightgreen",font=("times new roman",30))
        label18.pack()

        #labels
        label_aadhar_card18=Label(root18,text="AADHAR CARD",fg="black",font=("times new roman",12))
        label_aadhar_card18.place(x=20,y=150)
        label_list18=["NAME","AGE","GENDER M/F","PHONE NUMBER","BLOOD GROUP"]
        count18=150
        for i in label_list18:
            count18=count18+65
            l18=Label(root18,text=i,fg="black",font=("times new roman",12))
            l18.place(x=20,y=count18)
        #enters
        global input_aadhar_number18
        global input_patient_name18
        global input_patient_age18
        global input_patient_gender18
        global input_phone_number18
        global input_blood_group18


        input_aadhar_number18=Entry(root18,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_aadhar_number18.place(x=180,y=150)

        input_patient_name18=Entry(root18,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_patient_name18.place(x=180,y=215)

        input_patient_age18=Entry(root18,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_patient_age18.place(x=180,y=280)

        input_patient_gender18=Entry(root18,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_patient_gender18.place(x=180,y=345)

        input_phone_number18=Entry(root18,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_phone_number18.place(x=180,y=410)

        input_blood_group18=Entry(root18,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=30)
        input_blood_group18.place(x=180,y=475)

        input_aadhar_number18.insert(0,f"{j[1]}")
        input_aadhar_number18.config(state="disabled")
        input_patient_name18.insert(1,f"{j[2]}")
        input_patient_age18.insert(2,f"{j[3]}")
        input_patient_gender18.insert(3,f"{j[4]}")
        input_phone_number18.insert(4,f"{j[5]}")
        input_blood_group18.insert(5,f"{j[6]}")
  
        #buttons
        #Update
        button_update18=Button(root18,text="UPDATE",bg="green",fg="white",height=1,width=10,font=("times new roman",15),command=Change_data_Update)
        button_update18.place(x=300,y=600)
        #exit
        button_exit18=Button(root18,text="Exit",bg="red",fg="white",height=1,width=10,font=("times new roman",15),command=root18.destroy)
        button_exit18.place(x=50,y=600)
        root18.mainloop()


def Change_Data():
    root6=Tk()
    root6.geometry("600x400")
    root6.title("Change Details")
    root6.resizable(False,False)

    #title label
    label7=Label(root6,text="Change Details",fg="black",bg="lightgreen",font=("times new roman",30))
    label7.pack()

    #label
    label_aadhar_card3=Label(root6,text="AADHAR CARD",fg="black",font=("times new roman",15))
    label_aadhar_card3.place(x=20,y=130)

    global input_aadhar_number3
    #enters
    input_aadhar_number3=Entry(root6,fg="black",bg="lightgreen",font=("times new roman",15,"bold"),width=40)
    input_aadhar_number3.place(x=180,y=130)

    #submit button
    button_submit3=Button(root6,text="SUBMIT",bg="green",fg="white",height=1,width=15,font=("times new roman",15),command=Change_data_Submit)
    button_submit3.place(x=290,y=200)

    #exit button
    button_exit7=Button(root6,text="Exit",bg="red",fg="white",height=2,width=10,font=("times new roman",15),command=root6.destroy)
    button_exit7.place(x=220,y=280)

    root6.mainloop()

#main page
root=Tk()
root.geometry("1500x900")
root.resizable(False,False)
root.title("MAIN PAGE")
#main label
label1=Label(root,text="Hospital Management",fg="white",bg="green",font=("times new roman",50))
label1.pack()

#main page buttons and place 
button_patient_registration=Button(root,text="Registration",bg="green",fg="white",height=2,width=15,font=("times new roman",20),command=Patient_Registration)
button_patient_registration.place(x=200,y=150)

button_list_of_doctors=Button(root,text="List of Doctors",bg="green",fg="white",height=2,width=15,font=("times new roman",20),command=List_of_Doctors)
button_list_of_doctors.place(x=1000,y=150)

button_services_available=Button(root,text="Services Available",bg="green",fg="white",height=2,width=15,font=("times new roman",20),command=Services_Available)
button_services_available.place(x=200,y=350)

button_view_data=Button(root,text="View Data",bg="green",fg="white",height=2,width=15,font=("times new roman",20),command=View_Data)
button_view_data.place(x=1000,y=350)

button_appointment=Button(root,text="Appoinment",bg="green",fg="white",height=2,width=15,font=("times new roman",20),command=Appointment)
button_appointment.place(x=200,y=550)

button_change_data=Button(root,text="Change Data",bg="green",fg="white",height=2,width=15,font=("times new roman",20),command=Change_Data)
button_change_data.place(x=1000,y=550)

button_admin=Button(root,text="Admin",bg="yellow",fg="green",height=2,width=15,font=("times new roman",20),command=Admin_Login)
button_admin.place(x=600,y=100)

button_exit1=Button(root,text="Exit",bg="red",fg="white",height=2,width=15,font=("times new roman",20),command=root.destroy)
button_exit1.place(x=600,y=600)

root.mainloop()