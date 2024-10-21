from tkinter import *
from tkinter import ttk
import math

#planned expansion and refractoring of IO operations -> % and trigs
#draft plan for Constants implementation
#look towards eventual frame implementation
#Raise the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
    
#Global Vars
unit_holder = ''
full_calculation_string = []
evaluated_string = ''
partial_expression_label = None
full_expression_label = None

#creating the window and configuring it
main_window = Tk()
main_window.grid()
main_window.title("DAMF Calculator")
main_window.geometry("540x600")
main_window.resizable(width=False, height=False)
main_window.configure(bg='#e6e6e6')

#preventing the cells from collapsing when empty
for num in range(1,50,1):
    main_window.grid_rowconfigure(num, minsize=20)
    main_window.grid_columnconfigure(num, minsize=40)

#various callable functions
#button creation creates the various buttons. we only take [text, row, column, command, columnspan, bg and fg]
def button_creation(expected_text, expected_row, expected_column, expected_command, expected_columnspan, expected_bg, expected_fg):
    button = Button(text=expected_text, font=(14), command=expected_command,bg=expected_bg,fg=expected_fg)
    button.grid(row=expected_row,column=expected_column, sticky=NSEW)

#label creation does a similar thing to button. we only take [text, row, column, columnspan, bg, fg and sticky]
def label_creation(expected_text, expected_row, expected_column, expected_columnspan, expected_bg, expected_fg, expected_sticky):
    label = Label(text=expected_text, font=(14), bg=expected_bg, fg=expected_fg)
    label.grid_configure(row=expected_row, column=expected_column,columnspan=expected_columnspan,sticky=expected_sticky)

#this creates the buttons Home, Calculator and Constants
def main_buttons():
    #Creating the main buttons
    home_button = Button(text='Home', font=(14), command=home_screen, bg='#003366', fg="#e0ffff")
    calculator_button = Button(text='Calculator', font=(14),command=calculator_main, bg='#003366', fg="#e0ffff")
    constants_button = Button(text='Constants',font=(14),command=constants_values, bg='#003366', fg="#e0ffff")

    #Configuring the main buttons
    home_button.grid_configure(column=0,row=0)
    calculator_button.grid_configure(column=1,row=0)
    constants_button.grid_configure(column=2,row=0)

#This clears every widget on screen, then calls main_buttons to replace it onto the window
def clear_widgets():
    # Iterate through all children of the main window and destroy them
    for widget in main_window.winfo_children():
        widget.destroy()
    main_buttons()

def home_screen():
   #all text to be shown
    clear_widgets()
    main_window.geometry("540x600")
    
    welcome_text = Label(text="A Python Calculator", font="14", bg='#e6e6e6', fg="#2B2828")
    welcome_text_2 = Label(text="Created by:", font="14", bg='#e6e6e6', fg="#2B2828")
    welcome_text_3 = Label(text="Slarmie, Hendricks, Laubser, Ndlovu", font="14", bg='#e6e6e6', fg="#2B2828")
    welcome_text_4 = Label(text="In theory this was a good idea", font="14", bg='#e6e6e6', fg="#2B2828")
    warning_text_1 = Label(text="Note: All buttons that are light orange is non-funtional", font=(14), bg='#e6e6e6', fg="#2B2828")
    
    #configuring text
    welcome_text.grid_configure(row=2,column=0,columnspan=3,sticky=W)
    welcome_text_2.grid_configure(row=3,column=0,columnspan=3,sticky=W)
    welcome_text_3.grid_configure(row=4,column=0,columnspan=5,sticky=W)
    welcome_text_4.grid_configure(row=27,column=0,columnspan=5,sticky=W)
    warning_text_1.grid_configure(row=6,column=0,columnspan=8, sticky=W)

