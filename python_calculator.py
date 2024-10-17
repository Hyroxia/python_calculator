from tkinter import *
from tkinter import ttk

#Global Vars
unit_holder = ''
full_calculation_string = []
evaluated_string = ''

#creating the window and configuring it
main_window = Tk()
main_window.grid()
main_window.title("DAMF Calculator")
main_window.geometry("500x600")
main_window.resizable(width=False, height=False)

#preventing the cells from collapsing when empty
for num in range(1,50,1):
    main_window.grid_rowconfigure(num, minsize=20)
    main_window.grid_columnconfigure(num, minsize=50)

#various callable functions
def main_buttons():
    #Creating the main buttons
    home_button = Button(text='Home', font=(14), command=home_screen)
    calculator_button = Button(text='Calculator', font=(14),command=calculator_main)
    constants_button = Button(text='Constants',font=(14),command=constants_values)

    #Configuring the main buttons
    home_button.grid_configure(column=0,row=0)
    calculator_button.grid_configure(column=1,row=0)
    constants_button.grid_configure(column=2,row=0)
    
def clear_widgets():
    # Iterate through all children of the main window and destroy them
    for widget in main_window.winfo_children():
        widget.destroy()
    main_buttons()

def home_screen():
   #all text to be shown
    clear_widgets()
    main_window.geometry("500x600")
    
    welcome_text = Label(text="A Python Calculator", font="14")
    welcome_text_2 = Label(text="Created by:", font="14")
    welcome_text_3 = Label(text="Slarmie, Hendricks, Laubser, Ndlovu", font="14")
    welcome_text_4 = Label(text="In theory this was a good idea", font="14")
    
    #configuring text
    welcome_text.grid_configure(row=2,column=0,columnspan=2,sticky=W)
    welcome_text_2.grid_configure(row=3,column=0,columnspan=2,sticky=W)
    welcome_text_3.grid_configure(row=4,column=0,columnspan=4,sticky=W)
    welcome_text_4.grid_configure(row=27,column=0,columnspan=4,sticky=W)

def calculator_main():
    clear_widgets()
    main_window.geometry("500x600")
    calculator_main_button_1 = Button(text="Maths", font=(14),command=calculator_maths)
    calculator_main_button_2 = Button(text="Physics", font=(14),command=calculator_physics)
    
    calculator_main_button_1.grid_configure(row=3,column=0,sticky=W)
    calculator_main_button_2.grid_configure(row=3,column=1,sticky=W)

