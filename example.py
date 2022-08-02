import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()
        
        #create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create widgets
        #Top frame
        self.label1 = tkinter.Label(self.top_frame, text='Richland College')

        self.my_button = tkinter.Button(self.bottom_frame, text='Click me!', command=self.showInfo)
        self.exit_button = tkinter.Button(self.bottom_frame, text='Exit Application', command=self.main_window.destroy)

        #Pack widgets
        #self.label1.pack(side='top')
        self.my_button.pack(side='left')
        self.exit_button.pack(side='left')

        #pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
       
        #Enter the tkinter main loop
        tkinter.mainloop()
    
#Handle button on click
    def displayMessage(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button')
    
    def showInfo(self):
        self.label1.pack(side='top')

#Create an instance of the MyGUI class
my_gui = myGUI()

