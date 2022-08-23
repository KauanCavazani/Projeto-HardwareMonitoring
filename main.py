from tkinter import *
from tkinter import messagebox

# colors -------------------
white = '#bcb9b2'
grey = '#7e7d78'
black = '#000'

# config -------------------
window = Tk()
window.title('')
window.geometry('310x300')
window.configure(background=white)
window.resizable(width=False, height=False)

# config frames ------------
frame_up = Frame(window, width=310, height=50, bg=black, relief='flat')
frame_up.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_down = Frame(window, width=310, height=250, bg=white, relief='flat')
frame_down.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


def start_window():
    for widget in frame_down.winfo_children():
            widget.destroy()
    for widget in frame_up.winfo_children():
            widget.destroy()

    l_title = Label(frame_up, text='HARDWARE MONITORING',justify=CENTER, font=('Ivy 15'), bg=black, fg=grey)
    l_title.place(x=27, y=10)
    l_welcome = Label(frame_down, text='Bem vindo(a)!!!', anchor=NW, font=('Ivy 15'), bg=white, fg=black)
    l_welcome.place(x=80, y=20)

    b_login = Button(frame_down, text='Entrar', width=30, height=2, font=('Ivy 8 bold'), bg=black, fg=white, relief=RAISED, overrelief=RIDGE)
    b_login.place(x=38, y=70)

    b_login = Button(frame_down, command=register_window, text='Cadastrar', width=30, height=2, font=('Ivy 8 bold'), bg=black, fg=white, relief=RAISED, overrelief=RIDGE)
    b_login.place(x=38, y=120)

def register_window():
    for widget in frame_down.winfo_children():
            widget.destroy()
    for widget in frame_up.winfo_children():
            widget.destroy()
    
    l_title = Label(frame_up, text='CADASTRAR', font=('Ivy 15'), bg=black, fg=grey)
    l_title.place(x=90, y=10)

    l_name = Label(frame_down, text='Nome *', anchor=NW, font=('Ivy 10'), bg=white, fg=black)
    l_name.place(x=10, y=5)
    e_name = Entry(frame_down, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
    e_name.place(x=14, y=30)

    l_email = Label(frame_down, text='Nome *', anchor=NW, font=('Ivy 10'), bg=white, fg=black)
    l_email.place(x=10, y=60)
    e_email = Entry(frame_down, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
    e_email.place(x=14, y=90)

    l_passwd = Label(frame_down, text='Senha *', anchor=NW, font=('Ivy 10'), bg=white, fg=black)
    l_passwd.place(x=10, y=120)
    e_passwd = Entry(frame_down, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
    e_passwd.place(x=14, y=150)

    b_submit = Button(frame_down, text='Cadastrar', width=18, height=2, font=('Ivy 8 bold'), bg=black, fg=white, relief=RAISED, overrelief=RIDGE)
    b_submit.place(x=15, y=190)

    b_back = Button(frame_down, command=start_window, text='Voltar', width=18, height=2, font=('Ivy 8 bold'), bg=black, fg=white, relief=RAISED, overrelief=RIDGE)
    b_back.place(x=157, y=190)

start_window()

window.mainloop()

