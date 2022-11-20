from tkinter import *

from tkinter import messagebox 

from PIL import ImageTk,Image

# ===== ALL PAGE =============
def reference_page(): 
    global top
    top = Toplevel()
    top.geometry("500x500")
    root.withdraw()


    Label(top,text="Reference",font=('Aerial 12 bold')).pack()


    Label(top,text="www : https://vogue.co.th/beauty/outfit-trend",font=('Aerial 12 bold')).pack()

    back_btn = Button(top,text="Back",command=close_reference_page)
    back_btn.pack()


def blaze_page(): 
    global top2
    root.withdraw()
    top2 = Toplevel()
    top2.geometry("700x700")

    blaze_img = ImageTk.PhotoImage(Image.open("assets/NoFont+NoBG2.PNG").resize((250,250)) )

    Label(top2,text="Blazer Look",font=('Aerial 12 bold')).pack()
    
    canvas = Canvas(top2, width=300, height=300)
    canvas.pack()
    canvas.create_image(250,250,image=blaze_img)

    desc = "เบลเซอร์ คือเสื้อคลุมที่คล้ายกับสูท แต่ต่างกันตรงที่\nเบลเซอร์จะมีความ Casual มากกว่า จึงเป็นไอเทมที่ควรมีติดตู้เสื้อผ้า"
    Label(top2,text=desc,font=('Aerial 12 bold')).pack()

    back_btn2 = Button(top2,text="Back",command=close_blaze)
    back_btn2.pack()


def y2k_page(): 
    global top3
    root.withdraw()
    top3 = Toplevel()
    top3.geometry("700x700")

    blaze_img = ImageTk.PhotoImage(Image.open("assets/NoFont+NoBG4.PNG").resize((250,250)) )

    Label(top3,text="Y2K Look",font=('Aerial 12 bold')).pack()
    
    canvas = Canvas(top3, width=300, height=300)
    canvas.pack()
    canvas.create_image(250,250,image=blaze_img)

    desc = "การรวมตัวกันของโทนสีเน้นสีสันสดใส หรือพาสเทลน่ารักๆ\nกับไอเทมที่ทำให้ลุคนี้น่าสนใจ ไม่ว่าจะเป็น กระโปรงหรือกางเกงเอวต่ำที่สวนกระแสเอวสูงไปเมื่อปีที่แล้ว\nหรือว่าจะเป็นเสื้อครอปเอวลอยตัวจิ๋วโชว์เอวเน้นๆ นอกจากนี้ยังมีกระเป๋าถือสุดวินเทจที่บอกเลยว่าเป็นท็อปไอเทมของลุคนี้"
    Label(top3,text=desc,font=('Aerial 12 bold')).pack()
    back_btn3 = Button(top3,text="Back",command=close_y2k)
    back_btn3.pack()

def headscaff_page(): 
    global top4
    root.withdraw()
    top4 = Toplevel()
    top4.geometry("700x700")

    blaze_img = ImageTk.PhotoImage(Image.open("assets/NoFont+NoBG1.PNG").resize((150,150)))

    Label(top4,text="Head Scarf Look",font=('Aerial 12 bold')).pack()
    
    canvas = Canvas(top4, width=300, height=300)
    canvas.pack()
    canvas.create_image(250,250,image=blaze_img)

    desc = "ลุคที่มาพร้อมกับผ้าโพกผม แฟชั่นเมื่อปี 60s ที่กลับมาฮิตอีกครั้ง โดยเสน่ห์ของลุคนี้คือการนำผ้าต่างๆ\nเช่น ผ้าเช็ดหน้า ผ้าคลุม มาโพกหัว ทำให้ลุคนั้นดูเก๋ขึ้น สามารถจับมาแต่งกับชุดไหนก็ได้หลากหลายแนว\nไม่ว่าจะเป็น ชุดสำหรับไปทะเล หรือวันสบายๆ ก็ดูเก๋ไม่เบา"
    Label(top4,text=desc,font=('Aerial 12 bold')).pack()
    back_btn4 = Button(top4,text="Back",command=close_headscaff)
    back_btn4.pack()

def close_reference_page(): 
    top.destroy()
    root.deiconify()


def close_blaze(): 
    top2.destroy()
    root.deiconify()

def close_y2k(): 
    top3.destroy()
    root.deiconify()

def close_headscaff(): 
    top4.destroy()
    root.deiconify()

def exit_program(): 
    root.destroy()





if __name__ == '__main__': 
    root = Tk()
    root.title("Fashion")
    root.geometry("700x700+0+0")


    Label(root,text='Fashion Application',font=('Aerial 20 bold')).pack(pady=20)
    img1 = ImageTk.PhotoImage(Image.open("assets/NoFont+NoBG1.PNG").resize((150,150)))

    menu_frame = Frame(root)
    menu_frame.pack()
    btn = Button(menu_frame,text='Blazer Look',image=img1,compound=TOP,font=('Aerial 12 bold'),command=blaze_page,cursor='hand2')
    btn.pack(side=LEFT,padx=5)

    img2 = ImageTk.PhotoImage(Image.open("assets/NoFont+NoBG5.PNG").resize((150,150)))
    btn2 = Button(menu_frame,image=img2,text='Y2K Look',compound=TOP,font=('Aerial 12 bold'),command=y2k_page,cursor='hand2')
    btn2.pack(side=LEFT,padx=5)



    img3 = ImageTk.PhotoImage(Image.open("assets/NoFont+NoBG4.PNG").resize((150,150)))
    btn3 = Button(menu_frame,image=img3,text='Head Scarf Look',compound=TOP,font=('Aerial 12 bold'),command=headscaff_page,cursor='hand2')
    btn3.pack(side=LEFT,padx=5)


    menu_frame2 = Frame(root)
    menu_frame2.pack()

    img4 = ImageTk.PhotoImage(Image.open("assets/NoFont+NoBG2.PNG").resize((150,150)))
    btn4 = Button(menu_frame2,image=img4,text='Reference',compound=TOP,font=('Aerial 12 bold'),command=reference_page,cursor='hand2')
    btn4.pack(side=LEFT,padx=5)

    img5 = ImageTk.PhotoImage(Image.open("assets/NoFont+NoBG6.PNG").resize((150,150)))
    btn5 = Button(menu_frame2,image=img5,text='Exit Program',compound=TOP,font=('Aerial 12 bold'),command=exit_program,cursor='hand2')
    btn5.pack(side=LEFT,padx=5)


    root.mainloop()