from tkinter import *
import fun

master = Tk()
master.title("To Py")
master.geometry("1440x1024")

# Carrega as imagens
back = PhotoImage(file="Images//back.png")
myday = PhotoImage(file="Images//myday.png")
all = PhotoImage(file="Images//all.png")
done = PhotoImage(file="Images//done.png")
important = PhotoImage(file="Images//important.png")
planned = PhotoImage(file="Images//planned.png")
pending = PhotoImage(file="Images//pending.png")
new = PhotoImage(file="Images//new.png")
#Define a imagem de fundo
lab_back = Label(master, image=back)
lab_back.pack()

# Cria um botão para cada imagem
myday_button = Button(master, bd=0, image=myday)
all_button = Button(master, bd=0, image=all)
done_button = Button(master, bd=0, image=done)
important_button = Button(master, bd=0, image=important)
planned_button = Button(master, bd=0, image=planned)
pending_button = Button(master, bd=0, image=pending)
new_button = Button(master, bd=0, image=new)

# Posiciona cada botão na janela
myday_button.place(x=137, y=240, width=357, height=74)
all_button.place(x=137, y=694, width=357, height=74)
done_button.place(x=137, y=518, width=357, height=74)
important_button.place(x=137, y=334, width=357, height=74)
planned_button.place(x=137, y=428, width=357, height=74)
pending_button.place(x=137, y=607, width=357, height=74)
new_button.place(x=736, y=185, width=643, height=60)

master.mainloop()