def calculator_maths():
    clear_widgets()
    calculator_main()
    global unit_holder
    global full_calculation_string
    global evaluated_string
    
    #Maths Calc Partial And Full Equation Display
    calculator_maths_partial_equation_head = Label(text="Partial Equation:",font=(14))
    calculator_maths_partial_equation = Label(text=unit_holder,font=(14))
    calculator_maths_full_equation_head = Label(text="Full Equation:",font=(14))
    calculator_maths_full_equation = Label(text=evaluated_string,font=(14))
    
    #Maths Calc Buttons (Numbers and Basic Functions)
    #still need command implementation
    calculator_maths_C = Button(text="C",font=(14),command=lambda:calculator_clearer('c'))
    calculator_maths_CE = Button(text="CE",font=(14),command=lambda:calculator_clearer('ce'))
    calculator_maths_AC = Button(text="AC",font=(14),command=main_window.destroy)
    calculator_maths_one = Button(text="1",font=(14),command=lambda:calculator_io_operations_maths('1'))
    calculator_maths_two = Button(text="2",font=(14),command=lambda:calculator_io_operations_maths('2'))
    calculator_maths_three = Button(text="3",font=(14),command=lambda:calculator_io_operations_maths('3'))
    calculator_maths_four = Button(text="4",font=(14),command=lambda:calculator_io_operations_maths('4'))
    calculator_maths_five = Button(text="5",font=(14),command=lambda:calculator_io_operations_maths('5'))
    calculator_maths_six = Button(text="6",font=(14),command=lambda:calculator_io_operations_maths('6'))
    calculator_maths_seven = Button(text="7",font=(14),command=lambda:calculator_io_operations_maths('7'))
    calculator_maths_eight = Button(text="8",font=(14),command=lambda:calculator_io_operations_maths('8'))
    calculator_maths_nine = Button(text="9",font=(14),command=lambda:calculator_io_operations_maths('9'))
    calculator_maths_zero = Button(text="0",font=(14),command=lambda:calculator_io_operations_maths('0'))
    calculator_maths_comma = Button(text=".",font=(14),command=lambda:calculator_io_operations_maths(','))
    calculator_maths_equals = Button(text="=",font=(14),command=lambda:calculator_io_operations_maths('='))
    
    calculator_maths_plus = Button(text="+",font=(14),command=lambda:calculator_io_operations_maths('+'))
    calculator_maths_minus = Button(text="-",font=(14),command=lambda:calculator_io_operations_maths('-'))
    calculator_maths_multiplication = Button(text="*",font=(14),command=lambda:calculator_io_operations_maths('*'))
    calculator_maths_division = Button(text="/",font=(14),command=lambda:calculator_io_operations_maths('/'))
    
    #Maths Calc Partial And Full Equation Display
    calculator_maths_full_equation_head.grid_configure(row=5,column=0,columnspan=2, sticky=W)
    calculator_maths_full_equation.grid_configure(row=6,column=0,columnspan=10, sticky=W)
    calculator_maths_partial_equation_head.grid_configure(row=7,column=0,columnspan=2, sticky=W)
    calculator_maths_partial_equation.grid_configure(row=8,column=0,columnspan=10, sticky=W)
    
    #Maths Calc Buttons (Numbers and Basic Functions) Display
    calculator_maths_C.grid_configure(row=10,column=2, sticky=NSEW)
    calculator_maths_CE.grid_configure(row=10,column=1, sticky=NSEW)
    calculator_maths_AC.grid_configure(row=10,column=0, sticky=NSEW)
    calculator_maths_nine.grid_configure(row=11,column=2, sticky=NSEW)
    calculator_maths_eight.grid_configure(row=11,column=1, sticky=NSEW)
    calculator_maths_seven.grid_configure(row=11,column=0, sticky=NSEW)
    calculator_maths_six.grid_configure(row=12,column=2, sticky=NSEW)
    calculator_maths_five.grid_configure(row=12,column=1, sticky=NSEW)
    calculator_maths_four.grid_configure(row=12,column=0, sticky=NSEW)
    calculator_maths_three.grid_configure(row=13,column=2, sticky=NSEW)
    calculator_maths_two.grid_configure(row=13,column=1, sticky=NSEW)
    calculator_maths_one.grid_configure(row=13,column=0, sticky=NSEW)
    calculator_maths_zero.grid_configure(row=14,column=0, sticky=NSEW)
    calculator_maths_comma.grid_configure(row=14,column=1, sticky=NSEW)
    calculator_maths_equals.grid_configure(row=14,column=2, sticky=NSEW)
    
    calculator_maths_plus.grid_configure(row=11,column=3, sticky=NSEW)
    calculator_maths_minus.grid_configure(row=12,column=3, sticky=NSEW)
    calculator_maths_multiplication.grid_configure(row=13,column=3, sticky=NSEW)
    calculator_maths_division.grid_configure(row=14,column=3, sticky=NSEW)

