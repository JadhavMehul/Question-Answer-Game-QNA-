from tkinter import *

def next1():
    window.destroy()
    import level_1
    
def end():
    window.destroy()
    import end_1
    
window=Tk()
window.title("K.B.C")
w=Canvas(window,width=1360,height=700,bg="black")

#< image_part >

picture=PhotoImage(file="kbc1.png")
w.create_image(690,190,image=picture)

#< image_part_close >

#<question_bar_part>

qbar_1=w.create_polygon(80,420,300,420,330,380,1050,380,1080,420,1290,420,1330,425,1075,425,1045,385,335,385,305,425,40,425,fill="sky blue")
qbar_2=w.create_polygon(40,430,305,430,335,470,1045,470,1075,430,1330,430,1290,435,1080,435,1050,475,330,475,300,435,80,435,fill="sky blue")

#</question_bar_part>

#<answer_bar>

abar_1=w.create_polygon(190,525,300,525,330,485,610,485,640,525,720,525,750,485,1055,485,1085,525,1200,525,1240,530,1080,530,1050,490,755,490,725,530,635,530,605,490,335,490,305,530,150,530,fill="sky blue")
abar_2=w.create_polygon(150,535,305,535,335,575,605,575,635,535,725,535,755,575,1050,575,1080,535,1240,535,1200,540,1085,540,1055,580,750,580,720,540,640,540,610,580,330,580,300,540,190,540,fill="sky blue")

abar_3=w.create_polygon(190,625,300,625,330,585,610,585,640,625,720,625,750,585,1055,585,1085,625,1200,625,1240,630,1080,630,1050,590,755,590,725,630,635,630,605,590,335,590,305,630,150,630,fill="sky blue")
abar_4=w.create_polygon(150,635,305,635,335,675,605,675,635,635,725,635,755,675,1050,675,1080,635,1240,635,1200,640,1085,640,1055,680,750,680,720,640,640,640,610,680,330,680,300,640,190,640,fill="sky blue")

#</answer_bar>

#<question_tag>

qtag=w.create_text(690,430,text="Choose your option",fill="orange",font=("Italic",30))

#</question_tag>

#<answer_tag>

ans_tag_A=Button(w,text="A : Play        ",bg="black",fg="orange",font=("Italic",19),command = next2)
ans_tag_A.place(x=330,y=505)

ans_tag_B=Button(w,text="B : Rules            ",bg="black",fg="orange",font=("Italic",19),command = end)
ans_tag_B.place(x=750,y=505)

ans_tag_C=Button(w,text="C : know more ",bg="black",fg="orange",font=("Italic",19),command = end)
ans_tag_C.place(x=330,y=610)

ans_tag_D=Button(w,text="D : Quit       ",bg="black",fg="orange",font=("Italic",19),command = end)
ans_tag_D.place(x=750,y=610)

#</answer_tag>

w.pack()
window.mainloop()
