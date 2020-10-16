from tkinter import *

class Tela:
    user = ""
    passw = ""
    root = Tk()

    def main(root,title="Tela inicial"):
        root.title("")
        root.mainloop()

    
    def login(root):
        lb_user = Label(root, text="Username: ")
        lb_passw = Label(root, text="Password: ")

        et_user = Entry(root)
        et_passw = Entry(root, show="*")

        lb_result = Label(root)

        bt_login = Button(root, text='Login')
        bt_register = Button(root, text="Register")

        lb_user.grid(row=0, column=0)
        lb_passw.grid(row=1, column=0)
        et_user.grid(row=0, column=1)
        et_passw.grid(row=1, column=1)
        lb_result.grid(row=2, columnspan=2, sticky=W+E)
        bt_login.grid(row=3, columnspan=2, sticky=W+E)
        bt_register.grid(row=4,columnspan=2, sticky=W+E)


Tela.login(Tela.root)
Tela.main(Tela.root, "Login")