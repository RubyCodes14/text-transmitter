#IJN A
import tkinter as tk
#import re
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

'''
import pyttsx3
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 290)
'''

#CONTROL WINDOW
window1 = tk.Tk()
window1.title("Text Transmitter")
window1.iconbitmap("TTransmitter2.ico")
window1.geometry("850x650+250+20")
window1.configure(bg="#C3C3C3")

ctrl_win_bg = "#E3E3E3"         #Skin colour

ctrl_win = tk.Frame(window1, bd=10, relief=tk.FLAT, bg = ctrl_win_bg)
ctrl_win.pack(fill=tk.BOTH,)

#DISPLAY WINDOW
window2 = tk.Toplevel(window1)
window2.configure(bg = "#FCAAFE")
window2.iconbitmap("TTransmitter2.ico")

#***********RESPONSIVENESS*******************************
ctrl_win.rowconfigure(0, weight = 1, minsize = 400)     #display screen          *\
ctrl_win.rowconfigure(1, weight = 1, minsize = 50)          #menu bar                       *\
ctrl_win.rowconfigure(2, weight = 1, minsize = 130)         #text input frame              * > Frames
ctrl_win.rowconfigure(3, weight = 1, minsize = 50)          #buttons                          */
ctrl_win.columnconfigure([0, 1], weight = 1, minsize = 250)         #                  */
ctrl_win.columnconfigure(2, weight = 1, minsize = 100)

window2.rowconfigure(0, weight = 1, minsize = 600)
window2.columnconfigure(0, weight = 1, minsize = 800)
#**************************************************************
screenWidth = window2.winfo_screenwidth()
screenHeight = window2.winfo_screenheight()

# ********* FOR USING AN EXTENDED SCREEN **********
def  toggle_FullScreen():
    if extend_var.get() == "on":
        window2.geometry(str(screenWidth) + "x" + str(screenHeight) + "+" + str(screenWidth) + "+0")  
        window2.overrideredirect(1) #REMOVES THE TOP BADGE OF THE WINDOW - NO DRAGGING, NO BUTTONS, HIDES TASKBAR
        #window2.lift()
        window1.geometry("850x650+250+20")
    else:
        window1.lift()
        window1.geometry("850x650+50+20")
        window2.geometry("1000x650+300+25")
        window2.overrideredirect(0) 
        
#********* ****************

default = "Watch Here..."
text_input = default
display_type = "Characters"
from_chardisplay = False
autoFlag = False
from_worddisplay = False
store_chars = "" #Used in chardisplay() only
check_index = 2
text_typed = ""
auto_type_index = 0
auto_type_index1 = 0
word_index = 0
delay_time = 500
font_perc = 85
#Control Window - Window Skin -- still set up ^ under window1 initialization --defined twice ---scroll up 
ctrl_win_bg = ctrl_win_bg
#Control/Display Screen Bg & Fg colour
screen_bg = "#FFFFFF"
screen_fg = "#000000"
#Buttons Colour
enable_colour = "#FFFFFF"#DFE8DA"
disable_colour  = "#E3E3E3"

def percent(val, perc):
    val += 1
    try:
        nval = int(val * (perc / 100))
    except e as ZeroDivisionError:
        nval = int(val * (perc / 100))
    return nval

