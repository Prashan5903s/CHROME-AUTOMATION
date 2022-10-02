from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
from datetime import datetime
import math
import mysql.connector
import pandas as pd
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from tkinter.filedialog import askopenfilename
from threading import *
import time
from webdriver_manager.chrome import ChromeDriverManager

window = Tk()
window.title("LogIn")
window.geometry("925x500+300+200")
window.configure(bg='#fff')

config = {
    'user': "us4ysjqeg4frhsrm",
    'password': "B1aUz79uvSHr53C7VThr",
    'host': "bi63d9qn701g0iqwf9lx-mysql.services.clever-cloud.com",
    'database': "bi63d9qn701g0iqwf9lx"
}

mydb = mysql.connector.connect(**config)

now = datetime.now()
rty = now.strftime('%d/%m/%Y %I:%M:%S')

def threading1():

    t1 = Thread(target=sign)
    t1.start()

def threading2():

    t2 = Thread(target=log)
    t2.start()

def threading3():

    t3 = Thread(target=forgot)
    t3.start()

def sign():

    def threading8():

        t8 = Thread(target=sub)
        t8.start()

    def sub():

        a = user16.get()
        b = user29.get()
        c = user39.get()

        cursor2 = mydb.cursor()
        sql = f"SELECT user_email FROM tbl_user WHERE user_email='{b}'"
        cursor2.execute(sql)
        result = cursor2.fetchall()

        d = len(result)

        if d == 0:

            cursor1 = mydb.cursor()
            sql = "INSERT INTO tbl_user (user_name, user_email, user_password, stat) VALUES (%s ,%s, %s, %s)"
            val = (f"{a}", f"{b}", f"{c}", "Inactive")
            cursor1.execute(sql, val)
            mydb.commit()

            messagebox.showinfo('information', f'{b} is your new UID\n{c} is your new password')

        else:

            messagebox.showinfo('information', f'{b} user already exist')

    new = Toplevel(window)
    new.title("Signup")
    new.geometry("925x500+200+100")
    new.configure(bg='#fff')

    frame16 = Frame(new, width=650, height=650, bg='white')
    frame16.place(x=290, y=70)

    heading17 = Label(frame16, text="Sign In", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, "bold"))
    heading17.place(x=100, y=5)

    user16 = Entry(frame16, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user16.place(x=30, y=80)
    user16.insert(0, 'Name')

    Frame(frame16, width=295, height=2, bg="black").place(x=25, y=107)

    user29 = Entry(frame16, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user29.place(x=30, y=150)
    user29.insert(0, "Email Id")

    Frame(frame16, width=295, height=2, bg="black").place(x=25, y=177)

    user39 = Entry(frame16, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user39.place(x=30, y=217)
    user39.insert(0, "Password")

    Frame(frame16, width=295, height=2, bg="black").place(x=25, y=247)

    Button(frame16, width=39, pady=7, text="Submit", bg="#57a1f8", fg="white", border=0, command=threading8).place(x=36,
                                                                                                                   y=305)

def forgot():

    def threading6():

        t6 = Thread(target=verify)
        t6.start()

    def verify():

        z = user11.get()

        cursor5 = mydb.cursor()
        sql3 = f"SELECT user_email FROM tbl_user WHERE user_email='{z}'"
        cursor5.execute(sql3)
        result5 = cursor5.fetchall()

        y = len(result5)

        if y == 0:

            messagebox.showinfo('information', f'{z} user does not exist')

        else:

            def threading7():

                t7 = Thread(target=ver2)
                t7.start()

            def ver2():

                x = user12.get()
                m = user21.get()

                if x == m:

                    cursor440 = mydb.cursor()
                    sql_update_query = f"""Update tbl_user set user_password = '{x}' where user_email = '{z}'"""
                    cursor440.execute(sql_update_query)
                    mydb.commit()

                    messagebox.showinfo('information', f'{x} is your new password')

                else:

                    messagebox.showinfo('information', 'Enter same password')

            new2 = Toplevel(window)

            new2.title("Verification")

            new2.geometry("925x500+200+100")

            new2.configure(bg='#fff')

            frame12 = Frame(new2, width=550, height=550, bg='white')

            frame12.place(x=290, y=70)

            heading12 = Label(frame12, text="Create new passsword", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, "bold"))

            heading12.place(x=10, y=5)

            user12 = Entry(frame12, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))

            user12.place(x=30, y=80)

            user12.insert(0, 'Create new password')

            Frame(frame12, width=295, height=2, bg="black").place(x=25, y=107)

            user21 = Entry(frame12, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))

            user21.place(x=30, y=130)

            user21.insert(0, "Reconfirm password")

            Frame(frame12, width=295, height=2, bg="black").place(x=25, y=157)

            Button(frame12, width=39, pady=7, text="Submit", bg="#57a1f8", fg="white", border=0, command=threading7).place(x=35, y=200)

    new1 = Toplevel(window)

    new1.title("Forgot password")

    new1.geometry("925x500+200+100")

    new1.configure(bg='#fff')

    frame1 = Frame(new1, width=550, height=550, bg='white')

    frame1.place(x=290, y=70)

    heading1 = Label(frame1, text="Forgot password", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, "bold"))

    heading1.place(x=30, y=0)

    user11 = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))

    user11.place(x=30, y=80)

    user11.insert(0, 'Email Id')

    Frame(frame1, width=295, height=2, bg="black").place(x=25, y=107)

    Button(frame1, width=39, pady=7, text="Verify", bg="#57a1f8", fg="white", border=0, command=threading6).place(x=35, y=150)

