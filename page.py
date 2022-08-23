from tkinter import NE, NSEW, NW, RAISED, RIDGE, Button, Entry, Frame, Label, Tk, ttk
from tkinter import messagebox

# Cores 
black = "#000000"
white = "#ffffff"
blue = "#3fb5a3"
value = "#38576b"
letter = "#403d3d"

window = Tk()
window.title('')
window.geometry('310x300')
window.configure(background=white)
window.resizable(width=False, height=False)

frame_up = Frame(window, width=310, height=50, bg=white, relief='flat')
frame_up.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_down = Frame(window, width=310, height=250, bg=white, relief='flat')
frame_down.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# frame_up
l_title = Label(frame_up, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=white, fg=letter)
l_title.place(x=5, y=5)

l_linha = Label(frame_up, text='', width=275, anchor=NW, font=('Ivy 1'), bg=blue, fg=letter)
l_linha.place(x=10, y=45)

credentials = ['joao', '123']

def verify_passwd():
    name = e_name.get()
    passwd = e_passwd.get()

    if name == 'admin' and passwd == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo admin!!!')
    elif credentials[0] == name and credentials[1] == passwd:
        messagebox.showinfo('Login', 'Seja bem vindo de volta ' + credentials[0] + '!!!')

        #apagar o que tiver no frame_up e frame_down
        for widget in frame_up.winfo_children():
            widget.destroy()

        for widget in frame_down.winfo_children():
            widget.destroy()

        new_window()
    else:
        messagebox.showwarning('ERRO: Verifique a senha')

def new_window():
    l_title = Label(frame_up, text='Usuário: ' +credentials[0], anchor=NE, font=('Ivy 25'), bg=white, fg=letter)
    l_title.place(x=5, y=5)

    l_linha = Label(frame_up, text='', width=275, anchor=NW, font=('Ivy 1'), bg=blue, fg=letter)
    l_linha.place(x=10, y=45)

    l_welcome = Label(frame_down, text='Seja bem vindo ' +credentials[0], anchor=NW, font=('Ivy 10'), bg=white, fg=letter)
    l_welcome.place(x=10, y=20)



# frame_down
l_name = Label(frame_down, text='Nome *', anchor=NW, font=('Ivy 10'), bg=white, fg=letter)
l_name.place(x=10, y=20)
e_name = Entry(frame_down, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
e_name.place(x=14, y=50)

l_passwd = Label(frame_down, text='Senha *', anchor=NW, font=('Ivy 10'), bg=white, fg=letter)
l_passwd.place(x=10, y=95)
e_passwd = Entry(frame_down, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
e_passwd.place(x=14, y=130)

b_submit = Button(frame_down, command=verify_passwd, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=blue, fg=white, relief=RAISED, overrelief=RIDGE)
b_submit.place(x=15, y=180)



window.mainloop()


