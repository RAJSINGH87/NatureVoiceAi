import tkinter
from  tkinter import *
from tkinter import messagebox
import speech_recognition as sr
from tkinter import PhotoImage
import pygame
from PIL import Image,ImageTk

t=tkinter.Tk()
t.geometry('1700x1700')
t.title('AI Speak')
def change():
    r=sr.Recognizer()
    messagebox.showinfo(('Hi','Pls Speak....'))
    with sr.Microphone() as source:
        print('Pls Speak')
        atext=r.listen(source)
        print('Time over')
        try:
            st=r.recognize_google(atext)
            print("you said:",st)
            if st=='water':
                img = Image.open("water.png")
                img = img.resize((300,300))
                img = ImageTk.PhotoImage(img)
                a.config(image=img)
                a.image=img
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('watersound.mp3')
                pygame.mixer.music.play(loops=5)
            elif st=='wind':
                img = Image.open("wind.png")
                img = img.resize((300,300))
                img = ImageTk.PhotoImage(img)
                a.config(image=img)
                a.image=img
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('windsound.mp3')
                pygame.mixer.music.play(loops=5)
            elif st=='fire':
                img = Image.open("fire.png")
                img = img.resize((300,300))
                img = ImageTk.PhotoImage(img)
                a.config(image=img)
                a.image=img
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('firesound.mp3')
                pygame.mixer.music.play(loops=5)
            elif st=='insect':
                img = Image.open("insect.png")
                img = img.resize((300,300))
                img = ImageTk.PhotoImage(img)
                a.config(image=img)
                a.image=img
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('insectsound.mp3')
                pygame.mixer.music.play(loops=5)
            elif st=='rain':
                img = Image.open("rain.png")
                img = img.resize((300,300))
                img = ImageTk.PhotoImage(img)
                a.config(image=img)
                a.image=img
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('rainsound.mp3')
                pygame.mixer.music.play(loops=5)
            elif st=='Thunder':
                img = Image.open("thunder.png")
                img = img.resize((300,300))
                img = ImageTk.PhotoImage(img)
                a.config(image=img)
                a.image=img
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('thundersound.mp3')
                pygame.mixer.music.play(loops=5)
            elif st=='animal':
                img = Image.open("bird.png")
                img = img.resize((300,300))
                img = ImageTk.PhotoImage(img)
                a.config(image=img)
                a.image=img
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load('birdsound.mp3')
                pygame.mixer.music.play(loops=5)
             
        except Exception as ex:
         print('Issue',ex)
   
def st():
    pygame.mixer.music.stop()
a=Label(t,text='Here')
a.place(x=200,y=50)
bt=Button(t,text='Speak',command=change)
bt.place(x=200,y=200) 
bt2=Button(t,text='Stop',command=st)
bt2.place(x=200,y=300)
t.mainloop()