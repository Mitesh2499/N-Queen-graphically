from tkinter import *
from tkinter import messagebox
from random import *
import winsound
bclick = True


tk = Tk()
tk.title("N Queen")

n = 4

btns = []

x = randint(0, 1)




def win():
    winsound.PlaySound("Ta_Da1.wav", winsound.SND_ASYNC)
    messagebox.showinfo("Winner", " Played well!!")


def loss():
    winsound.PlaySound("Ta_Da1.wav", winsound.SND_ASYNC)
    messagebox.showinfo("Loss", " Try again!!")
    board()

def check(c):
    print(c)
    if c==4:
        win()

    count=0
    for i in range(n):
        for j in range(n):
            if btns[i][j]["bg"] == "red":
                count+=1

    if count>=13:
        loss()
                
        
        
    
    
                
            
    

def red(r,c):
    if btns[r][c]["text"] == "":
        btns[r][c].config(bg="red",state=DISABLED)



def block(button, r, c):
   
    print(r, c)
    
    print(button)
    for i in range(4):
        print(r, i)
        red(r,i)
        pass

    for j in range(4):
        print(j, c)
        red(j,c)
    

    for i,j in zip(range(r,-1,-1),range(c,-1,-1)):
        print(i,j)
        red(i,j)
    
        
    for i,j in zip(range(r,n),range(c,-1,-1)):
        print(i,j)
        red(i,j)
        

    for i,j in zip(range(r,n),range(c,n)):
        print(i,j)
        red(i,j)
        
    for i,j in zip(range(r,-1,-1),range(c,n)):
        print(i,j)
        red(i,j)
    

global c   
c=0
def Queen(row,column):
    global c
    
    if btns[row][column]["text"] == "":
        c+=1
        btns[row][column].config(text="Q")
        a = btns[row][column].grid_info()
        # print(a['row'],a['column'])

        column = a['column']
        row = a['row']
        block(btns[row][column], row, column)
        check(c)


def board():
    name = Label(None, text="N Queen", font=('Times 20 bold'))
    #name.grid(row=0, column=2)
    for i in range(4):
        l=[]
        for j in range(4):
            l.append(Button(font=('Times 20 bold'), bg='white', fg='black', height=4, width=8))
        btns.append(l)
   

    for i in range(4):
        for j in range(4):
            btns[i][j].grid(row=i, column=j)
            btns[i][j].config(command=lambda row=i,column=j: Queen(row,column))

            
def main():
    board()
main()
tk.mainloop()
