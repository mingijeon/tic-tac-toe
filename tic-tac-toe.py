from tkinter import *
 
 def checked(i) :
       global player
       global count
       button = list[i]
 
       if button["text"] != "     " :
             return
       button["text"] = player 
       button["bg"] = "yellow"
 
       if player == "X" :
             player = "O"
             button["bg"] = "yellow"
       else :
             player = "X"
             button["bg"] = "lightgreen"
 
       count = count + 1
 
       if count >= 5 and checkedwinner(i//3, i%3) == 1 :
             print_whowin()
             window.destroy()
       elif count == 9 and checkedwinner(i//3, i%3) == 0 :
             print_draw()
             window.destroy()
 
 # cheked Who Win
 def checkedwinner(row, column) :
       if list[row*3]["text"] == list[row*3+1]["text"] == list[row*3+2]["text"] :
             return 1
       elif list[column]["text"] == list[column+3]["text"] == list[column+6]["text"] :
             return 1
       elif list[0]["text"] == list[4]["text"] == list[8]["text"] :
             return 1
       elif list[2]["text"] == list[4]["text"] == list[6]["text"] :
             return 1
       else :
             return 0
 # print who win
 def print_whowin() :
       if player == "X" :
             print("O Win!")
       elif player == "O" :
             print("X Win!")
 # print draw
 def print_draw() :
       print("Draw!")
 
 window = Tk()
 player = "X"
 count = 0
 list= []
 
 
 for i in range(9) :
       b = Button(window, text="     ", command=lambda k=i: checked(k))
       b.grid(row=i//3, column=i%3)
       list.append(b)
 
 window.mainloop()