def calculator_main():
    clear_widgets()
    main_window.geometry("540x600")
    #creates the buttons to choose between maths or physics
    calculator_main_button_1 = Button(text="Maths", font=(14),command=calculator_maths,bg='#003366', fg="#e0ffff")
    calculator_main_button_2 = Button(text="Physics", font=(14),command=calculator_physics,bg='#003366', fg="#e0ffff")
    
    calculator_main_button_1.grid_configure(row=3,column=0,sticky=W)
    calculator_main_button_2.grid_configure(row=3,column=1,sticky=W)

#stopgap solution of placing partial_expression and full_expression into global until fix can be found in updating display
def calculator_display(): 
    global unit_holder
    global evaluated_string
    global partial_expression_label, full_expression_label

    # Destroy only the specific labels that need to be updated
    if partial_expression_label:
        partial_expression_label.destroy()
    if full_expression_label:
        full_expression_label.destroy()

    # Create new labels with updated text
    display_partial_expression_head = Label(text="Partial Equation:", font=(14), bg='#e6e6e6', fg="black")
    partial_expression_label = Label(text=unit_holder, font=(14), bg='#e6e6e6', fg="black")  # Update with unit_holder
    display_full_expression_head = Label(text="Full Equation:", font=(14), bg='#e6e6e6', fg="black")
    full_expression_label = Label(text=evaluated_string, font=(14), bg='#e6e6e6', fg="black")  # Update with evaluated_string

    # Layout the new labels in the grid
    display_full_expression_head.grid(row=5, column=0, columnspan=2, sticky=W)
    full_expression_label.grid(row=6, column=0, columnspan=10, sticky=W)
    display_partial_expression_head.grid(row=7, column=0, columnspan=2, sticky=W)
    partial_expression_label.grid(row=8, column=0, columnspan=10, sticky=W)

def calculator_backspace():
    global full_calculation_string, unit_holder, evaluated_string

    # Check if unit_holder contains a value
    if unit_holder:
        # Remove the last character from unit_holder
        unit_holder = unit_holder[:-1]
        calculator_display()
    else:
        # Remove the last character from full_calculation_string
        full_calculation_string = full_calculation_string[:-1]
        evaluated_string = evaluated_string[:-1]
        calculator_display()

#does the calculations for the maths calculator - Seperated until improved handling of physics constants and maths constants
def calculator_io_operations(unit):
    global unit_holder
    global full_calculation_string
    global evaluated_string

    # Handle mathematical operations and functions
    if unit in ['*', '/', '-', '+', '(', ')', 'tan(', 'sin(', 'cos(','sin⁻¹(', 'cos⁻¹(', 'tan⁻¹(','%']:
        if unit == '(':
            # If there's a current number in unit_holder, append it before adding '('
            if unit_holder:
                full_calculation_string.append(unit_holder)
                full_calculation_string.append('*')  # Implicit multiplication
                unit_holder = ''  # Clear the unit holder
            full_calculation_string.append(unit)  # Append '('
        
        elif unit == ')':
            # Append the current number before the closing parenthesis if there's something in unit_holder
            if unit_holder:
                full_calculation_string.append(unit_holder)
                unit_holder = ''  # Clear the unit holder
            full_calculation_string.append(unit)  # Append ')'
        
        elif unit in ['sin(', 'cos(', 'tan(']:
            # If there's a current number, append it before the function
            if unit_holder:
                full_calculation_string.append(unit_holder)
                full_calculation_string.append('*')  # Implicit multiplication
                unit_holder = ''  # Clear the unit holder
            full_calculation_string.append(unit)  # Append the function
            
        elif unit in  ['sin⁻¹(', 'cos⁻¹(', 'tan⁻¹(']:
            # If there's a current number, append it before the function
            if unit_holder:
                full_calculation_string.append(unit_holder)
                full_calculation_string.append('*')  # Implicit multiplication
                unit_holder = ''  # Clear the unit holder
            full_calculation_string.append(unit)  # Append the function
            
        elif unit == '%':
            if unit_holder:
                # Convert the current unit holder to a percentage
                percent_value = f'({unit_holder}/100)'
                full_calculation_string.append(percent_value)
                unit_holder = ''
            else:
                # If no value in unit_holder, just append the % sign (or handle as you see fit)
                full_calculation_string.append(unit)

        # Update evaluated string
        evaluated_string = ''.join(full_calculation_string)
    
    elif unit == "ce":  # Clear everything
        unit_holder = ''
        full_calculation_string = []
        evaluated_string = ''
        calculator_display()
    
    elif unit == "c":  # Clear unit holder only
        unit_holder = ''
        calculator_display()
    
    elif unit == '=':
        if unit_holder:  # Append any remaining input
            full_calculation_string.append(unit_holder)
        
        expression_string = ''.join(full_calculation_string)  # Join full calculation string
        
        # Replace '^' with '**' for proper exponentiation
        expression_string = expression_string.replace('^', '**')
        expression_string = expression_string.replace('sin(', 'math.sin(')
        expression_string = expression_string.replace('cos(', 'math.cos(')
        expression_string = expression_string.replace('tan(', 'math.tan(')
        expression_string = expression_string.replace('sin⁻¹(', 'math.degrees(math.asin(')
        expression_string = expression_string.replace('cos⁻¹(', 'math.degrees(math.acos(')
        expression_string = expression_string.replace('tan⁻¹(', 'math.degrees(math.atan(')
        
        try:
            ex_ev = eval(expression_string)  # Evaluate the expression
            evaluated_string = [f'=', ex_ev]  # Update evaluated string with the result
        except Exception as e:
            evaluated_string = f'Error: {e}'
    
    else:  # For number inputs or other characters
        unit_holder += unit  # Append the input to the unit holder

    calculator_display()  # Update the display

