from tkinter import *
import decrypt
import encrypt

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)


        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="encrypt", command=self.callback_encrypt)
        file.add_command(label="decrypt", command=self.callback_decrypt)
        # file.add_command(label="show text", command=self.show_text)
        file.add_command(label="Exit", command=self.client_exit)

        menu.add_cascade(label="File", menu=file)
        
    def callback_encrypt(self):
        lblMessage = Label(self, text="Input Message")
        lblMessage.pack()
        e = Entry(self)
        e.pack()
        lblKey = Label(self, text="Input Key")
        lblKey.pack()
        e2 = Entry(self)
        e2.pack()
        b = Button(self, text="Encrypt", command=self.data_encrypt)
        encrypt.start(e.get(), e2.get())
        b.pack()


    def data_encrypt(self):
        text = Label(self, text="Encryption Complete")
        text.pack()
        print("Encryption Complet!!")
    
    def data_decrypt(self):
        message = decrypt.start_decript(e3.get())
        text2 = Label(self, text=message)
        text2.pack()
        pass



    def callback_decrypt(self):
        lblKey = Label(self, text="Input Key")
        lblKey.pack()
        e3 = Entry(self)
        e3.pack()
        b = Button(self, text="Decrypt", command=self.data_decrypt)
        b.pack()
        


    def data_decrypt(self):
        # print("Decrypt")
        # _data = decrypt.start_decript()
        text = Label(self, text="Hi there")
        text.pack()
    
    def show_text(self):
        text = Label(self, text="Hi there")
        text.pack()


    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()