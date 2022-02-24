import tkinter as tk
import random

#functions:
def btn_unhide(num):
    global previous_card #otherwise the assignment will convert previous_card within the function to a local variable
    cards[num][0].config(text=words[num],bg='blue') #set card 1 (index 0) to corresponding word 1 (undex 0) i.e. display word
    if previous_card > -1:
        if words[previous_card] == words[num]: #if current selection word is same as previous selection (referenced in words list by indices)
            cards[num][1] = 1 #set card to solved
            cards[previous_card][1] =1 #set previous card to solved
        elif cards[previous_card][1] != 1: #if previous card not solved, clear it
            print("Clearing card ",previous_card)
            cards[previous_card][0].config(text="",bg='grey') #maybe this should just get reset to white again? as grey it allows player to know what cards they've not yet picked but I actually think that makes it harder in practice as it's visually more confusing
    previous_card = num
    global clicks
    clicks -= 1
    score = "Moves left: " + str(clicks)
    window.title(score)

def btn1_unhide():
    btn_unhide(0)
def btn2_unhide():
    btn_unhide(1)
def btn3_unhide():
    btn_unhide(2)
def btn4_unhide():
    btn_unhide(3)
def btn5_unhide():
    btn_unhide(4)
def btn6_unhide():
    btn_unhide(5)
def btn7_unhide():
    btn_unhide(6)
def btn8_unhide():
    btn_unhide(7)
def btn9_unhide():
    btn_unhide(8)
def btn10_unhide():
    btn_unhide(9)
def btn11_unhide():
    btn_unhide(10)
def btn12_unhide():
    btn_unhide(11)
def btn13_unhide():
    btn_unhide(12)
def btn14_unhide():
    btn_unhide(13)
def btn15_unhide():
    btn_unhide(14)
def btn16_unhide():
    btn_unhide(15)
def btn17_unhide():
    btn_unhide(16)
def btn18_unhide():
    btn_unhide(17)
def btn19_unhide():
    btn_unhide(18)
def btn20_unhide():
    btn_unhide(19)
#-------------------------------------------------------------------------------
previous_card = -1
clicks = 100
words = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"] #where numbers are button state
words += words
random.shuffle(words)

window = tk.Tk()
window.title("Moves left: 100")

for i in range(4):
    window.rowconfigure(i,minsize=80,weight=1)
for i in range(5):
    window.columnconfigure(i,minsize=160,weight=1)
#window.rowconfigure(0, minsize=80, weight=1)
#window.columnconfigure(0, minsize=80, weight=1)

btn1 = tk.Button(window,height=10,width=10,text="",command=btn1_unhide,bg='white') #sizes not in pixels...
btn2 = tk.Button(window,height=10,width=10,text="",command=btn2_unhide,bg='white')
btn3 = tk.Button(window,height=10,width=10,text="",command=btn3_unhide,bg='white')
btn4 = tk.Button(window,height=10,width=10,text="",command=btn4_unhide,bg='white')
btn5 = tk.Button(window,height=10,width=10,text="",command=btn5_unhide,bg='white')
btn6 = tk.Button(window,height=10,width=10,text="",command=btn6_unhide,bg='white')
btn7 = tk.Button(window,height=10,width=10,text="",command=btn7_unhide,bg='white')
btn8 = tk.Button(window,height=10,width=10,text="",command=btn8_unhide,bg='white')
btn9 = tk.Button(window,height=10,width=10,text="",command=btn9_unhide,bg='white')
btn10 = tk.Button(window,height=10,width=10,text="",command=btn10_unhide,bg='white')
btn11 = tk.Button(window,height=10,width=10,text="",command=btn11_unhide,bg='white')
btn12 = tk.Button(window,height=10,width=10,text="",command=btn12_unhide,bg='white')
btn13 = tk.Button(window,height=10,width=10,text="",command=btn13_unhide,bg='white')
btn14 = tk.Button(window,height=10,width=10,text="",command=btn14_unhide,bg='white')
btn15 = tk.Button(window,height=10,width=10,text="",command=btn15_unhide,bg='white')
btn16 = tk.Button(window,height=10,width=10,text="",command=btn16_unhide,bg='white')
btn17 = tk.Button(window,height=10,width=10,text="",command=btn17_unhide,bg='white')
btn18 = tk.Button(window,height=10,width=10,text="",command=btn18_unhide,bg='white')
btn19 = tk.Button(window,height=10,width=10,text="",command=btn19_unhide,bg='white')
btn20 = tk.Button(window,height=10,width=10,text="",command=btn20_unhide,bg='white')

cards = [[btn1,0],[btn2,0],[btn3,0],[btn4,0],[btn5,0],[btn6,0],[btn7,0],[btn8,0],[btn9,0],[btn10,0],[btn11,0],[btn12,0],[btn13,0],
[btn14,0],[btn15,0],[btn16,0],[btn17,0],[btn18,0],[btn19,0],[btn20,0]]
#cards = random.shuffle(cards)
#i = 0
for i, card in enumerate(cards): #this syntax iterates over the index (i) and the values (card) in a list (cards)
    card[0].grid(row=int(i/5), column=int(i%5), sticky="ew", padx=5, pady=5)
#-------------------------------------------------------------------------------

window.mainloop()