#Maths calculator - Seperated due to constants buttons created
def calculator_maths():
    clear_widgets()
    calculator_main()
    calculator_display()
    global unit_holder
    global full_calculation_string
    global evaluated_string
    
    #goes in order [text,row,column,command,columnspan, bg, fg]
    maths_calculator_definitions = [
        ("C", 10, 0, lambda:calculator_io_operations('c'), 1,"#003366","#e0ffff"),
        ("CE", 10, 1, lambda:calculator_io_operations('ce'), 1,"#003366","#e0ffff"),
        ("⌫", 10, 2, lambda:calculator_backspace(), 1,"#003366","#e0ffff"),
        ("0", 14, 0, lambda:calculator_io_operations('0'), 1,"#003366","#e0ffff"),
        (",", 14, 1, lambda:calculator_io_operations('.'), 1,"#003366","#e0ffff"),
        ("=", 14, 2, lambda:calculator_io_operations('='), 1,"#003366","#e0ffff"),
        ("1", 13, 0, lambda:calculator_io_operations('1'), 1,"#003366","#e0ffff"),
        ("2", 13, 1, lambda:calculator_io_operations('2'), 1,"#003366","#e0ffff"),
        ("3", 13, 2, lambda:calculator_io_operations('3'), 1,"#003366","#e0ffff"),
        ("4", 12, 0, lambda:calculator_io_operations('4'), 1,"#003366","#e0ffff"),
        ("5", 12, 1, lambda:calculator_io_operations('5'), 1,"#003366","#e0ffff"),
        ("6", 12, 2, lambda:calculator_io_operations('6'), 1,"#003366","#e0ffff"),
        ("7", 11, 0, lambda:calculator_io_operations('7'), 1,"#003366","#e0ffff"),
        ("8", 11, 1, lambda:calculator_io_operations('8'), 1,"#003366","#e0ffff"),
        ("9", 11, 2, lambda:calculator_io_operations('9'), 1,"#003366","#e0ffff"),
        ("+", 11, 3, lambda:calculator_io_operations('+'), 1,"#003366","#e0ffff"),
        ("-", 12, 3, lambda:calculator_io_operations('-'), 1,"#003366","#e0ffff"),
        ("*", 13, 3, lambda:calculator_io_operations('*'), 1,"#003366","#e0ffff"),
        ("/", 14, 3, lambda:calculator_io_operations('/'), 1,"#003366","#e0ffff"),
        ("(", 11, 4, lambda:calculator_io_operations('('), 1, "#003366", "#e0ffff"),
        (")", 12, 4, lambda:calculator_io_operations(')'), 1, "#003366", "#e0ffff"),
        ("^", 13, 4, lambda:calculator_io_operations('^'), 1, "#003366", "#e0ffff"),
        ("%", 14, 4, lambda:calculator_io_operations('%'), 1, "#003366", "#e0ffff"),
        ("<", 10, 3, "#", 1, "#FFB74D", "#C62828"),
        (">", 10, 4, "#", 1, "#FFB74D", "#C62828"),
        ("sin(", 10, 7, lambda:calculator_io_operations('sin('), 1, "#003366", "#e0ffff"),
        ("cos(", 10, 8, lambda:calculator_io_operations('cos('), 1, "#003366", "#e0ffff"),
        ("tan(", 10, 9, lambda:calculator_io_operations('tan('), 1, "#003366", "#e0ffff"),
        ("sin⁻¹(", 11, 7, lambda:calculator_io_operations('sin⁻¹('), 1, "#003366", "#e0ffff"),
        ("cos⁻¹(", 11, 8, lambda:calculator_io_operations('cos⁻¹('), 1, "#003366", "#e0ffff"),
        ("tan⁻¹(", 11, 9, lambda:calculator_io_operations('tan⁻¹('), 1, "#003366", "#e0ffff"),
        ]
    
    #takes all list info to the button_creation() function
    for ex_text, ex_row, ex_col, ex_command, ex_columnspan, ex_bg, ex_fg in maths_calculator_definitions:
        button_creation(ex_text, ex_row, ex_col, ex_command, ex_columnspan, ex_bg, ex_fg)