def calculator_physics():
    clear_widgets()
    calculator_main()
    global unit_holder
    global full_calculation_string
    
    #Physics Calc Partial And Full Equation Display
    calculator_physics_partial_equation_head = Label(text="Partial Equation:",font=(14))
    calculator_physics_partial_equation = Label(text=unit_holder,font=(14))
    calculator_physics_full_equation_head = Label(text="Full Equation:",font=(14))
    calculator_physics_full_equation = Label(text=full_calculation_string,font=(14))
    
    #Physics Calc Buttons (Numbers and Basic Functions)
    #still need command implementation
    calculator_physics_C = Button(text="C",font=(14),command=lambda:calculator_clearer('c'))
    calculator_physics_CE = Button(text="CE",font=(14),command=lambda:calculator_clearer('ce'))
    calculator_physics_AC = Button(text="AC",font=(14),command=main_window.destroy)
    calculator_physics_one = Button(text="1",font=(14),command=lambda:calculator_io_operations_physics('1'))
    calculator_physics_two = Button(text="2",font=(14),command=lambda:calculator_io_operations_physics('2'))
    calculator_physics_three = Button(text="3",font=(14),command=lambda:calculator_io_operations_physics('3'))
    calculator_physics_four = Button(text="4",font=(14),command=lambda:calculator_io_operations_physics('4'))
    calculator_physics_five = Button(text="5",font=(14),command=lambda:calculator_io_operations_physics('5'))
    calculator_physics_six = Button(text="6",font=(14),command=lambda:calculator_io_operations_physics('6'))
    calculator_physics_seven = Button(text="7",font=(14),command=lambda:calculator_io_operations_physics('7'))
    calculator_physics_eight = Button(text="8",font=(14),command=lambda:calculator_io_operations_physics('8'))
    calculator_physics_nine = Button(text="9",font=(14),command=lambda:calculator_io_operations_physics('9'))
    calculator_physics_zero = Button(text="0",font=(14),command=lambda:calculator_io_operations_physics('0'))
    calculator_physics_comma = Button(text=".",font=(14),command=lambda:calculator_io_operations_physics(','))
    calculator_physics_equals = Button(text="=",font=(14),command=lambda:calculator_io_operations_physics('='))
    
    calculator_physics_plus = Button(text="+",font=(14),command=lambda:calculator_io_operations_physics('+'))
    calculator_physics_minus = Button(text="-",font=(14),command=lambda:calculator_io_operations_physics('+'))
    calculator_physics_multiplication = Button(text="*",font=(14),command=lambda:calculator_io_operations_physics('+'))
    calculator_physics_division = Button(text="/",font=(14),command=lambda:calculator_io_operations_physics('+'))
    
    #Physics Calc Partial And Full Equation Display
    calculator_physics_full_equation_head.grid_configure(row=5,column=0,columnspan=2, sticky=W)
    calculator_physics_full_equation.grid_configure(row=6,column=0,columnspan=10, sticky=W)
    calculator_physics_partial_equation_head.grid_configure(row=7,column=0,columnspan=2, sticky=W)
    calculator_physics_partial_equation.grid_configure(row=8,column=0,columnspan=10, sticky=W)
    
    #Physics Calc Buttons (Numbers and Basic Functions) Display
    calculator_physics_C.grid_configure(row=10,column=2, sticky=NSEW)
    calculator_physics_CE.grid_configure(row=10,column=1, sticky=NSEW)
    calculator_physics_AC.grid_configure(row=10,column=0, sticky=NSEW)
    calculator_physics_nine.grid_configure(row=11,column=2, sticky=NSEW)
    calculator_physics_eight.grid_configure(row=11,column=1, sticky=NSEW)
    calculator_physics_seven.grid_configure(row=11,column=0, sticky=NSEW)
    calculator_physics_six.grid_configure(row=12,column=2, sticky=NSEW)
    calculator_physics_five.grid_configure(row=12,column=1, sticky=NSEW)
    calculator_physics_four.grid_configure(row=12,column=0, sticky=NSEW)
    calculator_physics_three.grid_configure(row=13,column=2, sticky=NSEW)
    calculator_physics_two.grid_configure(row=13,column=1, sticky=NSEW)
    calculator_physics_one.grid_configure(row=13,column=0, sticky=NSEW)
    calculator_physics_zero.grid_configure(row=14,column=0, sticky=NSEW)
    calculator_physics_comma.grid_configure(row=14,column=1, sticky=NSEW)
    calculator_physics_equals.grid_configure(row=14,column=2, sticky=NSEW)
    
    calculator_physics_plus.grid_configure(row=11,column=3, sticky=NSEW)
    calculator_physics_minus.grid_configure(row=12,column=3, sticky=NSEW)
    calculator_physics_multiplication.grid_configure(row=13,column=3, sticky=NSEW)
    calculator_physics_division.grid_configure(row=14,column=3, sticky=NSEW)

