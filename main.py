from tkinter import *
import pickle as pick
import datetime

window = Tk()
window.title("Employee system")

def read_file():
    try:
        file = open('workers.txt','rb')
        by = file.read()
        file.close()
        return pick.loads(by)
    except:
        return []

def write_file(list):
    bi = pick.dumps(list)
    file = open('workers.txt','wb')
    file.write(bi)
    file.close()

def show_login():
    main_frame.pack_forget()
    login_frame.pack(fill="both",expand=True)
    worker_frame.pack_forget()
    newcreat_frame.pack_forget()

def show_panel():
    login_frame.pack_forget()
    main_frame.pack(fill="both",expand=True)
    worker_frame.pack_forget()
    newcreat_frame.pack_forget()
    menubar = Menu(window)
    menubar.add_command(label="New employee definition",command=show_for_new_worker)
    menubar.add_command(label="Change administrator information",command=show_for_change_admin)
    window.config(menu=menubar)
    list = read_file()
    count = 0
    location = 0
    try:
        for i in list:
            count += 1
            location += 40
            Label(main_frame,text=i.name,font=14).place(x=20,y=0+location)
            Button(main_frame,text="Enter",bg="green",command=lambda i=i:change_config(i)).place(x=350,y=0+location)
    except:
        pass

def show_Wpanel():
    login_frame.pack_forget()
    worker_frame.pack(fill="both",expand=True)
    main_frame.pack_forget()
    newcreat_frame.pack_forget()

def show_new():
    window.config(menu=" ")
    main_frame.pack_forget()
    login_frame.pack_forget()
    worker_frame.pack_forget()
    newcreat_frame.pack(fill="both",expand=True)
    button_back.config(command=show_panel)
    button_back.place(x=2,y=40)
    label_for_fullname.place(x=25,y=20)
    entry_new_name.place(x=25,y=50)
    label_for_user.place(x=25,y=100)
    entry_new_user.place(x=25,y=130)
    label_for_password.place(x=25,y=180)
    entry_for_password.place(x=25,y=210)
    save_newcreat_button.place(x=180,y=280)

def show_for_change_admin():
    show_new()
    save_newcreat_button.config(command=change_admin)

def check_admin():
    global admin
    try:
        file = open('admin.txt','rb')
        by_ = file.read()
        file.close()
        item = pick.loads(by_)
    except:
        bi = pick.dumps(admin)
        file = open('admin.txt','wb')
        file.write(bi)
        file.close()

def change_admin():
    global entry_new_user ,entry_for_password
    file = open('admin.txt','rb')
    by_ = file.read()
    file.close()
    item = pick.loads(by_)
    item["username"] = entry_new_user.get()
    item["password"] = entry_for_password.get()
    bi = pick.dumps(item)
    file = open('admin.txt','wb')
    file.write(bi)
    file.close()

def change_worker():
    global entry_new_user ,entry_for_password ,entry_new_name,list2,error_label
    list2 = read_file()
    name = entry_new_name.get()
    user = entry_new_user.get()
    password = entry_for_password.get()
    if name == "" or user == "" or password == "":
        error_label.config(text="None of the items can be empty.")
        error_label.place(x=25,y=240)
    else :
        try:
            for i in list:
                if i.user  == user:
                    error_label.config(text="The username entered is a duplicate.")
                    error_label.place(x=25,y=240)
                    break
            else :
                praworker = PraWorker(name,user,password)
                list2.append(praworker)
                write_file(list2)
        except:
            praworker = PraWorker(name,user,password)
            list2.append(praworker)
            write_file(list2)

def show_for_new_worker():
    show_new()
    save_newcreat_button.config(command=change_worker)

def change_config(i):
    show_Wpanel()
    global a,q,last_app,show_user,text,password_show,save_button
    a.config(text=f"full name:{i.name}")
    q.config(text="Write a message")
    last_app.config(text=f"last appearance:{i.hozoor}")
    show_user.config(text=f"username:{i.user}")
    window.config(menu=" ")
    text.delete("1.0",END)
    text.insert(INSERT,i.message)
    text.place(x=20, y=50, width=350, height=200)
    password_show.config(text=f"password:{i.password}")
    save_button.config(text="                                                      save                                                     ")
    def save_message():
        file = read_file()
        for j in file:
            if i.user == j.user:
                j.message = str(text.get(1.0,END))
                write_file(file)
                break

    save_button.config(command=save_message)
    save_button.place(x=20,y=250)
    back_button.config(command=show_panel)
    back_button.place(x=2,y=40)

