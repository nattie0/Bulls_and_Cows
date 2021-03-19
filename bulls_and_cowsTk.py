from tkinter import *
from tkinter import ttk
from random import shuffle
 
root = Tk()
root.title('Bulls and cows')
 
tries = IntVar()
tries.set(0)
number = StringVar()
 
 
def new_game():
    '''Starts new game'''
    tries.set(0)
    gen(n.get())
    box.delete(0, END)
    n['state'] = 'disable'
    change['fg'] = 'grey'
    
def gen(n):
    '''Generates random n-digits combination without repeating'''
    num = ''
    nums =[1,2,3,4,5,6,7,8,9,0]
    shuffle(nums)
    for i in range(int(n)):
        num += str(nums.pop())
    lab['text'] = 'Computer has generated number!'
    number.set(num)
    
def control(event):
    '''Validation of input'''
    entry = ent.get()
    num = int(n.get())
    if len(entry)==num and entry.isdigit():
        check(entry, number.get())
    elif not entry.isdigit():
        lab['text'] = 'Error. Only digits are allowed'
    elif len(entry) != num:
        lab['text'] = f'''Error. You should enter
{n.get()}-digit number'''
    else: lab['text'] = 'Error'
    
def check(num, number):
    '''Checs input number with hidden one'''
    tries.set(tries.get()+1)
    ent.delete(0, END)
    
    if num == number:
        lab['text'] = f'''Congratulations!
        You guessed in {tries.get()} tries!
        Let's play again!'''
        n['state'] = 'readonly'
        change['fg'] = 'black'
        box.insert(END, f'{tries.get()}. {num}    congratulations!')
    else:
        cows = 0
        bulls = 0
        for i,j in enumerate(num):
            if j in number:
                if num[i] == number[i]:
                    bulls += 1
                else: cows += 1
        lab['text'] = f'{bulls} bulls and {cows} cows'
        box.insert(END, f'{tries.get()}. {num}:    b{bulls},  c{cows}')
            
 
f = Frame()
ent = Entry(width=10, font='Arial 16', justify='right')
ent.bind('<Return>', control)
but = Button(width=5, text='Check', bg='lightgreen')
but.bind('<Button-1>', control)
lab = Label(text='Hello!', width=23, height=3, font=('Arial', 7))
new = Button(f, text='New game', bg='lightyellow', width=11, command=new_game)
change = Label(f, font='Arial 6', text='lenth of number ')
n = ttk.Combobox(f, width=3, values=[3,4,5,6], state='readonly')
n.current(1)
box = Listbox(width=15, height=10)
 
change.pack(side='left')
n.pack(side='left')
new.pack(side='right')
f.pack(fill=X)
box.pack(side='right')
lab.pack(fill=X)
 
ent.pack(fill=X)
but.pack(fill=X)
 
root.mainloop()