def calculator_io_operations_maths(unit):
    global unit_holder
    global full_calculation_string
    global evaluated_string
    if unit in ['*', '/', '-', '+']:
        full_calculation_string.append(unit_holder)
        full_calculation_string.append(unit)
        unit_holder=''
        evaluated_string = full_calculation_string
    elif unit == '=':
        full_calculation_string.append(unit_holder)
        expression_string = ''.join(full_calculation_string)
        try:
            ex_ev = eval(expression_string)
            evaluated_string.append(f'=')
            evaluated_string.append(ex_ev)
        except Exception as e:
            evaluated_string = f'Error: {e}'
    else:
        unit_holder += unit
    calculator_maths()
    
def calculator_io_operations_physics(unit):
    global unit_holder
    global full_calculation_string
    global evaluated_string
    if unit in ['*', '/', '-', '+']:
        full_calculation_string.append(unit_holder)
        full_calculation_string.append(unit)
        unit_holder=''
        evaluated_string = full_calculation_string
    elif unit == '=':
        full_calculation_string.append(unit_holder)
        expression_string = ''.join(full_calculation_string)
        try:
            ex_ev = eval(expression_string)
            evaluated_string.append(f'=')
            evaluated_string.append(ex_ev)
        except Exception as e:
            evaluated_string = f'Error: {e}'
    else:
        unit_holder += unit
    calculator_maths()
        
def calculator_clearer(char):
    global unit_holder
    global full_calculation_string
    global evaluated_string
    if char == "ce":
        unit_holder = ''
        full_calculation_string = []
        evaluated_string = ''
    else:
        unit_holder = ''
        
        
def constants_values():
    clear_widgets()
    main_window.geometry("1000x600")
    #Defining Maths Constants
    maths_label = Label(text="Maths Constants:", font=(14))
    maths_label_eulers_constant_e = Label(text="Eulers Constant (\"e\"): 2.7182818284",font=(14))
    maths_label_pi = Label(text="Eulers Constant (\"π\"): 3.141592654",font=(14))
    maths_label_golden_ratio = Label(text="Golden Ratio (\"φ\"): 1.6180339887498948482",font=(14))
    maths_label_eulers_constant_y = Label(text="Eulers Constant (\"γ\"): 0.577215664901532",font=(14))
    maths_label_imaginary = Label(text="imaginary unit (\"i\"): √-1",font=(14))
    maths_label_Khinchins = Label(text="Khinchin’s constant (\"K\"): 2.6854520010",font=(14))
    
    #Displaying Maths Constants
    maths_label.grid_configure(row=2,column=0,columnspan=5,sticky=W)
    maths_label_eulers_constant_e.grid_configure(row=4,column=0,columnspan=5,sticky=W)
    maths_label_eulers_constant_y.grid_configure(row=5,column=0,columnspan=5,sticky=W)
    maths_label_pi.grid_configure(row=6,column=0,columnspan=5,sticky=W)
    maths_label_golden_ratio.grid_configure(row=7,column=0,columnspan=5,sticky=W)
    maths_label_imaginary.grid_configure(row=8,column=0,columnspan=5,sticky=W)
    maths_label_Khinchins.grid_configure(row=9,column=0,columnspan=5,sticky=W)
    
    #Defining Physical Constants
    physics_label = Label(text="Physics Constants:", font=(14))
    physics_label_newtons_constant_of_grav = Label(text="Newtonian constant of gravitation (\"G\"): 6.67430 x 10⁻¹¹ m³ kg⁻¹ s⁻²", font=(14))
    physics_label_planks_constant = Label(text="Planck constant (\"h\"): 6.62607015 x 10-34 J Hz⁻¹", font=(14))
    physics_label_avogadro_constant = Label(text="Avogadro constant (\" Nₐ\"): 6.02214076 x 1023 mol⁻¹", font=(14))
    
    #Displaying Physical Constants
    physics_label.grid_configure(row=2,column=8,columnspan=5, sticky=W)
    physics_label_newtons_constant_of_grav.grid_configure(row=4,column=8,columnspan=5, sticky=W)
    physics_label_planks_constant.grid_configure(row=5,column=8,columnspan=5, sticky=W)
    physics_label_avogadro_constant.grid_configure(row=6,column=8,columnspan=5, sticky=W)

main_buttons()
home_screen()


#execute
main_window.mainloop()
