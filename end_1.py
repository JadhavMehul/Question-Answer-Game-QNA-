from tkinter import *
window=Tk()
window.title("K.B.C")
w=Canvas(window,width=1360,height=700,bg="black")

level_1=w.create_text(720,350,text="Your High Score is 0",fill="orange",font=("Italic",40))

w.pack()
window.mainloop()
