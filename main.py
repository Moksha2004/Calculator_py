import tkinter as tk
light_gery="#F5F5F5"
white="#FFFFFF"
label_colour="#25265E"
off_white="#F8FAFF"
light_blue="#CCEDFF"
fonts=("Arial",16)
bold_font=("Arial",40,"bold")
digit_font=("Arial",24,"bold")
default_font=("Arial",20)

class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(10,10)
        self.window.title("Calculator")

        self.total_expression=""
        self.current_expression=""
        #creating display
        self.display_frame=self.create_display_frame()
        #creating dictionary containing all buttons in the calculator
        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4: (2, 1),5:(2,2),6:(2,3),
            1: (3, 1),2:(3,2),3:(3,3),
            '.':(4,1),0:(4,2),
        }
        self.operations={"/": "\u00F7","*":"\u00D7","-":"-","+":"+"}
        self.total_label,self.label=self.create_display_labels()

        self.buttons_frame=self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
             self.buttons_frame.rowconfigure(x, weight=1)
             self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_oprator_buttons()
        self.create_special_button()
    #creating labels
    def create_special_button(self):
        self.create_clear_button()
        self.create_equal_button()
    def create_display_labels(self):#added colours,padding
        total_label=tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E,bg=light_gery,fg=label_colour,padx=24,font=fonts)
        total_label.pack(expand=True,fill="both")
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=light_gery,
                               fg=label_colour, padx=24, font=bold_font)
        label.pack(expand=True, fill="both")
        return total_label,label
    def add_to_current_expression(self,value):
        self.current_expression+=str(value)
        self.update_label()
    def create_display_frame(self):
        frame=tk.Frame(self.window, height=221, bg="#F5F5F5")
        frame.pack(expand=True,fill="both")
        return frame
    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.buttons_frame,text=str(digit),bg=white,fg=label_colour,font=digit_font,borderwidth=0,command=lambda x=digit :self.add_to_current_expression(x))
#command=self.add_to_current_expression(digit), this command has to be function, so we wrap it with lambda
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)
    def add_operator(self,operator):
        self.current_expression+=operator
        self.total_expression+=self.current_expression
        self.current_expression=""
        self.update_label()
        self.update_total_label()
    def create_oprator_buttons(self):
        i=0
        for operator,symbol in self.operations.items():
            button=tk.Button(self.buttons_frame,text=symbol,bg=off_white,fg=label_colour,font=default_font,borderwidth=0,
                             command=lambda x=operator:self.add_operator(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    def clear(self):
        self.total_expression=""
        self.current_expression=""
        self.update_total_label()
        self.update_label()
    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=off_white, fg=label_colour, font=default_font,
                           borderwidth=0,command=self.clear())
        button.grid(row=0, column=1,columnspan=3, sticky=tk.NSEW)
    def create_equal_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=light_blue, fg=label_colour, font=default_font,
                           borderwidth=0)
        button.grid(row=4, column=3,columnspan=3, sticky=tk.NSEW)
    def update_total_label(self):
        self.total_label.config(text=self.total_expression)
    def update_label(self):
        self.label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()
if __name__ =="__main__":
    cal=Calculator()
    cal.run()