def log():

    e = user1.get()

    f = user2.get()

    cursor558 = mydb.cursor()

    sql558 = f"SELECT stat FROM tbl_user WHERE stat='Active'"

    cursor558.execute(sql558)

    result558 = cursor558.fetchall()

    z = len(result558)

    cursor3 = mydb.cursor()

    sql1 = f"SELECT user_email FROM tbl_user WHERE user_email='{e}'"

    cursor3.execute(sql1)

    result1 = cursor3.fetchall()

    g = len(result1)

    if z == 0:

        if g == 0:

            messagebox.showinfo('information', f'{e} user does not exist')

        else:

            cursor4 = mydb.cursor()

            sql2 = f"SELECT user_password FROM tbl_user WHERE user_email='{e}'"

            cursor4.execute(sql2)

            result2 = cursor4.fetchall()

            i = result2[0][0]

            if f == i:

                cursor445 = mydb.cursor()

                sql_update_query1 = f"""Update tbl_user set Time = '{rty}' where user_email = '{e}'"""

                cursor445.execute(sql_update_query1)

                mydb.commit()

                cursor446 = mydb.cursor()

                sql_update_query2 = f"""Update tbl_user set stat = 'Active' where user_email = '{e}'"""

                cursor446.execute(sql_update_query2)

                mydb.commit()

                messagebox.showinfo('Information',
                                    f'Tips before using the software:- \nThe title of the URL and Key CSV must be url and keyword exactly otherwise the softwaere woouldn"t be getting start to run')

                def thread1():

                    t5 = Thread(target=logoutyy)
                    t5.start()

                def logoutyy():

                    cursor447 = mydb.cursor()
                    sql_update_query9999 = f"""Update tbl_user set stat = 'Inactive' where user_email = '{e}'"""
                    cursor447.execute(sql_update_query9999)
                    mydb.commit()
                    messagebox.showinfo('information', 'You have successfully logged out')

                def thread_software():

                    t_software = Thread(target=software_submit)
                    t_software.start()

                def software_submit():

                    u = user_software.get()
                    p= user_softwares.get()

                    messagebox.showinfo('information', 'Next select the backlink csv.')

                    exculpate = askopenfilename()

                    df = pd.read_csv(exculpate)

                    messagebox.showinfo('information', 'Now select the keyword csv.')

                    exl = askopenfilename()

                    dt = pd.read_csv(exl)

                    ul = df["url"]

                    um = dt["keyword"]

                    o = len(ul)

                    driver = webdriver.Chrome(ChromeDriverManager().install())

                    driver.maximize_window()

                    driver.delete_all_cookies()

                    for n in range(o):

                        a = ul[n]

                        bar = um[n]

                        xz = float("nan")

                        if ((type(a)) == (type(xz))):

                            driver.switch_to.window(driver.window_handles[0])

                        else:

                            urlt = ul[n]

                            axz = ((requests.head(urlt).status_code))

                            b = int(axz / 10 ** int(math.log10(axz)))

                            if ((b == 4) or (b == 5)):

                                driver.switch_to.window(driver.window_handles[0])

                                driver.get(ul[n])

                            else:

                                if ((type(bar)) == (type(xz))):

                                    driver.switch_to.window(driver.window_handles[0])

                                    driver.get(ul[n])

                                else:

                                    driver.switch_to.window(driver.window_handles[0])

                                    driver.get(ul[n])

                                    urlt = ul[n]

                                    req = requests.get(urlt)

                                    soup = BeautifulSoup(req.text, "html.parser")

                                    for link in soup.find_all('a'):

                                        if ((link.text) == um[n]):
                                            time.sleep(int(u))

                                            proper = driver.find_element(By.LINK_TEXT, um[n])

                                            driver.execute_script("arguments[0].click();", proper)

                                            time.sleep(int(p))

                    driver.close()

                new_software = Toplevel(window)

                new_software.title("Forgot password")

                new_software.geometry("925x500+200+100")

                new_software.configure(bg='#fff')

                frame_software = Frame(new_software, width=650, height=650, bg='white')
                frame_software.place(x=290, y=70)

                heading_software = Label(frame_software, text="Software portal", fg="#57a1f8", bg="white",
                                         font=('Microsoft YaHei UI Light', 23, "bold"))
                heading_software.place(x=44, y=0)

                user_software = Entry(frame_software, width=25, fg="black", border=0, bg="white",
                                      font=('Microsoft YaHei UI Light', 11))
                user_software.place(x=30, y=64)
                user_software.insert(0, 'Interval(sec) to find a keyword')

                Frame(frame_software, width=295, height=2, bg="black").place(x=25, y=97)

                user_softwares = Entry(frame_software, width=25, fg="black", border=0, bg="white",
                                       font=('Microsoft YaHei UI Light', 11))
                user_softwares.place(x=30, y=120)
                user_softwares.insert(0, "Interval(sec) go to webpage")

                Frame(frame_software, width=295, height=2, bg="black").place(x=25, y=155)

                Button(frame_software, width=39, pady=7, text="Submit", bg="#57a1f8", fg="white", border=0,
                       command=thread_software).place(x=36, y=180)
                Button(frame_software, width=39, pady=7, text="Log Out", bg="#57a1f8", fg="white", border=0,
                       command=thread1).place(x=36, y=220)

            else:

                messagebox.showinfo('information', 'Wrong password')

    else:

        messagebox.showinfo('information', 'Somebody is already using the software')

img=PhotoImage(file="login.png")
Label(window, image=img, bg='white').place(x=50, y=50)

frame = Frame(window, width=350, height=350, bg='white')
frame.place(x=490, y=70)

heading = Label(frame, text="NKTech softwares", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, "bold"))
heading.place(x=30, y=5)

user1 = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user1.place(x=30, y=80)
user1.insert(0, 'UID')

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

user2=Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user2.place(x=30, y=150)
user2.insert(0, "Password")
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, pady=7, text="Log In", bg="#57a1f8", fg="white", border=0, command=threading2).place(x=35, y=204)
Button(frame, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=threading1).place(x=35, y=255)
Button(frame, width=39, pady=7, text="Forgot password", bg="#57a1f8", fg="white", border=0, command=threading3).place(x=35, y=305)
window.mainloop()