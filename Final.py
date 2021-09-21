import time
from tkinter import *
from tkinter import messagebox
main_window = Tk()
screen_width = main_window.winfo_screenwidth()
screen_width=int(screen_width/2)
screen_height = main_window.winfo_screenheight()
screen_height=int(screen_height/1)
main_window.geometry(f'{screen_width}x{screen_height}')
#main_window.geometry("1200x600")
main_window.title('lmmm')
print(screen_width)
print(screen_height)
#main_window.iconbitmap('./lbb.ico')


    # Dropdown menu options
gpios = [
        " how",
    ]

global gpio_options_var
global gpio_value_var
global func_sel
global radio_value
global function_button

gpio_options_var = IntVar()
gpio_value_var = IntVar()
func_sel = IntVar()
radio_value= IntVar()

def read_device():
    print('device reading ....')
    device_cofigure_read.insert('end', 'Device Configuration reading....' + '\n')


def write_device():
    print('device reading ....')
    device_cofigure_read.insert('end', 'Device Configuration Writing....' + '\n')



def show():
    #global radio_value
    print(int(str(gpio_options_var.get())))


def close():
    str1= messagebox.askquestion("askquestion", "Are you sure?")
    if(str1=='yes'):
        print('if part')
        main_window.destroy()
    else:
        print('else part')    

def sel():
    #global radio_value
    selection = str(gpio_value_var.get())
    #print(selection)
    radio_value=int(selection)
    print(radio_value)
    

def program():
    global function_button
    print("Wait programmin is going on....")
    #messagebox.showinfo("showinfo", "Programming....")
    print(function_button.get())
    write_device()




def gpio_radio_button():
    

    global gpio_value_var
    frame = Frame(main_window,highlightbackground="green", highlightcolor="green", highlightthickness=4, width=100, height=100, bd=10)
    frame.pack()
    w = Label(frame, text ='SELECT GPIO', font = "12",   fg="white",
    bg="blue",
    relief="groove",pady=10, padx=10) 
    w.pack(side = TOP)
    bottomframe = Frame(main_window)
    bottomframe.pack(anchor=E, side = LEFT )
    
    gpio_option_0 = Radiobutton(frame, text="GPIO0", variable=gpio_options_var, value=0, command=show)#bg='grey', fg='black'
    gpio_option_0.pack(side = LEFT)

    gpio_option_1 = Radiobutton(frame, text="GPIO1", variable=gpio_options_var, value=1, command=show)
    gpio_option_1.pack(side = LEFT)

    gpio_option_2 = Radiobutton(frame, text="GPIO2", variable=gpio_options_var, value=2, command=show)
    gpio_option_2.pack(side = LEFT)

    gpio_option_3 = Radiobutton(frame, text="GPIO3", variable=gpio_options_var, value=3, command=show)
    gpio_option_3.pack(side = LEFT)

    gpio_option_4 = Radiobutton(frame, text="GPIO4", variable=gpio_options_var, value=4, command=show)
    gpio_option_4.pack(side = LEFT)

    gpio_option_5 = Radiobutton(frame, text="GPIO5", variable=gpio_options_var, value=5, command=show)
    gpio_option_5.pack(side = LEFT)

    gpio_option_6 = Radiobutton(frame, text="GPIO6", variable=gpio_options_var, value=6, command=show)
    gpio_option_6.pack(side = LEFT)

    gpio_option_7 = Radiobutton(frame, text="GPIO07", variable=gpio_options_var, value=7, command=show)
    gpio_option_7.pack(side = LEFT)

    gpio_option_8 = Radiobutton(frame, text="GPIO8", variable=gpio_options_var, value=8, command=show)
    gpio_option_8.pack(side = LEFT)

    gpio_option_9 = Radiobutton(frame, text="GPIO9", variable=gpio_options_var, value=9, command=show)
    gpio_option_9.pack(side = LEFT)

    gpio_option_10 = Radiobutton(frame, text="GPIO10", variable=gpio_options_var, value=10, command=show)
    gpio_option_10.pack(side = LEFT)
    
    gpio_option_11 = Radiobutton(frame, text="GPIO11", variable=gpio_options_var, value=11, command=show)
    gpio_option_11.pack(side = LEFT)

    gpio_option_12 = Radiobutton(frame, text="GPIO12", variable=gpio_options_var, value=12, command=show)
    gpio_option_12.pack(side = LEFT)

    gpio_option_13 = Radiobutton(frame, text="GPIO13", variable=gpio_options_var, value=13, command=show)
    gpio_option_13.pack(side = LEFT)

    gpio_option_14= Radiobutton(frame, text="GPIO14", variable=gpio_options_var, value=14, command=show)
    gpio_option_14.pack(side = LEFT)

    gpio_option_15 = Radiobutton(frame, text="GPIO15", variable=gpio_options_var, value=15, command=show)
    gpio_option_15.pack(side = LEFT)


