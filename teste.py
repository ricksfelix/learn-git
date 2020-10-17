from tkinter import *

class Tela:
    popup = True
    user = ""
    passw = ""
    root = Tk()

    def popup(msg="asd", bt_text="confirm",title="Popup"):
        pop = Tk()

        def confirm():
            pop.destroy()

        lb_text = Label(pop)
        bt_confirm = Button(pop, command=confirm)

        lb_text["text"] = msg
        bt_confirm["text"] = bt_text
        pop.title(title)

        lb_text.grid(row=0, column=0)
        bt_confirm.grid(row=1, column=0)
        pop.mainloop()

    def reset():
        root = Tela.root
        for widget in root.winfo_children():
            widget.destroy()
        Tela.login(Tela.root)

    def main(root,title="Tela inicial"):
        root.title("")
        root.mainloop()


    def register(root):
        def cadastro():
            user = et_user.get()
            passw = et_passw.get()
        
        def voltar():
            Tela.reset()
            Tela.login(Tela.root)

        lb_user = Label(root, text="Username: ")
        lb_passw = Label(root, text="Password: ")

        et_user = Entry(root)
        et_passw = Entry(root, show="*")

        lb_result = Label(root, text="Digite o Usuario e Senha Para Cadastrar!")

        bt_login = Button(root, text='Cadastrar', command=cadastro)
        bt_register = Button(root, text="Voltar", command=voltar)

        lb_user.grid(row=0, column=0)
        lb_passw.grid(row=1, column=0)

        et_user.grid(row=0, column=1)
        et_passw.grid(row=1, column=1)

        lb_result.grid(row=2, columnspan=2, sticky=W+E)

        bt_login.grid(row=3, columnspan=2, sticky=W+E)
        bt_register.grid(row=4,columnspan=2, sticky=W+E)


    def login(root):
        def check_login():
            user = et_user.get()
            passw = et_passw.get()
            Tela.popup("TESTE 123123123123")
        
        def register():
            Tela.reset()
            Tela.register(Tela.root)


        lb_user = Label(root, text="Username: ")
        lb_passw = Label(root, text="Password: ")

        et_user = Entry(root)
        et_passw = Entry(root, show="*")

        lb_result = Label(root)

        bt_login = Button(root, text='Login', command=check_login)
        bt_register = Button(root, text="Register", command=register)

        lb_user.grid(row=0, column=0)
        lb_passw.grid(row=1, column=0)

        et_user.grid(row=0, column=1)
        et_passw.grid(row=1, column=1)

        lb_result.grid(row=2, columnspan=2, sticky=W+E)

        bt_login.grid(row=3, columnspan=2, sticky=W+E)
        bt_register.grid(row=4,columnspan=2, sticky=W+E)

Tela.login(Tela.root)
Tela.main(Tela.root, "Login")