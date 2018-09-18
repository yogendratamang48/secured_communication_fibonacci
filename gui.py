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
        self.e = Entry(self)
        self.e.pack()
        lblKey = Label(self, text="Input Key")
        lblKey.pack()
        self.e2 = Entry(self)
        self.e2.pack()
        b = Button(self, text="Encrypt", command=self.data_encrypt)
        b.pack()


    def data_encrypt(self):
        _result = encrypt.start(self.e.get(), self.e2.get())
        if _result:
            text = Label(self, text="Encryption Complete")
        else:
            text = Label(self, text="Wrong Character")
        text.pack()
        print("Encryption Complet!!")
        quit()
    
    def data_decrypt(self):
        print("Starting Decryption..")
        message = decrypt.start_decript(self.e3.get())
        print("Message")
        message = "Message: " + message
        text2 = Label(self, text=message)
        text2.pack()

    def callback_decrypt(self):
        lblKey = Label(self, text="Input Key")
        lblKey.pack()
        self.e3 = Entry(self)
        self.e3.pack()
        b = Button(self, text="Decrypt", command=self.data_decrypt)
        b.pack()
        
    def show_text(self):
        text = Label(self, text="Hi there")
        text.pack()


    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