def set_font(Text):
    wordlen = len(Text)
    len_perc = percent(wordlen, font_perc)
    if wordlen == 1:
        size = (500 // len_perc)
    elif wordlen > 1:
        size = int((500 // len_perc) * 2.6)
    else:
        size = 500
    font = ("Cambria", size, "bold")
    lbl_textWin2["font"] = font
    size1 = int(size // 1.8)
    lbl_textWin1["font"] = ("Cambria", size1, "bold")
    '''
    if len(lbl_textWin1["text"]) > 3:
        font = ("Cambria", 50, "bold")
    else:
        font = ("Cambria", 500, "bold")
    
    lbl_textWin2["font"] = font
    #return font'''

def get_text(event):
    global text_typed
    text_typed += event.char #ent_text.get(1.0, tk.END)#
    
    #return text_typed

def set_display_type(event):
    global display_type
    display_type = combo_display_var.get()    #sets the display type global variable
    if display_type == "Words":
        type_combo.current(1)     #sets typing method to authomatic
        enable_btns()
    ent_text.focus_set() #Sets the cursor back in the text box

def update_text(txt):
    set_font(txt)
    lbl_textWin1["text"] = txt
    lbl_textWin2["text"] = txt

    lbl_textWin1["bg"] = screen_bg
    lbl_textWin1["fg"] = screen_fg
    lbl_textWin2["bg"] = screen_bg
    lbl_textWin2["fg"] = screen_fg
    #audio_text(txt)#############################################################
        
def display_text(curr_text):
    global text_typed
    #set_display_type()
    if display_type == "Characters":
        output = chardisplay(curr_text)
        
    elif display_type == "Words":
        output = worddisplay(text_typed)   
        
    elif display_type == "Words by Chars":
        output = words_byChar_display(curr_text)

    else:
        output = "Unknown Error..."
        
    update_text(output)

def backspace_text(event):
    global text_typed
    if event.keysym == "BackSpace":
        width = len(text_typed) - 1
        text_typed = text_typed[:width]
        lbl_char_no["text"]  = ("Total Chars: {0}".format(len(text_typed)))
        text_input = ""
        #update_text(text_typed[:width])
        try:
            if display_type == "Characters":
                display_text(text_typed[-1])
            elif display_type == "Words":
                pass
            elif display_type == "Words by Chars":
                pass
            
        except(IndexError):
            pass


def chardisplay(char_):
    global text_input, from_chardisplay, store_chars, check_index
    from_chardisplay = True
    store_chars  += char_
    lbl_textWin1["font"] = ("Cambria", 180, "bold")
    lbl_textWin2["font"] = ("Cambria", 500, "bold")
    if len(store_chars) > 1:
        if store_chars[-1] == store_chars[-check_index]:            # or ord(store_chars[-1]) == ord(store_chars[-check_index]) + 32:
            text_input = store_chars[-1] * abs(check_index)      #ord(store_chars[-1]) == ord(store_chars[-check_index]) - 32:
            check_index += 1
        else:
            text_input = char_
            check_index = 2
    else:
            text_input = char_
            check_index = 2
    return text_input

def worddisplay(whole_text, pause = True):
    global text_input, auto_type_index, text_typed, from_worddisplay
    from_worddisplay = True
    text_input = " "
    whole_text = whole_text.replace("\n", " ").split(" ")
   #whole_text = re.findall(r"[\w']+", whole_text)
    
    if auto_type_index < len(whole_text):
        text_input = whole_text[auto_type_index]
    """
        if auto_type_index >= 1:
            prevText = whole_text[auto_type_index ]
            if "." in prevText or "," in prevText or ";" in prevText or ":" in prevText or "!" in prevText:
                text_input = " "
                auto_type_index -= 1
       """
    return text_input


def words_byChar_display(char0):
    global text_input, from_chardisplay
    if char0.isspace():
        text_input = " "
    elif  from_chardisplay or text_input == default:
        text_input = char0
        from_chardisplay = False
    else:
        text_input += char0
        
        '''if len(text_input) > 12 and "\n" not in text_input:
            text_input += "\n"
        '''
    return text_input

def manual_typing(text):
    global autoFlag
    if combo_display_var.get() == "Words":
        display_type_combo.current(1)     #set to words_by_character
    btn_auto_start["state"] = "disabled"
    btn_rpt_auto_start["state"] = "disabled"
    btn_stop_auto["state"] = "disabled"
    btn_stop_auto["bg"] = disable_colour
    if not(text) == "":
        typed_char = text[-1]
    else:
        typed_char = ""
    if not(autoFlag):
        display_text(typed_char)
    else:
        autoFlag = False

def repeat_autotyping():
    auto_typing()
    start_autotyping()
    
def auto_typing():
    global auto_type_index
    auto_type_index = 0
    btn_auto_start["state"] = "normal"
    btn_rpt_auto_start["state"] = "normal"
    #get_text()
    #return text_typed

def start_autotyping():
    global auto_type_index, text_input, delay_time, loop, from_worddisplay
    loop = window1.after(delay_time, start_autotyping)
    #set_font()
    cursorPoint_text_typed = text_typed
    if from_worddisplay or combo_display_var.get() == "Words":
        length = len(text_typed.replace("\n", " ").split(" "))
        #length = len(re.findall(r"[\w']+", text_typed))
        from_worddisplay = False
    else:
        length = len(text_typed)
        
    if auto_type_index >= length :
        text_input = ""
        window1.after_cancel(loop)
        
        enable_btns()
    else:
        display_text(cursorPoint_text_typed[auto_type_index])
        auto_type_index += 1
        
        disable_btns()

def stop_autotyping():
    try:
        window1.after_cancel(loop)
    except(NameError):
        update_text("Error... L0-279+")
    enable_btns()

def get_filesource():
    global text_input, text_typed
    text_file = filedialog.askopenfilename()
    type_combo.current(1)
    btn_auto_start["state"] = "normal"
    btn_auto_start["bg"] = enable_colour      
    btn_rpt_auto_start["state"] = "normal"
    btn_rpt_auto_start["bg"] = enable_colour
    try:
        with open(text_file, "r", encoding = "utf-8") as file:
            text_typed = file.read()
    except(FileNotFoundError, UnicodeDecodeError):
        if text_file:
            messagebox.showinfo("Error", "Unable to open file. \n\nHints:\n* Upload a text file only.\n* Change file location and try again.")
        #lbl_textWin1["text"] =  text_typed
    finally:
        ent_text.delete(1.0, tk.END)
        ent_text.insert(1.0, text_typed)
        lbl_char_no["text"]  = ("Total Chars: {0}".format(len(text_typed)))
        text_source_combo.current(0)
    
    
def set_typing_method(event):
    global text_typed, autoFlag 
    #get_text()
    activate_btns()
    man_aut = combo_typing_method_var.get()
    if  man_aut == "Manual":
        manual_typing(text_typed)
    elif man_aut == "Automatic":
        autoFlag = True
        #pass#auto_typing()
    else:
        lbl_textWin1["text"] = "Error"    
    #set_font()
    ent_text.focus_set() #Sets the cursor back in the text box
    lbl_char_no["text"]  = ("Total Chars: {0}".format(len(text_typed)))
    
def select_text_source(event):
    type_upload = combo_text_source_var.get()
    if type_upload == "Type in text Box":
         set_typing_method(event)
    elif type_upload == "Upload text File":
        get_filesource()

    ent_text.focus_set() #Sets the cursor back in the text box
        #pass
    
def execute(event):
    global text_typed
    try:
        if event.char.isprintable and 128 > ord(event.char) > 31 :
            get_text(event)
            select_text_source(event)
        else:
            #lbl_textWin2["text"] = event.keysym
            pass
    except(TypeError):
        pass
    
    if len(text_typed) > 0:
        backspace_text(event)

def enable_btns():
    btn_auto_start["state"] = "normal"
    btn_auto_start["bg"] = enable_colour
        
    btn_rpt_auto_start["state"] = "normal"
    btn_rpt_auto_start["bg"] = enable_colour

    btn_stop_auto["state"] = "disabled"
    btn_stop_auto["bg"] = disable_colour

def disable_btns():
    btn_auto_start["state"] = "disabled"
    btn_auto_start["bg"] = disable_colour
          
    btn_rpt_auto_start["state"] = "disabled"
    btn_rpt_auto_start["bg"] = disable_colour

    btn_stop_auto["state"] = "normal"
    btn_stop_auto["bg"] = enable_colour

    
def activate_btns():
    if combo_typing_method_var.get() == "Automatic":
        enable_btns()

    elif combo_typing_method_var.get() == "Manual":
        disable_btns()

def set_delay(event):
    global delay_time
    delay_time = int(eval(combo_typing_delay_var.get()[:-5]) * 1000)
    ent_text.focus_set() #Sets the cursor back in the text box

'''def audio_text(text):
    engine.say(text)
    engine.runAndWait()'''
              
#***************EVENT TRIGGERS************************
def get_event():
    ent_text.focus_set()
    ent_text.bind("<KeyPress>", execute)

#*********************************************************

def clear_current_display():
    global text_input, store_chars, auto_type_index1
    text_input = ""
    store_chars = ""
    update_text(text_input)


#CONTROL WORD                                                                                            ^
#Control Window is grided into 4-rows and 3 columns -- Responsive |
#---------------DISPLAY FRAME---------------------------
frm_display = tk.Frame(ctrl_win, bg = ctrl_win_bg, relief = tk.GROOVE, bd=1)
frm_display.grid(row = 0, column = 0, sticky = "nsew", columnspan=3)

lbl_textWin1 = tk.Label(frm_display, text = default, bg=screen_bg, fg=screen_fg, font = ("Cambria", 70, "bold"))#get_text())
lbl_textWin1.pack(fill = tk.BOTH, expand = True)
#-----------------------------------------------------------------------------

#-------------MENU FRAME--------------------------
frm_menu = tk.Frame(ctrl_win, bg = ctrl_win_bg)# "#EFEFEF",)#relief = tk.GROOVE, bd=5)
frm_menu.grid(row = 1, column = 0, sticky = "nsew", columnspan=3)

#Menu Frame is grided into 1-row and 6-columns -- Responsive
frm_menu.rowconfigure(0, weight = 1, minsize = 2,)
frm_menu.columnconfigure([0, 1, 2, 3], weight = 1, minsize = 10)
frm_menu.columnconfigure(4, weight = 1, minsize = 5)
frm_menu.columnconfigure(5, weight = 1, minsize = 5)

#-------------------------------------------------------------------------------------------------

#------------------MENU ITEMS---------------------------------------------------------------
menu_sticky = "nsew"
#Background colour
menu_bg = ctrl_win_bg#"#0000FF"
menu_lbl_bg = menu_bg
#
menu_bd = 1
menu_relief = tk.FLAT
menu_font = ("default", 10, "normal")

#Extend Screen Check Button - Column 1
extend_var = StringVar()
check_btn_extend = Checkbutton(frm_menu, text = "Extend Screen", fg="black", bg=menu_bg, variable = extend_var, onvalue = "on", offvalue = "off",
                               command=toggle_FullScreen, activeforeground = "#FF0000", selectcolor="#FFFFFF", underline=0, font=menu_font)
check_btn_extend.select()
check_btn_extend.grid(row=0, column=0, sticky=menu_sticky)

#Display Combo Box - Column 2
#Frame - Container for "Label and DropDown"
frm_disp_combo_lbl = tk.Frame(frm_menu, bg=menu_bg)
frm_disp_combo_lbl.grid(row=0, column=1, sticky=menu_sticky)

display_options = ["Characters", "Words by Chars", "Words"]

lbl_display_type = tk.Label(frm_disp_combo_lbl, bg = menu_lbl_bg, text ="Display Type: ", bd=menu_bd, relief=menu_relief, font=menu_font)
lbl_display_type.pack(side=LEFT)#grid(row=row_disp, column=column_disp, sticky="nsew")

combo_display_var = StringVar()
display_type_combo = ttk.Combobox(frm_disp_combo_lbl, width=12, textvariable=combo_display_var, value=display_options, state = "readonly")
display_type_combo.current(0)
display_type_combo.pack(side=LEFT)#grid(row=row_disp, column=column_disp+1)
display_type_combo.bind("<<ComboboxSelected>>", set_display_type)

#Typing Combo Box
frm_typing_combo = tk.Frame(frm_menu, bg = menu_bg)
frm_typing_combo.grid(row=0, column=2, sticky=menu_sticky)

typing_options = ["Manual", "Automatic"]

lbl_typing = tk.Label(frm_typing_combo, bg = menu_lbl_bg, text ="Typing: ", bd=menu_bd, relief=menu_relief, font=menu_font)
lbl_typing.pack(side=LEFT)#grid(row=row_disp, column=column_disp, sticky="nsew")

combo_typing_method_var = StringVar()
type_combo = ttk.Combobox(frm_typing_combo, width=8, textvariable=combo_typing_method_var, value=typing_options, state = "readonly")
type_combo.current(0)
type_combo.pack(side=LEFT)#grid(row=row_disp, column=column_disp+1)
type_combo.bind("<<ComboboxSelected>>", set_typing_method)

#TEXT SOURCE
text_source_combo_frm = tk.Frame(frm_menu, bg = menu_bg)
text_source_combo_frm.grid(row=0, column=3, sticky=menu_sticky)

text_source_options = ["Type in text Box", "Upload text File"]

lbl_text_source = tk.Label(text_source_combo_frm, bg = menu_lbl_bg, text ="Text Source: ", bd=menu_bd, relief=menu_relief, font=menu_font)
lbl_text_source.pack(side=LEFT)

combo_text_source_var = StringVar()
# the 'postcommand' parameter updates the options before displaying tbe drop-down menu 
text_source_combo = ttk.Combobox(text_source_combo_frm, width=14, textvariable=combo_text_source_var, value=text_source_options, state = "readonly")
text_source_combo.current(0)
text_source_combo.pack(side=LEFT)
text_source_combo.bind("<<ComboboxSelected>>", select_text_source)

#Auto Typing Delay Time Combo Box
frm_typing_delay_combo = tk.Frame(frm_menu, bg = menu_bg)
frm_typing_delay_combo.grid(row=0, column=4, sticky=menu_sticky)

delay_options = ["0.25 secs", "0.5 secs", "0.75 secs", "1 secs", "2 secs", "3 secs", "4 secs"]

lbl_delay_time = tk.Label(frm_typing_delay_combo, bg = menu_lbl_bg, text ="Delay: ", bd=menu_bd, relief=menu_relief, font=menu_font)
lbl_delay_time.pack(side=LEFT)

combo_typing_delay_var = StringVar()
typing_delay_combo = ttk.Combobox(frm_typing_delay_combo, width=7, textvariable=combo_typing_delay_var, value=delay_options, state = "readonly")
typing_delay_combo.current(0)
typing_delay_combo.pack(side=LEFT)
typing_delay_combo.bind("<<ComboboxSelected>>", set_delay)

#CLEAR BUTTON
btn_clear_display = tk.Button(frm_menu, height = 0, text="Clear", font=("helvetica", 10, "bold"), bg = "#F5F5F5", fg="red", command=clear_current_display)
btn_clear_display.grid(row=0, column=5, padx=(5, 5), ipadx=5, ipady=2)# sticky="ew")

#------------------------------------------------------------

#--------------INPUT FRAME-------------------------
inputColour = "#C3C3C3"

frm_input = tk.Frame(ctrl_win, bg=inputColour)
frm_input.grid(row = 2, column = 0, sticky = "nsew", columnspan=3)

lbl_prompt = tk.Label(frm_input, text="Type in the box below:", bg=ctrl_win_bg, relief=tk.GROOVE, bd=2)
lbl_prompt.pack(fill=tk.X)#grid(row=1, column=0, columnspan=3, sticky="nsew")

#Total Characters in Text Box
lbl_char_no = tk.Label(lbl_prompt, text="Total Chars: 0", bg=ctrl_win_bg, relief=tk.GROOVE, bd=0)
lbl_char_no.pack(side=RIGHT, padx=(0, 30))

#Scrollbar
scrollbar = Scrollbar(frm_input)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

ent_text = tk.Text(frm_input, bg="#FFFFFF", relief=tk.RAISED, bd=2, wrap = tk.WORD, yscrollcommand = scrollbar.set)
ent_text.pack(fill=tk.BOTH)
scrollbar.config(command = ent_text.yview)
#ent_text.insert(1.0, "Here You Go: ")
#-----------------------------------------------------------------------------

#---------------------------------------------------------------------------------

#------------------BUTTONS ------------------------------------------
#bg="#00AFFF"
btn_bg = "#E3E3E3"
btn_rpt_auto_start = tk.Button(ctrl_win, state="disabled", bg=btn_bg, text="Start Over", font=("Cambria", 15, "bold"), command=repeat_autotyping)
btn_rpt_auto_start.grid(row = 3, column = 0, sticky = "nsew", pady=(15,0))#.pack(side=RIGHT)

btn_auto_start = tk.Button(ctrl_win, state="disabled", bg= btn_bg, text="Start/Continue", font=("Cambria", 15, "bold"), command=lambda: [clear_current_display(), start_autotyping()])
btn_auto_start.grid(row = 3, column = 1, sticky = "nsew", padx=10, pady=(15,0))#.pack(side=RIGHT)

btn_stop_auto = tk.Button(ctrl_win, state="disabled", bg=btn_bg, text="Stop/Pause", font=("Cambria", 15, "bold"), command=stop_autotyping)
btn_stop_auto.grid(row = 3, column = 2, sticky = "nsew", pady=(15,0))#.pack(side=RIGHT)
#-----------------------------------------------------------------------------------

#DISPLAY/OUTPUT WINDOW
lbl_textWin2 = tk.Label(window2, text =  default, bg = screen_bg, fg=screen_fg, font = ("Cambria", 110, "bold"))  
lbl_textWin2.grid(row = 0, column = 0, sticky = "nsew", ipadx=20, ipady=20)#pack(fill = tk.BOTH, expand = True)

#***********EVENT TRIGGERS CALLING*****************
toggle_FullScreen()
'''
typing()
get_delay()
'''

get_event()

#******************************************************

window1.mainloop()