def login():
    global list
    username = username_entry.get()
    password = password_entry.get()
    if choice.get() == "admin":
        file_ = open('admin.txt','rb')
        by_ = file_.read()
        file_.close()
        item_ = pick.loads(by_)
        if username == item_['username'] and password == item_["password"]:
            # main_frame
            
            show_panel()
            list = read_file()
            location = 0
            count = 0
            menubar = Menu(window)
            menubar.add_command(label="New employee definition",command=show_for_new_worker)
            menubar.add_command(label="Change administrator information",command=show_for_change_admin)
            window.config(menu=menubar)
            try:
                for i in list:
                    count += 1
                    location += 40
                    Label(main_frame,text=i.name,font=14).place(x=20,y=0+location)
                    Button(main_frame,text="Enter",bg="green",command=lambda i=i:change_config(i)).place(x=350,y=0+location)
            except:
                pass
                
                    
        else :
            error.config(text="Invalid username or password",fg="red")
    elif choice.get() == "worker":
        try:
            global namelogin_worker ,userlogin_worker 
            list = read_file()
            for i in list:
                if username == i.user and password == i.password:
                    show_Wpanel()
                    namelogin_worker = i.name
                    userlogin_worker = i.user
                    last_hozor = i.hozoor
                    global worker_about
                    worker_about = i.name
                    def new_presence():
                        list = read_file()
                        for i in list:
                            if i.name == worker_about:
                                last_hozor = datetime.date.today()
                                i.hozoor = last_hozor
                                write_file(list)
                                last_app.config(text=f"last appearance:{str(last_hozor)}")
                                
                    Button(worker_label,font=("Arial",14),text="Register a new presence",command=new_presence).place(x=20,y=170)
                    text.delete("1.0",END)
                    text.insert(INSERT,i.message)
                    text.place(x=20, y=50, width=350, height=200)
                    q.config(text="last admin message for you:")
                    a.config(text=f"full name:{str(namelogin_worker)}")
                    last_app.config(text=f"last appearance:{str(i.hozoor)}")
                    show_user.config(text=f"username:{str(userlogin_worker)}")
                    
            else :
                error.config(text="Invalid username or password",fg="red")
        except:
            error.config(text="Invalid username or password",fg="red")
        
worker_about = ""

try:
    creat_file_admin = open("admin.txt",'x')
    creat_file_admin.close()
    creat_file_worker = open("workers.txt","x")
    creat_file_worker.close()
except:
    pass


admin = {'username':"admin","password":"1234"}
check_admin()

class PraWorker:
    def __init__(self,name,user,password,hozoor='Absence',message='None'):
        self.name = name
        self.user = user
        self.password = password
        self.hozoor = hozoor
        self.message = message
    def presence(self,date):
        self.hozoor = date

list = []
list2 = []

login_frame = Frame(window)
main_frame = Frame(window)
worker_frame = Frame(window)
newcreat_frame = Frame(window)


namelogin_worker = ""
userlogin_worker = ""

modes = [("admin","admin",100),("Employee","worker",200)]
choice = StringVar()
choice.set("admin")
for t,m,v in modes:
    Radiobutton(login_frame,text=t,variable=choice,value=m,font=14).place(x=v,y=240)

# login_frame

Label(login_frame,text=" ",font=14).pack()
Label(login_frame,text="username",font=14).pack()
username_entry = Entry(login_frame,font=14)
username_entry.pack()
Label(login_frame,text=" ",font=14).pack()
Label(login_frame,text="password",font=14).pack()
password_entry = Entry(login_frame,font=14)
password_entry.pack()
error = Label(login_frame,text=" ",font=14,fg="black")
error.pack()
Button(login_frame,text="login",command=login).pack()

# worker_frame

worker_label = LabelFrame(worker_frame,text="about")
worker_label.pack(fill="both",expand=True)
text_message = Frame(worker_frame)
text_message.pack(fill="both",expand=True)
a = Label(worker_label,font=14,text=" ")
a.place(x=20,y=20)
show_user = Label(worker_label,font=14,text=" ")
show_user.place(x=20,y=70)
last_app = Label(worker_label,font=14,text=" ")
last_app.place(x=20,y=120)
q = Label(text_message,font=14)
q.place(x=20,y=10)
text = Text(text_message,font=14)
password_show = Label(worker_label,font=14,text=" ")
password_show.place(x=20,y=170)
save_button = Button(text_message,text=" ")
back_button = Button(worker_frame,text="<")

# newcreat_frame

button_back = Button(newcreat_frame,text="<")
label_for_fullname = Label(newcreat_frame,text="Enter full name:",font=14)
entry_new_name = Entry(newcreat_frame,font=14,width=40)
label_for_user = Label(newcreat_frame,text="Enter username:",font=14)
entry_new_user = Entry(newcreat_frame,font=14,width=40)
label_for_password = Label(newcreat_frame,text="Enter password:",font=14)
entry_for_password = Entry(newcreat_frame,font=14,width=40)
error_label = Label(newcreat_frame,text="The username entered is a duplicate.",fg="red",font=8)
save_newcreat_button = Button(newcreat_frame,font=5,text="save")

show_login()
window.resizable(False,False)
window.geometry("400x600")
window.mainloop()
