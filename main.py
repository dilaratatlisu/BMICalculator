from tkinter import *

my_tkinter = Tk()
my_tkinter.title("BMI Calculator")
my_tkinter.config(background="light blue")
my_tkinter.wm_minsize(width=280, height=280)

my_label = Label(text="***BMI Calculator***", font=("Arial", 15, "bold"), background="light blue", foreground="dark blue")
my_label.config(pady=10)
my_label.pack()

label_2 = Label(text="Enter weight: ", font=("Arial", 11, "normal"), background="light blue", pady=7)
label_2.pack()
entry_1 = Entry(my_tkinter)
entry_1.pack()

label_3 = Label(text="Enter height: ", font=("Arial", 11, "normal"), background="light blue", pady=7)
label_3.pack()
entry_2 = Entry(my_tkinter)
entry_2.pack()

result_label = Label(background="light blue", font=("Arial", 11, "bold"), pady=10)
result_label.pack()



def bmi_calculate():
    my_weight = entry_1.get()
    my_height = entry_2.get()
    if my_weight == "" or my_height == "":
        result_label.config(text="Enter your weight or your height!")
    else:
        try:
            bmi = float(my_weight) / ((float(my_height) / 100) ** 2)
            bmi_result(bmi)
        except:
            result_label.config("Enter a valid number!")



def bmi_result(bmi):
    if bmi <= 16:
        result_label.config(text="Severe Thinness")
    elif 16 < bmi <= 17:
        result_label.config(text="Moderate Thinness")
    elif 17 < bmi <= 18.5:
        result_label.config(text="Mild Thinness")
    elif 18.5 < bmi <= 25:
        result_label.config(text="Normal")
    elif 25 < bmi <= 30:
        result_label.config(text="Overweight")
    elif 30 < bmi <= 35:
        result_label.config(text="Obese Class I")
    elif 35 < bmi <= 40:
        result_label.config(text="Obese Class II")
    else:
        result_label.config(text="Obese Class III")




my_button = Button(my_tkinter, text="Calculate", command=bmi_calculate)
my_button.pack()

my_tkinter.mainloop()


