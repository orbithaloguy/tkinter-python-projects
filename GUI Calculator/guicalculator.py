import tkinter as tk

main = None
display_text = ''
display = None
str_expression = ''
past_number = ''
display_operator = ''
operator_label = None

def display_action(btn_pressed):
    global display_text, str_expression, past_number, display_operator, operator_label
    symbols = ['*', '+', '-', '=', '%', '/']

    try:
        if btn_pressed in symbols and btn_pressed != "=":
            if display_text:
                past_number = display_text
                display_operator = btn_pressed
                display_text = ''
                str_expression = ''
            else:
                display_operator = ''
            operator_label.config(text=display_operator)

        elif btn_pressed == "=":
            if past_number and display_operator and display_text:
                expression = f"{past_number}{display_operator}{display_text}"
                display_text = str(eval(expression))
                past_number = ''
                display_operator = ''
                str_expression = ''
                operator_label.config(text=display_operator)
            else:
                display_text = 'ERROR'

        else:
            display_text += btn_pressed
            str_expression += btn_pressed

        display.config(text=display_text)
    except Exception as e:
        display_text = "ERROR"
        display_operator = ''
        str_expression = ''
        past_number = ''
        operator_label.config(text=display_operator)
        display.config(text=display_text)

def gui(main):
    global display_text, display, display_operator, operator_label

    display_frame = tk.Frame(main, bg='light gray', width=24, height=2)
    display_frame.pack(padx=10, pady=20, fill='x')

    operator_label = tk.Label(display_frame, text=display_operator, font=('Arial', 24), anchor='w', width=2, bg='light gray', fg='gray')
    operator_label.pack(side='left')

    display = tk.Label(display_frame, text=display_text, font=('Arial', 24), anchor='e', bg='light gray')
    display.pack(side='right', fill='x', expand=True)

    buttonframe = tk.Frame(main)
    buttonframe.columnconfigure(0, weight=2)
    buttonframe.columnconfigure(1, weight=2)
    buttonframe.columnconfigure(2, weight=2)
    buttonframe.columnconfigure(3, weight=1)

    btn1 = tk.Button(buttonframe, text="7", font=('Arial', 18), command=lambda: display_action("7"))
    btn1.grid(row=0, column=0, sticky='news')

    btn2 = tk.Button(buttonframe, text="8", font=('Arial', 18), command=lambda: display_action("8"))
    btn2.grid(row=0, column=1, sticky='news')

    btn3 = tk.Button(buttonframe, text="9", font=('Arial', 18), command=lambda: display_action("9"))
    btn3.grid(row=0, column=2, sticky='news')

    btn4 = tk.Button(buttonframe, text="x", font=('Arial', 18), command=lambda: display_action("*"))
    btn4.grid(row=0, column=3, sticky='news')

    btn5 = tk.Button(buttonframe, text="4", font=('Arial', 18), command=lambda: display_action("4"))
    btn5.grid(row=1, column=0, sticky='news')

    btn6 = tk.Button(buttonframe, text="5", font=('Arial', 18), command=lambda: display_action("5"))
    btn6.grid(row=1, column=1, sticky='news')

    btn7 = tk.Button(buttonframe, text="6", font=('Arial', 18), command=lambda: display_action("6"))
    btn7.grid(row=1, column=2, sticky='news')

    btn8 = tk.Button(buttonframe, text="+", font=('Arial', 18), command=lambda: display_action("+"))
    btn8.grid(row=1, column=3, sticky='news')

    btn9 = tk.Button(buttonframe, text="1", font=('Arial', 18), command=lambda: display_action("1"))
    btn9.grid(row=2, column=0, sticky='news')

    btn10 = tk.Button(buttonframe, text="2", font=('Arial', 18), command=lambda: display_action("2"))
    btn10.grid(row=2, column=1, sticky='news')

    btn11 = tk.Button(buttonframe, text="3", font=('Arial', 18), command=lambda: display_action("3"))
    btn11.grid(row=2, column=2, sticky='news')

    btn12 = tk.Button(buttonframe, text="-", font=('Arial', 18), command=lambda: display_action("-"))
    btn12.grid(row=2, column=3, sticky='news')

    btn13 = tk.Button(buttonframe, text="/", font=('Arial', 18), command=lambda: display_action("/"))
    btn13.grid(row=3, column=0, sticky='news')

    btn14 = tk.Button(buttonframe, text="0", font=('Arial', 18), command=lambda: display_action("0"))
    btn14.grid(row=3, column=1, sticky='news')

    btn15 = tk.Button(buttonframe, text="%", font=('Arial', 18), command=lambda: display_action("%"))
    btn15.grid(row=3, column=2, sticky='news')

    btn16 = tk.Button(buttonframe, text="=", font=('Arial', 18), command=lambda: display_action("="))
    btn16.grid(row=3, column=3, sticky='news')

    buttonframe.pack(fill='x', padx=10)

def draw_main():
    global main
    main = tk.Tk()

    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    width = 400
    height = 300
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    main.resizable(False, False)
    main.title('Calculator')
    main.geometry(f'{width}x{height}+{x}+{y}')

    gui(main)
    main.mainloop()

def run_main():
    draw_main()

if __name__ == '__main__':
    run_main()