from tkinter import *

window = Tk()

#title on the webpage
window.title("Restaurant Recommender")

#set window size when it pops up
window.geometry('350x200')

#header
h1 = Label(window, text="Welcome to the Restaurant Recommender System!",font=("Arial Bold", 20))  
h1.grid(row=0,column=0)

#caption under header
c1 = Label(window, text="Let us do the hard work of picking a restaurant for you.",font=("Arial Bold", 10))
c1.grid(row=1,column=0)

#adding a button
btn = Button(window, text="Click Me")
btn.grid(row=2,column=0)


window.mainloop()