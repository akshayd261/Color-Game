import tkinter
import random

#list of colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

#Time variable
timeleft = 30


#Function to start the game
def startGame(event):
    if timeleft == 30:
        #start countdown timer
        countdown()

    #run the function to choose the next color
    nextColor()


#Function to choose and display the next color
def nextColor():
    global score
    global timeleft

    #if a game is currently in play
    if timeleft > 0:

        #make the text entry box active
        e.focus_set()

        #check if the color typed is equal to the color of the text
        if e.get().lower() == colors[1].lower():
            score += 1

        #clear the text entry box
        e.delete(0, tkinter.END)

        random.shuffle(colors)

        #change the color to type, by changing the text and the color to a random color value
        label.config(fg=str(colors[1]), text=str(colors[0]))

        #update the score
        scoreLabel.config(text="Score: " + str(score))

#Countdown time function
def countdown():
    global timeleft

    #if a game is in play
    if timeleft > 0:
        #decrement the timer
        timeleft -= 1

        #update the time left label
        timeLabel.config(text="Time left: "
                              + str(timeleft))

        #run the function again after 1 second
        timeLabel.after(1000, countdown)

#Driver code
#create GUI window
root = tkinter.Tk()

#set the title
root.title("COLORGAME")

#set the size
root.geometry("375x200")

#add an instructions label
instructions = tkinter.Label(root, text="Type in the color"
                                        "of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

#add a score label
scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()

#add a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                                     str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

#add a label for displaying the colors
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

#add a text entry box for typing in colors
e = tkinter.Entry(root)

#run the 'startGame' function when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

#set focus on the entry box
e.focus_set()

#start the GUI
root.mainloop() 