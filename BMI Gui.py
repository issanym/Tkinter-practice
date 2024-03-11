from tkinter import *
from tkinter import messagebox


def calculate():
    height = int(entry1.get())
    weight = int(entry2.get())
    bmi = (weight / height ** 2) * 10000
    result = "Your BMI is %02.2d" % (bmi)
    print(result)
    # print(f"Your BMI is...{bmi}" )
    if bmi < 18.5:
        messagebox.showinfo(title="BMI calculator", message=f"{result} --You are underweight")
        print("You are underweight")
    elif bmi <= 24.9:
        messagebox.showinfo(title="BMI calculator", message=f"{result} You are normal")
        print("You are normal")
    elif bmi <= 29.9:
        messagebox.showinfo(title="BMI calculator", message=f"{result} You are overweight")
        print("You are overweight")
    elif bmi <= 34.9:
        messagebox.showinfo(title="BMI calculator", message=f"{result} You are obese")
        print("You are obese")
    else:
        messagebox.showinfo(title="BMI calculator", message=f"{result} You are extremely obese")
        print("You are extremely obese")
    entry1.delete(0,END)
    entry2.delete(0,END)

window = Tk()
####
window.geometry("500x500")
####
window.title("BMI calculator")
####
window.config(background="#E9BCAC")
###################################

label = Label(window, text="BMI calculator", bg="#E9BCAC", font=("Arial", 35, "bold"), fg="black")
label.pack(pady=25)
##################################
label2 = Label(window, text="Enter your height in cm:", bg="#E9BCAC", font=("Arial", 10, "bold"), fg="black")
label2.pack(pady=20)
##
entry1 = Entry(window, font=("Arial", 15))
entry1.pack(pady=15)
######
label3 = Label(window, text="Enter your weight in kg:", bg="#E9BCAC", font=("Arial", 10, "bold"), fg="black")
label3.pack(pady=20)
##
entry2 = Entry(window, font=("Arial", 15))
entry2.pack(pady=15)
##################################

button = Button(window, text="Get your BMI", bg="white", font=("Arial", 20), fg="black", command=calculate)
button.pack(pady=30)

window.mainloop()
