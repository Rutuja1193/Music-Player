from tkinter import *
from tkinter import messagebox
import mysql.connector


connection = mysql.connector.connect(host='localhost', user='root', password='Secreteng@4307', database='python')
c = connection.cursor()

def insertData():
    if usernameEntry.get()=='' or passwordEntry.get=='':
        messagebox.showerror('Error','All Fields are required')
    else:
        username = usernameEntry.get()
        password = passwordEntry.get()

        insert_query = "INSERT INTO `login`( `username`, `password`) VALUES (%s,%s)"
        vals = (username, password)
        c.execute(insert_query, vals)
        connection.commit()
        messagebox.showinfo('Success', 'Successfully Inserted')
        account_window.destroy()
        import python_login

def login_page():
    account_window.destroy()
    import python_login


account_window=Tk()
account_window.title('Create account')
account_window.geometry('990x660+50+50')
account_window.resizable(False,False)
bgImage=PhotoImage(file='musicback.png')

bgLabel=Label(account_window,image=bgImage)
bgLabel.grid()



frame=Frame(account_window)
frame.place(x=320,y=90)

heading=Label(frame,text='CREATE ACCOUNT',font=('Microsoft Yahei Ui Light',25,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei Ui Light',15,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10.0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',15,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei Ui Light',15,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei Ui Light',15,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

freeLabel=Label(frame)
freeLabel.grid(row=9,column=0,sticky='w',padx=25,pady=(10,0))

signupButton=Button(frame,text='Sign up',font=('Open Sans',15,'bold'),bd=0,fg='white',bg='firebrick1',activeforeground='white'
                    ,activebackground='firebrick1',width=17,command=insertData)
signupButton.grid(row=10,column=0,padx=10)


signupLabel=Label(frame,text='Have an account?',font=('Open Sans',11,'bold'),fg='firebrick1',bg='white' )
signupLabel.grid(row=11,column=0,sticky='w',padx=25,pady=10)

Button(account_window,text="Login",command=login_page,height=1,width=8,bd=2).place(x=540,y=375)



account_window.mainloop()
