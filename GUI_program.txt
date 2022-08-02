# This is the first GUI program
# create a program that displays my name and address

import tkinter
import tkinter.messagebox

class MyGUI:
    def __in__(self):
        # create the main window widget.
        self.main_window = tkinter.Tk()

        # create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
       
        # Create a button widget.
        self.labell = tkinter.Label(self.top_frame, text="Show Info")    
        
        
        self.show_info_button = tkinter.Button(self.main_window, text="Show Info", command=self.display)

        # Create a Quit button
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        
        # Pack the button.
        
        self.show_info_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #enter the tkinter main loop.
        tkinter.mainloop()

    # The display method is a callback function for the Button widget.
    def display(self):
        # Display my name and address
        tkinter.messagebox.showinfo("Name and Address", "Elyse Konan\n763 McCallum Blvd\nDallas, TX 75243")

    def showInfo(self):
        self.labell.pack(side="top")

 
# Create an instance of MyGUI class.
my_gui = MyGUI()