#Physics calculator - Seperated due to constants buttons created
def calculator_physics():
    clear_widgets()
    calculator_main()
    calculator_display()
    global unit_holder
    global full_calculation_string
    
    #goes in order [text,row,column,command,columnspan]
    physics_calculator_definitions = [
        ("C", 10, 0, lambda:calculator_io_operations('c'), 1,"#003366","#e0ffff"),
        ("CE", 10, 1, lambda:calculator_io_operations('ce'), 1,"#003366","#e0ffff"),
        ("⌫", 10, 2, lambda:calculator_backspace(), 1,"#003366","#e0ffff"),
        ("0", 14, 0, lambda:calculator_io_operations('0'), 1,"#003366","#e0ffff"),
        (".", 14, 1, lambda:calculator_io_operations('.'), 1,"#003366","#e0ffff"),
        ("=", 14, 2, lambda:calculator_io_operations('='), 1,"#003366","#e0ffff"),
        ("1", 13, 0, lambda:calculator_io_operations('1'), 1,"#003366","#e0ffff"),
        ("2", 13, 1, lambda:calculator_io_operations('2'), 1,"#003366","#e0ffff"),
        ("3", 13, 2, lambda:calculator_io_operations('3'), 1,"#003366","#e0ffff"),
        ("4", 12, 0, lambda:calculator_io_operations('4'), 1,"#003366","#e0ffff"),
        ("5", 12, 1, lambda:calculator_io_operations('5'), 1,"#003366","#e0ffff"),
        ("6", 12, 2, lambda:calculator_io_operations('6'), 1,"#003366","#e0ffff"),
        ("7", 11, 0, lambda:calculator_io_operations('7'), 1,"#003366","#e0ffff"),
        ("8", 11, 1, lambda:calculator_io_operations('8'), 1,"#003366","#e0ffff"),
        ("9", 11, 2, lambda:calculator_io_operations('9'), 1,"#003366","#e0ffff"),
        ("+", 11, 3, lambda:calculator_io_operations('+'), 1,"#003366","#e0ffff"),
        ("-", 12, 3, lambda:calculator_io_operations('-'), 1,"#003366","#e0ffff"),
        ("*", 13, 3, lambda:calculator_io_operations('*'), 1,"#003366","#e0ffff"),
        ("/", 14, 3, lambda:calculator_io_operations('/'), 1,"#003366","#e0ffff"),
        ("(", 11, 4, lambda:calculator_io_operations('('), 1, "#003366", "#e0ffff"),
        (")", 12, 4, lambda:calculator_io_operations(')'), 1, "#003366", "#e0ffff"),
        ("^", 13, 4, lambda:calculator_io_operations('^'), 1, "#003366", "#e0ffff"),
        ("%", 14, 4, lambda:calculator_io_operations('%'), 1, "#003366", "#e0ffff"),
        ("<", 10, 3, "#", 1, "#FFB74D", "#C62828"),
        (">", 10, 4, "#", 1, "#FFB74D", "#C62828"),
        ("sin(", 10, 7, lambda:calculator_io_operations('sin('), 1, "#003366", "#e0ffff"),
        ("cos(", 10, 8, lambda:calculator_io_operations('cos('), 1, "#003366", "#e0ffff"),
        ("tan(", 10, 9, lambda:calculator_io_operations('tan('), 1, "#003366", "#e0ffff"),
        ("sin⁻¹(", 11, 7, lambda:calculator_io_operations('sin⁻¹('), 1, "#003366", "#e0ffff"),
        ("cos⁻¹(", 11, 8, lambda:calculator_io_operations('cos⁻¹('), 1, "#003366", "#e0ffff"),
        ("tan⁻¹(", 11, 9, lambda:calculator_io_operations('tan⁻¹('), 1, "#003366", "#e0ffff"),
        ("h", 12, 6, "#", 1, "#FFB74D", "#C62828"), #this is where the constants start
        ("G", 12, 7, "#", 1, "#FFB74D", "#C62828"),
        ("e", 12, 8, "#", 1, "#FFB74D", "#C62828"),
        ("Nₐ", 12, 9, "#", 1, "#FFB74D", "#C62828"),
        ]
    
    for ex_text, ex_row, ex_col, ex_command, ex_columnspan, ex_bg, ex_fg in physics_calculator_definitions:
        button_creation(ex_text, ex_row, ex_col, ex_command, ex_columnspan, ex_bg, ex_fg)
    
    #Physics Constants
    
    #Physics Constants Display
    
    #SI Units
    si_units_state = BooleanVar()
    
    calculator_physics_si_units = Checkbutton(text="SI Units", variable= si_units_state, onvalue=1, offvalue=0, command=lambda:si_units(si_units_state), font=(14), bg='#51A7FC', fg='black')
    calculator_physics_si_units.grid_configure(row=22,column=7,columnspan=3,rowspan=1,sticky=NSEW)

