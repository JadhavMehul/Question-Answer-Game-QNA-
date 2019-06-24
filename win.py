from tkinter import *
window=Tk()
window.title("K.B.C")
w=Canvas(window,width=1360,height=700,bg="black")

winner=w.create_text(720,350,text="Your High Score is level 15",fill="orange",font=("Italic",40))
winner=w.create_text(720,395,text="Your are the winner of this Game",fill="orange",font=("Italic",40))
winner=w.create_text(720,440,text="Your Prize is 1 Crore rs",fill="orange",font=("Italic",40))



w.pack()
window.mainloop()
