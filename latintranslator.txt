import tkinter
import tkinter.messagebox

class LatTransGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text = "English Translation is:")
        self.prompt_label.pack(side="left")
        self.sinister_button = tkinter.Button(self.bottom_frame, 
                                         text="sinister", 
                                         command=self.convert)
        self.dexter_buttom = tkinter.Button(self.bottom_frame,\
                                            text="dexter", \
                                            command=self.convert2)
        self.medium_buttom = tkinter.Button(self.bottom_frame, \
                                            text="medium", \
                                            command=self.convert3)
        self.label2 = tkinter.Label(self.bottom_frame, \
                                    text="Latin word is:")
        self.label2.pack(side="left")
        self.sinister_button.pack(side="left")
        self.dexter_buttom.pack(side="left")
        self.medium_buttom.pack(side="left")
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        self.label1 = tkinter.Label(self.top_frame,
                                    text="left")
        self.label1.pack(side="top")
        
    def convert2(self):
        self.label3 = tkinter.Label(self.top_frame,
                                     text="right")
        self.label3.pack(side="top")

    def convert3(self):
        self.label4 = tkinter.Label(self.top_frame,
                                    text="center")
        self.label4.pack(side="top")

english_conv = LatTransGUI()
