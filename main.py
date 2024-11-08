import customtkinter

#watch the tutorial for this game at https://youtu.be/37kTR0VGfoE

clicks = 0
clickup = 1
cost = 15

def updatebutton():
    button2.configure(text=f"upgrade (cost: {cost})",command=clickupgrade)

def updatelable():
    lable1.configure(text=str(clicks))
    lable2.configure(text=f"click lvl {clickup}")

def click():
    global clicks, clickup
    clicks = 1 * clickup + clicks
    updatelable()

def clickupgrade():
    global clicks, clickup, cost

    if clicks >= cost:
        clickup = clickup + 1
        clicks = clicks - cost
        cost = cost * 2
        updatelable()
        updatebutton()
    

#this sets the default color themes
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

#this makes our window
#root is the window customtkinter.CTk() is a func for a window
root = customtkinter.CTk()
#geometry makes the size of our window or "root"
root.geometry("500x450")

#this makes the frame that we put all of our stuff in master must = root
frame = customtkinter.CTkFrame(master=root)
#element.pack is needed for all elements or they will not show
frame.pack(pady=10, padx=12)

lable = customtkinter.CTkLabel(master=frame, text="clicker game")
lable.pack(pady=10, padx=12)

lable1 = customtkinter.CTkLabel(master=frame, text=str(clicks))
lable1.pack(pady=10, padx=12)

lable2 = customtkinter.CTkLabel(master=frame, text=f"click lvl {clickup}")
lable2.pack(pady=10,padx=12)

button1 = customtkinter.CTkButton(master=frame, text="click", command=click)
button1.pack(pady=10,padx=12)

button2 = customtkinter.CTkButton(master=frame, text=f"upgrade (cost: {cost})",command=clickupgrade)
button2.pack(pady=10,padx=12)

#this is our gui loop
root.mainloop()
