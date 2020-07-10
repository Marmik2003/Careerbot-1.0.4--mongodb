from tkinter import *
import tkinter.messagebox
import botmind
import speech_recognition as sr
from playsound import playsound
import pyttsx3 as tts
import threading

window_size = "400x400"


class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.tl_bg = "#4f4f4f"
        self.tl_bg2 = "#444444"
        self.tl_fg = "#ffffff"
        self.font = "Verdana 10"

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5, bg="#444444")

        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
        file.add_command(label="Clear Chat", command=self.clear_chat)
        file.add_command(label="Exit", command=self.chatexit)

        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        help_option.add_command(label="About CareerBot", command=self.msg)
        help_option.add_command(label="Develpoer", command=self.about)

        self.text_frame = Frame(self.master, bd=6, bg="#444444")
        self.text_frame.pack(expand=True, fill=BOTH)

        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=0, spacing3=0, wrap=WORD, bg="#4f4f4f", fg="#ffffff",
                             font=("Verdana 10", 8), relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END,
                             "Welcome to CareerBot v1.0.3 \nI can help you to decide your Career. \nFor more info you can click on help! \nYou Have these Options: \n      10th Pass \n      12th Pass \n")
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)

        self.entry_frame = Frame(self.master, bd=1, bg="#444444")
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT, bg="#4f4f4f", fg="#ffffff")
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)

        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)

        self.button_photo = PhotoImage(file = "send.png")
        self.send_button = Button(self.send_button_frame, image=self.button_photo, width=28, relief=GROOVE,
                                  bd=1, command=lambda: self.send_message_insert(None), bg="#4f4f4f", fg="#ffffff",
                                  activebackground="#4f4f4f",
                                  activeforeground="#ffffff")
        self.send_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)

        self.button_photo_mic = PhotoImage(file = "Mic.png")
        self.mic_button = Button(self.send_button_frame, image = self.button_photo_mic, width = 28, relief = GROOVE, bd=1,
                                 command=lambda: self.send_audmsg_insert(), bg="#4f4f4f", activebackground="#4f4f4f")
        self.mic_button.pack(side=LEFT, ipady=8)

    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.text_box.delete(1.0, END)
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    def chatexit(self):
        exit()

    def msg(self):
        tkinter.messagebox.showinfo("CareerBot v1.0", 'CareerBot is a chatbot for guidance of your Career')

    def about(self):
        tkinter.messagebox.showinfo("CareerBot Developer", "Marmik Patel")

    def playResponce(self, responce):
        x = tts.init()
        li = []
        if len(responce) > 100:
            if responce.find('--') == -1:
                b = responce.split('--')

        x.setProperty('rate', 120)
        x.setProperty('volume', 100)
        x.say(responce)
        x.runAndWait()

    def send_message_insert(self, message):
        user_input = self.entry_field.get()
        if user_input == '':
            tkinter.messagebox.showerror(title=None,message='You cannot send empty message!')
        else:
            pr1 = "You : " + user_input + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr1)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)

            ui_lower = user_input.lower()
            repstr = botmind.chat_reply(ui_lower)
            rep = 'CareerBot: ' + str(repstr) + '\n'
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, rep)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.entry_field.delete(0, END)
            t2 = threading.Thread(target=self.playResponce, args=(repstr,))
            t2.start()

    def send_audmsg_insert(self):
        r1 = sr.Recognizer()
        r2 = sr.Recognizer()
        playsound('sfx/vastart.mp3')
        with sr.Microphone() as source:
            audio = r2.listen(source)
        text = r1.recognize_google(audio)
        self.entry_field.insert(END, text)
        playsound('sfx/vastop.mp3')

root = Tk()

a = ChatInterface(root)
root.geometry(window_size)
root.title("CareerBot")
root.mainloop()