def gpio_value_radio_button():
    
    
    frame = Frame(main_window,highlightbackground="green", highlightcolor="green", highlightthickness=4, width=20, height=20, bd=10)
    frame.pack()
    w = Label(frame, text ='GPIO VALUE', font = "12",   fg="white",
    bg="blue",
    relief="groove",pady=10, padx=10) 
    w.pack(side = TOP)
    bottomframe = Frame(main_window)
    bottomframe.pack( side = LEFT )
     
    gpio_value_0 = Radiobutton(frame, text="0", variable=gpio_value_var, value=0, command=sel)
    gpio_value_0.pack()

    gpio_value_1 = Radiobutton(frame, text="1", variable=gpio_value_var, value=1, command=sel)
    gpio_value_1.pack()

def function_selection():
    global function_button
    frame = Frame(main_window,highlightbackground="green", highlightcolor="green", highlightthickness=4, width=10, height=10, bd=10)
    frame.pack()
    w = Label(frame, text ='Function Seletion', font = "12",   fg="white",
    bg="blue",
    relief="groove",pady=10, padx=10) 
    w.pack(side = TOP)
    bottomframe = Frame(main_window)
    bottomframe.pack( side = RIGHT )
    

    # datatype of menu text
    function_button = StringVar(frame)

    # initial menu text
    function_button.set( "Advertek I2C" )


    # Create Dropdown menu
    drop = OptionMenu( frame , function_button , *gpios )
    drop.pack()



label = Label(
    text="Automation Tool ",
    fg="white",
    bg="blue",
    width=150,
    height=5,
    font=("Arial", 16),
    relief="groove",pady=10, padx=10
)
label.pack(anchor=N, side=TOP,padx=10, pady=10)
# Change the label text
connection_msg=StringVar()
connection_msg='Disconnected'
fg_color='red'
def connect_disconnect_selection():
    global function_button
    frame = Frame(main_window, width=20, height=2)
    frame.pack()
    w = Label(frame, text =connection_msg, font = "8",   fg=fg_color, bg="white",
    relief="sunken",pady=10, padx=10) 
    w.pack(side = BOTTOM)
    bottomframe = Frame(main_window)
    bottomframe.pack( side = LEFT )


######################################

#device_cofigure_read.insert('end', 'hello read device is as follows')

device_cofigure_read = Text(main_window, height = 30,
                width = 25,
                bg = "light yellow")
                
device_cofigure_read.pack(anchor=E,side=RIGHT,padx=10, pady=40)

gpio_radio_button()
gpio_value_radio_button()
function_selection()




#####################################





read_device_button = Button(main_window, text='Read Device Settings',width=30,  borderwidth=5,relief="raised",bg='white', command=read_device)
read_device_button.pack(anchor=S, side=LEFT,padx=15, pady=10)

configure_device = Button(main_window, text='Configure Device',width=30,  borderwidth=5,relief="raised",bg='white', command=program)
configure_device.pack(anchor=S, side=LEFT,padx=40, pady=10)


close_button = Button(main_window, text='Close',width=10,  borderwidth=5,relief="raised",bg='white', command=close)
close_button.pack(anchor=S, side=LEFT,padx=40, pady=10)
connect_disconnect_selection()

#disconnected = Label(main_window,text = "Disconnected",bg='white',fg='green')
#disconnected.pack(anchor=SE,side=LEFT,padx=10, pady=10)
#anchor=SW,
#main_window.resizable(False, False)
main_window.mainloop()