#Handles the logic when the SI units button is pressed in the physics calculator
def si_units(si_units_state):
    if si_units_state.get() == 1:
        main_window.geometry("800x600")
        si_unit_label = [
            ("Length - meter (m)", 3, 11, 3, "#e6e6e6", "#2B2828",W),
            ("Time - seconds (s)", 4, 11, 3, "#e6e6e6", "#2B2828",W),
            ("Amount of Substance - mole (mol)", 5, 11, 3, "#e6e6e6", "#2B2828",W),
            ("Electric current - Ampere (A)", 6, 11, 3, "#e6e6e6", "#2B2828",W),
            ("Temperature - kelvin (K)", 7, 11, 3, "#e6e6e6", "#2B2828",W),
            ("Luminous intensity - candela (cd)", 8, 11, 3, "#e6e6e6", "#2B2828",W),
            ("Mass - kilogram (kg)", 9, 11, 3, "#e6e6e6", "#2B2828",W),
            ("Common Prefixes", 11, 11, 3, "#e6e6e6", "#2B2828",W),
            ("giga- (G) - 10⁹", 12, 11, 3, "#e6e6e6", "#2B2828",W),
            ("mega- (M) - 10⁶", 13, 11, 3, "#e6e6e6", "#2B2828",W),
            ("kilo- (k) - 10³", 14, 11, 3, "#e6e6e6", "#2B2828",W),
            ("deca- (D) - 10¹", 15, 11, 3, "#e6e6e6", "#2B2828",W),
            ("deci- (d) - 10⁻¹", 16, 11, 3, "#e6e6e6", "#2B2828",W),
            ("centi- (c) - 10⁻²", 17, 11, 3, "#e6e6e6", "#2B2828",W),
            ("milli- (m) - 10⁻³", 18, 11, 3, "#e6e6e6", "#2B2828",W),
            ("micro- (µ) - 10⁻⁶", 19, 11, 3, "#e6e6e6", "#2B2828",W),
            ("nano- (n) - 10⁻⁹", 20, 11, 3, "#e6e6e6", "#2B2828",W),
            ("pico- (p) - 10⁻¹²", 21, 11, 3, "#e6e6e6", "#2B2828",W)
            ]
        
        for lex_text, lex_row, lex_column, lex_columnspan, lex_bg, lex_fg, lex_sticky in si_unit_label:
            label_creation(lex_text, lex_row, lex_column, lex_columnspan, lex_bg, lex_fg, lex_sticky)
    
    else:
        main_window.geometry("540x600")
        calculator_physics()

