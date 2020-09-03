from tkinter import *
import tkinter as tk
import tkinter.font as font
import os
import pyttsx3
import datetime
import wikipedia
from time import strftime
import webbrowser
from datetime import datetime
from tkinter.ttk import *
import pyjokes
import random
import sys
import smtplib
import time
import psutil
from playsound import playsound
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import mixer
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
# engine.setProperty('volume',1.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Wishme():
    playsound("beep.wav")
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
        print("Jarvis : Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
        print("Jarvis : Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
        print("Jarvis : Good Evening Sir!")
def Welcome():
    speak("I am Jarvis")
    print("Jarvis : I am Jarvis sir")
    speak("How may I Help you sir")
    print("Jarvis : How may I help You Sir ? ")
def google():
    # top = tk.Tk()
       # w = tk.Label(top, text="Hello Tkinter!")

    # w.pack()
    # global w
    # w.configure(text = "rishi")
    print('Opening Google Sir')
    speak('opening google sir')
    webbrowser.open('google.com')
def youtube():
    # top = tk.Tk()
     # global top
    # w = tk.Label(top, text="Hello Tkinter!")

    # w.pack()
    # global w
    # w.configure(text = "rishi")
    print('Opening Youtube Sir')
    speak('opening Youtube sir')
    webbrowser.open('youtube.com')
def git():
    print('Opening Github Sir')
    speak('opening Github sir')
    webbrowser.open('github.com')

def Time():
    # creating tkinter window
    root = Tk()
    root.title('Clock')

    # This function is used to
    # display time on the label
    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)

    # Styling the label widget so that clock
    # will look more attractive
    lbl = Label(root, font=('calibri', 40, 'bold'),
                background='purple',
                foreground='white')

    # Placing clock at the centre
    # of the tkinter window
    lbl.pack(anchor='center')
    time()

    mainloop()
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print("Current Time is", current_time)
    #
    # if current_time<'12':
    #     speak("The current time is ")
    #     speak(current_time)
    #     speak('AM')
    # else :
    #     speak("The current time is ")
    #     speak(current_time)
    #     speak('PM')

def mail():
    def maill():
        try:
            x1 = entry1.get()
            x2 = entry2.get()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('jarvisprogramm@gmail.com', '9915972220')
            server.sendmail('jarvisprogramm@gmail.com', x1, x2)
            server.close()
            speak('email send successfully')
        except:
            playsound('erro.mp3')
            print('Cannot send E-Mail , please try later')
            speak('cannot send email , please try later')
            print('Make Sure To Connect With Internet')
            speak('Make Sure To Connect With Internet')

    # speak('Let david do this')
    top = tk.Tk()
    top.geometry("290x200")
    top.minsize(290,200)
    top.maxsize(290,200)

    tk.Label(top,
             text="E-Mail",
             fg="orange",
             # bg="dark green",
             font="Helvetica 35 bold italic").pack()

    top.title("E-Mail")
    # style = Style()
    l1 = Label(top, text="")
    message = StringVar()
    message.set('hi')
    canvas1 = tk.Canvas(top, width=500, height=170)
    canvas2 = tk.Canvas(top, width=500, height=170)
    # canvas1.pack()
    c= tk.Label(top,
             text="To:",
             fg="orange",
             # bg="dark green",
             font="Helvetica 10 bold italic")
    d = tk.Label(top,
                 text="Content:",
                 fg="orange",
                 # bg="dark green",
                 font="Helvetica 10 bold italic")
    c.place(x=20, y=80)
    d.place(x=20, y=120)
    entry1 = tk.Entry(top)
    entry1.place(x=90 , y=80)
    entry2 = tk.Entry(top,width=30)
    entry2.place(x=90, y=120)

    B11 = tk.Button(top, text="Send", command=maill, fg="orange", width=12, relief=GROOVE)
    # B11.pack()
    B11.place(relx=0.5, rely=0.9, anchor=CENTER)

    # entry1.pack(side='left')
    # entry1.pack()
    # canvas1.create_window(200, 140, window=entry1)
       # B9.place(x=140, y=200)

    # B1.pack(side="top")
    # B2.pack(side="top")

    # B4.place(x=390, y=100)
    # top = tk.Tk()
    # # global top
    # w = tk.Label(top, text="Hello Tkinter!")
    l1.pack()
    # # Wishme()
    # # Welcome()
    top.mainloop()




def wikipedia1():
    speak('Opening Wikipedia')
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    engine.setProperty('voice', voices[0].id)

    def wikk():
        # try:

            speak('Searching , Please wait sir')

            x1 = entry1.get()
            try :
                print(print(wikipedia.summary(x1)))
                l1.config(text=wikipedia.summary(x1, sentences=1))
                # canvas1.create_window(200, 230, window=label1)
                speak(wikipedia.summary(x1, sentences=2))
            except:
                playsound('erro.mp3')
                l1.config(text='Please Check Your Internet Connection')
                print('Please Try Again Later')
                print('Make sure to check your internet connection')
                speak('Please Try Again Later')
                speak('Make sure to check your internet connection')

        # except:
        #     print('Sorry , Try Again')
        #     speak('Sorry Please try again')
            # l1.config('Sorry Please try again')
            return x1
    root = tk.Tk()
    root.title("Wikipedia")
    tk.Label(root,
             text="Search Wikipedia",
             fg="green",
             # bg="dark green",
             font="Helvetica 20 bold italic").pack()
    canvas1 = tk.Canvas(root, width=400, height=170)
    canvas1.pack()
    entry1 = tk.Entry(root)
    # entry1.pack()
    canvas1.create_window(200, 140, window=entry1)
    B11 = tk.Button(root, text="Search",command=wikk,  fg="green",  width=12 ,relief=GROOVE)
    # B11.place(relx=0.5, rely=0.5, anchor=E,)
    # B11.place(x=190,y=200)
    B11.pack()
    # B11.pack(side="top", fill="both", expand=True)
    # entry1.place(relx=0.5, rely=0.5, anchor=NW)
    message = StringVar()
    message.set('')

    l1 = tk.Button(root, text="Type Something to Get Results",fg="green",height=20 ,relief=FLAT)
    l1.pack()

    # speak('test')


    # def getSquareRoot():
    #     x1 = entry1.get()
    # canvas1.create_window(200, 180, window=button1)

    root.mainloop()

def music():
  try:

    music_dir = 'E:\songs'
    song = os.listdir(music_dir)
    b = len(song)

    a = random.randint(0, b)

    # print(song)
    # print(a)
    speak('now playing ')
    speak(song[a])
    fd = os.startfile(os.path.join(music_dir , song[a]))

    # fd.close()
  except:
      playsound('erro.mp3')
      print('Please Try Again')
      speak('Please Try Again')
def quit():
    sys.exit()
def g():
    speak("Opening Google")
    print('Opening Please Wait , sir')
    codepath = 'E:\google\Google'
    os.startfile(codepath)


def code():
    speak("Opening VS Code")
    print('Opening Please Wait , sir')
    codepath = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
    os.startfile(codepath)
def gittt():
    speak("Opening Github")
    print('Opening Please Wait , sir')
    codepath = 'E:\g\GitHub'
    os.startfile(codepath)
# def quit():
def calc():
    speak('Opening Calculator')
    print('Opening Calculator')
    def add():
        try:
            x1 = entry1.get()
            x2 = entry2.get()
            a = int(x1)
            b = int(x2)
            c = a + b
            print(c)
            # print('The sum is :' , c)
            # l1.config(text='The sum is:')
            l2.config(text='The sum is :')
            l1.config(text=c)
            l1.place(x=120, y=300)
            l2.place(x=30, y=300)
        except:
            playsound('erro.mp3')
            speak('Please Enter a Number')
            print('Please Enter a Number')

    def sub():
        try:
            x1 = entry1.get()
            x2 = entry2.get()
            a = int(x1)
            b = int(x2)
            c = a - b
            print(c)
            # print('The sum is :' , c)
            # l1.config(text='The sum is:')
            l2.config(text='The Diffrence is :')
            l1.config(text=c)
            l1.place(x=150, y=300)
            l2.place(x=30, y=300)
        except:
            playsound('erro.mp3')
            speak('Please Enter a Number')
            print('Please Enter a Number')
    def mul():
        try:
            x1 = entry1.get()
            x2 = entry2.get()
            a = int(x1)
            b = int(x2)
            c = a * b
            print(c)
            # print('The sum is :' , c)
            # l1.config(text='The sum is:')
            l2.config(text='The Multiplication is :')
            l1.config(text=c)
            l1.place(x=180, y=300)
            l2.place(x=30, y=300)
        except:
            playsound('erro.mp3')
            speak('Please Enter a Number')
            print('Please Enter a Number')
    def div():
        try:
            x1 = entry1.get()
            x2 = entry2.get()
            a = int(x1)
            b = int(x2)
            c = a / b
            print(c)
            # print('The sum is :' , c)
            # l1.config(text='The sum is:')
            l2.config(text='The Division is :')
            l1.config(text=c)
            l1.place(x=150, y=300)
            l2.place(x=30, y=300)
        except:
            playsound('erro.mp3')
            speak('Please Enter a Number')
            print('Please Enter a Number')
    message = StringVar()
    message.set('hi')


    top = tk.Tk()
    top.geometry("250x340+300+0")
    top.minsize(250,340)
    top.maxsize(330,340)
    l1 = Label(top, text="")
    l1.place(x=50,y=300)
    l2 = tk.Label(top, text="" ,fg="magenta",font="Helvetica 8 bold italic")
    l1.place(x=50, y=310)

    # l1.place(x=50, y=610)
    # def hello():
    #    messagebox.showinfo("Say Hello", "Hello World")
    tk.Label(top,
             text="Calculator",
             fg="magenta",
             # bg="dark green",
             font="Helvetica 30 bold italic").pack()
    label2 = tk.Label(top,
             text="Value 1 :",
             fg="magenta",
             # bg="dark green",
             font="Helvetica 8 bold italic")
    label1 = tk.Label(top,
             text="Value 2 :",
             fg="magenta",
             # bg="dark green",
             font="Helvetica 8 bold italic")
    label2.place(x=20,y=58)
    label1.place(x=20, y=98)
    top.title("Calculator")
    # style = Style()
    myFont = font.Font(size=20)
    l1 = tk.Label(top, text="",fg="magenta",font="Helvetica 8 bold italic")

    message = StringVar()
    message.set('hi')
    canvas1 = tk.Canvas(top, width=100, height=30)
    canvas1.pack()

    entry1 = tk.Entry(top)
    entry1.place(x=80,y=60)
    # entry1.place(x=30,y=200)

    # entry1.pack()
    # canvas1.create_window(10, 20, window=entry1)
    canvas2 = tk.Canvas(top, width=100, height=50)
    canvas2.pack()

    entry2 = tk.Entry(top)
    entry2.place(x=80,y=100)
    # entry1.place(x=30,y=200)
    l1.pack()
    # entry1.pack()
    # canvas2.create_window(10, 20, window=entry1)
    B1 = tk.Button(top, text="Addition", fg="magenta",command=add,relief=GROOVE)#.pack()
    B2 = tk.Button(top, text="Subtraction", fg="magenta",command=sub,  relief=GROOVE)
    B3 = tk.Button(top, text="Multiplication", fg="magenta",command=mul,  relief=GROOVE)
    B4 = tk.Button(top, text="Division", fg="magenta",command=div, relief=GROOVE)
    B1.pack(fill='both')
    B2.pack(fill='both')
    B3.pack(fill='both')
    B4.pack(fill='both')
    # B1.place(y=20)
    B1.pack()
    # myFont = font.Font(size=20)
    B1['font'] = myFont
    B2['font'] = myFont
    B3['font'] = myFont
    B4['font'] = myFont
    l1['font'] = myFont
    l2['font'] = myFont
def musicc():

    def bca():
        speak('Now Playing Better Came Along')
        mixer.init()
        pygame.mixer.music.load('E:/songs/bca.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing Better Came Along")
        # speak('Finished')
    def dark():
        mixer.init()
        pygame.mixer.music.load('E:/songs/Darkside.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing Darkside")
        speak('Now Playing Darkside')
    def fade():
        mixer.init()
        pygame.mixer.music.load('E:/songs/Faded.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing Faded")
        speak('Now Playing Faded')
    def fall():
        mixer.init()
        pygame.mixer.music.load('E:/songs/Falling.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing Falling ")
        speak('Now Playing Falling')
    def fly():
        mixer.init()
        pygame.mixer.music.load('E:/songs/fa.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing Fly With Me")
        speak('Now Playing Fly With Me')
    def imf():
        mixer.init()
        pygame.mixer.music.load('E:/songs/imf.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing In My Feelings")
        speak('Now Playing In My Feelings  ')
    def lf():
        mixer.init()
        pygame.mixer.music.load('E:/songs/lf.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing Live Fast")
        speak('Now Playing Live Fast')
    def omw():
        mixer.init()
        pygame.mixer.music.load('E:/songs/omw.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing On My Way")
        speak('Now Playing On My Way')
    def july():
        mixer.init()
        pygame.mixer.music.load('E:/songs/July.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing July")
        speak('Now Playing July')
    def seno():
        mixer.init()
        pygame.mixer.music.load('E:/songs/Senorita.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing Senorita ")
        speak('Now Playing Senorita')
    def sou():
        mixer.init()
        pygame.mixer.music.load('E:/songs/sou.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing Shape Of You")
        speak('Now Playing Shape of You')

    def hero():
        mixer.init()
        pygame.mixer.music.load('E:/songs/Superhero.wav')
        mixer.music.set_volume(0.7)
        mixer.music.play()
        B17.config(text="Playing SuperHero ")
        speak('Now Playing Superhero')
    top = tk.Tk()

    top.geometry("465x650+600+0")
    top.minsize(465, 650)
    top.maxsize(465, 650)
    # photo = PhotoImage(file=r"E:/trackicon/previous.png")
    # photo1 = PhotoImage(file=r"E:/trackicon/next.png")
    # B = tk.Button(top, text='Click Me !', image=photo, width=20,command=music , relief=FLAT)
    # def hello():
    #    messagebox.showinfo("Say Hello", "Hello World")
    tk.Label(top,
             text="Music",
             fg="#007bff",
             # bg="dark green",
             font="Helvetica 35 bold italic").pack()
    top.title("Music")
    # style = Style()
    # l1 = Label(top, text="")
    # imagetest = PhotoImage(file="E:/trackicon/play.png")
    # canvas.create_image(250, 250, image=imagetest)

    # button_qwer = Button(top, text="asdfasdf", image=imagetest)

    B1 = tk.Button(top, text="Better Came Along", command =bca , fg="#007bff",height=2, relief=GROOVE)
    B2 = tk.Button(top, text="Darkside",  fg="#007bff",command=dark, height=2,relief=GROOVE)
    B3 = tk.Button(top, text="Faded",  fg="#007bff",command=fade,height=2, relief=GROOVE)
    B4 = tk.Button(top, text="Falling",  fg="#007bff",command=fall,height=2,relief=GROOVE)
    # B5 = tk.Button(top, text='Click Me !', image=photo, width=20,command=music , relief=FLAT)
    B6 = tk.Button(top, text="Fly Away",  fg="#007bff",command=fly, height=2,relief=GROOVE)
    # B7 =  tk.Button(top, text='Click Me !', image=photo1, width=20,command=music , relief=FLAT)
    B8 = tk.Button(top, text='In My Feelings', fg="#007bff",command=imf, height=2,relief=GROOVE)
    B9 = tk.Button(top, text='Live Fast',  fg="#007bff",command=lf,height=2, relief=GROOVE)
    B10 = tk.Button(top, text='On My Way',  fg="#007bff",command=omw,height=2,relief=GROOVE)
    B11 = tk.Button(top, text='July', fg="#007bff",height=2,command=july, relief=GROOVE)
    B12 = tk.Button(top, text='Senorita', fg="#007bff", height=2,command=seno, relief=GROOVE)
    B13 = tk.Button(top, text='Shape Of You', fg="#007bff", height=2,command=sou, relief=GROOVE)
    B14 = tk.Button(top, text='Superhero', fg="#007bff",height=2,command=hero, relief=GROOVE)
    # B15 = tk.Button(top, text='Wash Your Hand', fg="#007bff", height=2, relief=GROOVE)
    # B16 = tk.Button(top, text='Calculator', fg="red",height=2, relief=GROOVE)


    B1.pack(fill='both')
    B2.pack(fill='both')
    B3.pack(fill='both')
    B4.pack(fill='both')
    B6.pack(fill='both')
    B8.pack(fill='both')
    B9.pack(fill='both')
    B10.pack(fill='both')
    B11.pack(fill='both')
    B12.pack(fill='both')
    B13.pack(fill='both')
    B14.pack(fill='both')
    # hour.place(x=10,y=0)
    myFont = font.Font(size=25)

    def pause():
        pygame.mixer.music.pause()
        B17.config(text="Paused ")
    def play():
        pygame.mixer.music.unpause()
        B17.config(text="Playing")
    B15 = tk.Button(top, text='Play', fg="#007bff", relief=GROOVE,command=play,width=11,height=3)
    B15.place(x=30,y=565)
    B15['font'] = myFont
    B16 = tk.Button(top, text='Pause', fg="#007bff",command=pause, relief=GROOVE, width=11, height=3)
    B16.place(x=150, y=565)
    B16['font'] = myFont
    # def vol():
    #     x3 = w.get()
    #     print(x3)




    # v = DoubleVar()
    # w = Scale(top , from_=0 , to_=100,variable=v,)
    # w.place(x=420,y=585)
    B17 = tk.Button(top, text='Welcome To Music', fg="#007bff", width=30, relief=FLAT, height=4)
    B17.place(x=260, y=565)
    # B17['font'] = myFont
    # x3 = w.get()
    # print(x3)
    # w.pack()
    # B15.pack(fill='both')
    # B16.pack(fill='both')

    # imagetest = PhotoImage(file="E:/trackicon/play.png")
    # canvas.create_image(250, 250, image=imagetest)

    # button_qwer = Button(top, text="asdfasdf", image=imagetest)
    # button_qwer.pack()
    # imageFile = "Aaron.jpg"

    # top.im1 = Image.open(imageFile)
def timer():
    def code():
        x2= hour1.get()
        x1 = hour.get()
        x9 = int(x2)
        x10 = int(x1)
        # x3 = x1*60
        # x4=x3+x2
        # x5 = int(x4)
        #
        x12 = x10*60
        x15 = x12 + x9
        # print(x15)
        # l1.config(text="hello")

        for i in range(x15):
            x16 = (x15-i)

            # print(x16)
            l1["text"] =x16
            l1.pack()
            # l1.place(x=100, y=280)
            time.sleep(1)

    #     print(str(x5 - i) + " seconds remaining \n")
    #
    top = tk.Tk()
    top.geometry("300x400+600+0")
    myFont = font.Font(size=25)
    # def hello():
    #    messagebox.showinfo("Say Hello", "Hello World")
    tk.Label(top,
             text="Timer",
             fg="#90EE90",
             # bg="dark green",
             font="Helvetica 35 bold italic").pack()
    hour = tk.Spinbox(top, from_=0, to=59, wrap=True, validate='focusout', width=12)
    hour1 = tk.Spinbox(top, from_=0, to=59, wrap=True, validate='focusout', width=12)
    top.title("Timer")
    hour.place(x=70,y=70)
    hour1.place(x=70, y=100)
    B11 = tk.Button(top, text='Set Timer', command=code,  fg="#c3b371",  relief=GROOVE)

    B11.place(x=73,y=130)
    label  = tk.Label(top,
             text="Minutes :",
             fg="#c3b371",
             font="Helvetica 8 bold italic")
    labelx = tk.Label(top,
             text="Seconds :",
             fg="#c3b371",
             # bg="dark green",
             font="Helvetica 8 bold italic")
    label.place(x=5 , y=70)
    labelx.place(x=5, y=100)
    B11['font'] = myFont
    l1 = tk.Label(top, text="",fg="#c3b371")
    l1.pack()
    l1['font'] = myFont
def takecommand():
    top = tk.Tk()
    top.geometry("380x400+600+0")
    top.minsize(380,400)
    top.maxsize(380,400)
    # def hello():
    #    messagebox.showinfo("Say Hello", "Hello World")
    tk.Label(top,
             text="JARVISi",
             fg="red",
             # bg="dark green",
             font="Helvetica 35 bold italic").pack()
    tk.Label(top,
             text="All My Features",
             fg="red",
             # bg="dark green",
             font="Helvetica 15 bold italic").pack()
    top.title("Jarvis")
    # style = Style()
    l1 = Label(top, text="")
    message = StringVar()
    message.set('hi')

    def press():
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        speak(current_time)

        try:
            root = Tk()
            root.title('Clock')

            # This function is used to
            # display time on the label
            def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text=string)
                lbl.after(1000, time)

            # Styling the label widget so that clock
            # will look more attractive
            lbl = Label(root, font=('calibri', 40, 'bold'),
                        background='purple',
                        foreground='white')

            # Placing clock at the centre
            # of the tkinter window
            lbl.pack(anchor='center')
            time()

            mainloop()

            # now = datetime.now()
            # current_time = now.strftime("%H:%M")
            # speak(current_time)
            # l1.config(text=current_time)
            # l1.place(x=50, y=190)
        except:
            playsound('erro.mp3')
            print("")

    message = StringVar()
    message.set('hi')

    l1 = Label(top, text="")
    photo = PhotoImage(file=r"E:/trackicon/previous.png")
    photo1 = PhotoImage(file=r"E:/trackicon/next.png")
    B1 = tk.Button(top, text="Open Google" , command = g,fg="red", height = 5, width = 13,relief=GROOVE)
    B2 = tk.Button(top, text="Get Time", command=press ,  fg="red", height = 5, width = 13 ,relief=GROOVE)
    B3 = tk.Button(top, text="Open Youtube", command=youtube, fg="red", height=5, width=13, relief=GROOVE)
    B4 = tk.Button(top, text="Search Wikipedia", command=wikipedia1, fg="red", height=5, width=13, relief=GROOVE)
    B5 = tk.Button(top, text='Open Github',command=git, fg="red", height=5, width=13, relief=GROOVE)
    B6 = tk.Button(top, text="Play music", command=musicc, fg="red", height=5, width=13, relief=GROOVE)
    # B7 =  tk.Button(top, text='Click Me !', image=photo1, width=20,command=music , relief=FLAT)
    B8 = tk.Button(top, text='Open Vs Code', command=code, fg="red", height=5, width=13, relief=GROOVE)
    B9 = tk.Button(top, text='Send E-Mail', command=mail, fg="red", height=5, width=13, relief=GROOVE)
    B10 = tk.Button(top, text='Calculator', command=calc, fg="red", height=5, width=13, relief=GROOVE)
    # B9 = tk.Button(top, text='quit', command=quit, fg="red", height=5, width=13, relief=GROOVE)
    B11 = tk.Button(top, text='Timer', command=timer, fg="red", height=5, width=13, relief=GROOVE)

    # B1.pack(fill=X)
    # B2.pack(fill=X)
    # B3.pack(fill=X)
    # B4.pack(fill=X)
    # B6.pack(fill=X)
    # B8.pack(fill=X)
    # B9.pack(fill=X)
    # B10.pack(fill=X)
    # B11.pack(fill=X)
    # B12.pack(fill='both')
    # B13.pack(fill='both')
    # sb = Scrollbar(top)
    # sb.pack(side=RIGHT, fill=Y)
    # B14.pack(fill='both')
    # hour.place(x=10,y=0)
    # B4 = tk.Button(top, text="Open Youtube", command=press, fg="red", height=5, width=13, relief=GROOVE)


    B1.place(x=140, y=100)
    B2.place(x=20,y=100)
    B3.place(x=260, y=100)
    B4.place(x=20, y=200)
    B5.place(x=140,  y=200)
    B6.place(x=260, y=200)
    B8.place(x=20, y=300)
    B9.place(x=140, y=300)
    B10.place(x=260, y=300)


    # B9.place(x=140, y=200)


    # B1.pack(side="top")
    # B2.pack(side="top")

    # B4.place(x=390, y=100)
    # top = tk.Tk()
    # # global top
    # w = tk.Label(top, text="Hello Tkinter!")
    l1.pack()
    # Wishme()
    # Welcome()
    top.mainloop()

#
def battery():
    while True:
        battery = psutil.sensors_battery()
        # print(battery.secsleft / 60)
        plugged = battery.power_plugged
        percent = str(battery.percent)
        percent2 = percent + "%"
        plugged = "Plugged In" if plugged else "Not Plugged In"
        # print(percent + '% | ' + plugged)
        plug = battery.power_plugged
        # print(battery.power_plugged)
        charge = int(battery.secsleft)
        charge2 = int(charge/60)
        if battery.power_plugged!=True:
            if battery.percent <= 38:
                print(f"Jarvis : Suffering with low battery level, {percent2}")
                speak("Sir, Your device is suffering with low battery level")
                print("Jarvis : You Should Plug in the Charger (Recommended)")
                speak("You Should charge your device")
                print(f"Jarvis : Your Device May run for {charge2} minutes")
                speak(f"Your Device May run for {charge2} minutes")
            break
        break





def joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


Wishme()
Welcome()
battery()
takecommand()
input("Write Something To Exit : ")