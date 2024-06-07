# Connect Four Game

import tkinter

window = tkinter.Tk()
window.title("Connect Four Game")

x= True

def connect4(button):
    global x,buttons,label
    if(x==True):
        button["command"]=""
        button["text"]="red"
        button.config(fg="red",bg="red")
        x=False
        if(buttons[0]["text"]=="red" and buttons[1]["text"]=="red" and buttons[2]["text"]=="red" and buttons[3]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[4]["text"]=="red" and buttons[1]["text"]=="red" and buttons[2]["text"]=="red" and buttons[3]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[5]["text"]=="red" and buttons[6]["text"]=="red" and buttons[7]["text"]=="red" and buttons[8]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[6]["text"]=="red" and buttons[7]["text"]=="red" and buttons[8]["text"]=="red" and buttons[9]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[10]["text"]=="red" and buttons[11]["text"]=="red" and buttons[12]["text"]=="red" and buttons[13]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[14]["text"]=="red" and buttons[11]["text"]=="red" and buttons[12]["text"]=="red" and buttons[13]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[15]["text"]=="red" and buttons[16]["text"]=="red" and buttons[17]["text"]=="red" and buttons[18]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[16]["text"]=="red" and buttons[17]["text"]=="red" and buttons[18]["text"]=="red" and buttons[19]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[0]["text"]=="red" and buttons[5]["text"]=="red" and buttons[10]["text"]=="red" and buttons[15]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[1]["text"]=="red" and buttons[6]["text"]=="red" and buttons[11]["text"]=="red" and buttons[16]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[2]["text"]=="red" and buttons[7]["text"]=="red" and buttons[12]["text"]=="red" and buttons[17]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[3]["text"]=="red" and buttons[8]["text"]=="red" and buttons[13]["text"]=="red" and buttons[18]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[4]["text"]=="red" and buttons[9]["text"]=="red" and buttons[14]["text"]=="red" and buttons[19]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[0]["text"]=="red" and buttons[6]["text"]=="red" and buttons[12]["text"]=="red" and buttons[18]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[1]["text"]=="red" and buttons[7]["text"]=="red" and buttons[19]["text"]=="red" and buttons[13]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[4]["text"]=="red" and buttons[8]["text"]=="red" and buttons[12]["text"]=="red" and buttons[16]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[3]["text"]=="red" and buttons[7]["text"]=="red" and buttons[11]["text"]=="red" and buttons[15]["text"]=="red"):
            label["text"]="Red Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        flag=1
        for i in buttons:
            if(button[i]["text"]==""):
                flag=0
                break
        if(flag==1):
            label["text"]="Game Over"
    else:
        button["text"]="blue"
        button["command"]=""
        button.config(fg="blue",bg="blue")
        x=True
        if(buttons[0]["text"]=="blue" and buttons[1]["text"]=="blue" and buttons[2]["text"]=="blue" and buttons[3]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[4]["text"]=="blue" and buttons[1]["text"]=="blue" and buttons[2]["text"]=="blue" and buttons[3]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[5]["text"]=="blue" and buttons[6]["text"]=="blue" and buttons[7]["text"]=="blue" and buttons[8]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[6]["text"]=="blue" and buttons[7]["text"]=="blue" and buttons[8]["text"]=="blue" and buttons[9]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[10]["text"]=="blue" and buttons[11]["text"]=="blue" and buttons[12]["text"]=="blue" and buttons[13]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[14]["text"]=="blue" and buttons[11]["text"]=="blue" and buttons[12]["text"]=="blue" and buttons[13]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[15]["text"]=="blue" and buttons[16]["text"]=="blue" and buttons[17]["text"]=="blue" and buttons[18]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[16]["text"]=="blue" and buttons[17]["text"]=="blue" and buttons[18]["text"]=="blue" and buttons[19]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[0]["text"]=="blue" and buttons[5]["text"]=="blue" and buttons[10]["text"]=="blue" and buttons[15]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[1]["text"]=="blue" and buttons[6]["text"]=="blue" and buttons[11]["text"]=="blue" and buttons[16]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[2]["text"]=="blue" and buttons[7]["text"]=="blue" and buttons[12]["text"]=="blue" and buttons[17]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[3]["text"]=="blue" and buttons[8]["text"]=="blue" and buttons[13]["text"]=="blue" and buttons[18]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[4]["text"]=="blue" and buttons[9]["text"]=="blue" and buttons[14]["text"]=="blue" and buttons[19]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[0]["text"]=="blue" and buttons[6]["text"]=="blue" and buttons[12]["text"]=="blue" and buttons[18]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[1]["text"]=="blue" and buttons[7]["text"]=="blue" and buttons[19]["text"]=="blue" and buttons[13]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[4]["text"]=="blue" and buttons[8]["text"]=="blue" and buttons[12]["text"]=="blue" and buttons[16]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        elif(buttons[3]["text"]=="blue" and buttons[7]["text"]=="blue" and buttons[11]["text"]=="blue" and buttons[15]["text"]=="blue"):
            label["text"]="Blue Win"
            for b in range(0,20):
                buttons[b]["command"]=""
        flag=1
        for i in buttons:
            if(button[i]["text"]==""):
                flag=0
                break
        if(flag==1):
            label["text"]="Game Over"

def replay():
    global x, buttons,label
    x=True
    label.destroy()
    for i in range(0,20):
      buttons[i].destroy()
      buttons=[]
      b=0
      for i in range(0,20):
          buttons.append(tkinter.Button(window,width=10))
      for r in range(4):
         for c in range(5):
             buttons[b]["command"]=lambda button=buttons[b]: connect4(button)
             buttons[b]["text"]=""
             buttons[b].grid(row=r,column=c)
             b+=1
             
      label = tkinter.Label( window, text="")
      label.grid(row=5,column=2)

      button20= tkinter.Button(window, text="Replay", width=10, command= replay)
      button20.grid(row=7, column=2)
      
      
buttons=[]
b=0
for i in range(0,20):
    buttons.append(tkinter.Button(window,width=10))
for r in range(4):
   for c in range(5):
       buttons[b]["command"]=lambda button=buttons[b]: connect4(button)
       buttons[b]["text"]=""
       buttons[b].grid(row=r,column=c)
       b+=1
       
label = tkinter.Label( window, text="")
label.grid(row=5,column=2)

button20= tkinter.Button(window, text="Replay", width=10, command= replay)
button20.grid(row=7, column=2)
    
window.mainloop()