#The constant page, containing constants - TBU - Colors change needed
def constants_values():
    clear_widgets()
    main_window.geometry("1000x600")
    #[text, row, column, columnspan, bg, fg and sticky]
    #bg='#e6e6e6', fg="#2B2828"
    const_maths_vals = [
        ("Maths Constants:", 2, 0, 6, "#e6e6e6", "#2B2828", W),
        ("Eulers Constant (\"e\"): 2.7182818284", 4, 0, 6, "#e6e6e6", "#2B2828", W),
        ("Eulers Constant (\"γ\"): 0.577215664901532", 5, 0, 6, "#e6e6e6", "#2B2828", W),
        ("Pi (\"π\"): 3.141592654", 6, 0, 6, "#e6e6e6", "#2B2828", W),
        ("Golden Ratio (\"φ\"): 1.6180339887498948482", 7, 0, 6, "#e6e6e6", "#2B2828", W),
        ("imaginary unit (\"i\"): √-1", 8, 0, 6, "#e6e6e6", "#2B2828", W),
        ("Khinchin’s constant (\"K\"): 2.6854520010", 9, 0, 6, "#e6e6e6", "#2B2828", W),
        ("Maths Constants:", 2, 0, 6, "#e6e6e6", "#2B2828", W),
        ]
    
    const_physics_vals = [
        ("Physics Constants:", 2, 8, 6, "#e6e6e6", "#2B2828", W),
        ("Newtonian constant of gravitation (\"G\"): 6.67430 x 10⁻¹¹ m³ kg⁻¹ s⁻²", 4, 8, 6, "#e6e6e6", "#2B2828", W),
        ("Newtonian constant of gravitation (\"G\"): 6.67430 x 10⁻¹¹ m³ kg⁻¹ s⁻²", 5, 8, 6, "#e6e6e6", "#2B2828", W),
        ("Avogadro constant (\" Nₐ\"): 6.02214076 x 1023 mol⁻¹", 6, 8, 6, "#e6e6e6", "#2B2828", W),
        ]

    for lex_text, lex_row, lex_column, lex_columnspan, lex_bg, lex_fg, lex_sticky in const_maths_vals:
        label_creation(lex_text, lex_row, lex_column, lex_columnspan, lex_bg, lex_fg, lex_sticky)

    for lex_text, lex_row, lex_column, lex_columnspan, lex_bg, lex_fg, lex_sticky in const_physics_vals:
        label_creation(lex_text, lex_row, lex_column, lex_columnspan, lex_bg, lex_fg, lex_sticky)
        
main_buttons()
home_screen()

#execute
main_window.mainloop()
