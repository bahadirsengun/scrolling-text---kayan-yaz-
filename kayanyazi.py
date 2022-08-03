from tkinter import*
pencere = Tk()
pencere.title("@dev.sengun")
pencere.geometry("250x300")
pencere.resizable(FALSE, FALSE)
pencere.configure(bg="silver")

kayanyazi= "D E V  S E N G U N  P Y T H O N  İ L E  Y A P T I"
kayanyazi=(" "*20)+ kayanyazi + (" "*20)

text1 = Text(pencere, height=1, width=20, fg="blue")
text1.place(x=50, y=50)

i = 0

def command(x, i):
    text1.insert("1.1", x)
    if i == len(kayanyazi):
        i = 0
    else:
            i = i+1
    pencere.after(100, lambda:command(kayanyazi[i:i+20],i))

command(kayanyazi[i:i+20],i)

pencere.mainloop()