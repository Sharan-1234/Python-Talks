from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
import pyttsx3
 
# root window
root = Tk()
 
root.resizable(0,0)
root.configure(background="red")
root.title("PYTHON TALKS")
# functions
def speak():
    engine = pyttsx3.init()
    audio_string = text.get(1.0,END)
    engine.say(audio_string)
    engine.runAndWait()
    engine.stop()
 
 
def save_audio():
    engine = pyttsx3.init()
    audio_string = text.get(1.0,END)
    engine.save_to_file(audio_string,'test.mp3')
    engine.runAndWait()
    engine.stop()
    showinfo("python says","audio is saved as test.mp3")
 
# root widgets
text = scrolledtext.ScrolledText(root,width=100,height=40,wrap=WORD,padx=10,pady=10,borderwidth=5,relief=RIDGE)
text.grid(row=0,columnspan=3)
#buttons
ttk.Button(root,text="Listen",width=7,command=speak).grid(row=2,column=0,ipadx=2)
ttk.Button(root,text="Clear",width=7,command=lambda:text.delete(1.0,END)).grid(row=2,column=1,ipadx=2)
ttk.Button(root,text="Save",width=7,command=save_audio).grid(row=2,column=2,ipadx=2)
 
root.mainloop()
 
'''
## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound
import os



################### Initialized window####################

root = Tk()
root.geometry('420x420')
root.resizable(0,0)
root.config(bg = 'red')
root.title('PYTHON TALKS')


##heading
Label(root, text = 'PYTHON TALKS' , font='algerian 20' , bg ='red').pack()
#Label(root, text ='' , font ='arial 15 bold', bg = 'white smoke').pack(side = BOTTOM)




#label
Label(root, text ='Enter your text :', font ='agencyfb 15', bg ='yellow').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='62')
entry_field.place(x=20 , y=100)


###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('pythonspeech.mp3')
    playsound('pythonspeech.mp3')
    os.system('pyhtonspeech.mp3')
    os.remove('pythonspeech.mp3')
    speech.save('pythonspeech.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =6).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=167,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=300 , y =140)


#infinite loop to run program
root.mainloop()
'''