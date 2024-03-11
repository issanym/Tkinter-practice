from tkinter import *
from tkinter import messagebox


def crossing():

    parent_1=entry1.get()
    parent_2=entry2.get()

    #=================================================================================
    genotype1_1=parent_1[0].upper()+parent_1[1].lower()
    genotype2_1=parent_2[0].lower()+parent_2[1].upper()
    #=================================================================================
    genotype1_2=parent_1[0].lower()+parent_1[1].upper()
    genotype2_2=parent_2[0].upper()+parent_2[1].lower()
    #=================================================================================



    if parent_1 == parent_1.upper(): 
        if parent_2 == parent_2.upper():
            messagebox.showinfo(title="Monohybrid cross", message="All the children will be homozygous Dominant")
            print("All the children will be homozygous Dominant")
        elif parent_2 == parent_2.lower():
            messagebox.showinfo(title="Monohybrid cross", message="All the children will be heterozygous")
            print("All the children will be heterozygous")
        else:
            messagebox.showinfo(title="Monohybrid cross", message="50% of the children will be heterozygous and 50% will be homozygous Ressecive")
            print("50% of the children will be heterozygous and 50% will be homozygous Ressecive")

    elif parent_1 == parent_1.lower():
        if parent_2 == parent_2.lower():
            messagebox.showinfo(title="Monohybrid cross", message="All the children will be homozygous Ressecive")
            print("All the children will be homozygous Ressecive")
        elif parent_2 == parent_2.upper():
            messagebox.showinfo(title="Monohybrid cross", message="All the children will be heterozygous")
            print("All the children will be heterozygous")
        else:
            messagebox.showinfo(title="Monohybrid cross", message="50% of the children will be heterozygous and 50% will be homozygous Ressecive")
            print("50% of the children will be heterozygous and 50% will be homozygous Ressecive")

    elif genotype1_1 == parent_1:
        if parent_2 == parent_2.upper():
            messagebox.showinfo(title="Monohybrid cross", message="50% of the children will be heterozygous and 50% will be homozygous Dominant")
            print("50% of the children will be heterozygous and 50% will be homozygous Dominant")
        elif parent_2 == parent_2.lower():
            messagebox.showinfo(title="Monohybrid cross", message="50% of the children will be heterozygous and 50% will be homozygous Ressecive")
            print("50% of the children will be heterozygous and 50% will be homozygous Ressecive")
        else:
            messagebox.showinfo(title="Monohybrid cross", message="50% of the children will be heterozygous, 25% will hetrozygous dominat and 25% will heterozygous ressecive")
            print("50% of the children will be heterozygous, 25% will hetrozygous dominant and 25% will heterozygous ressecive")

    elif parent_1 == genotype1_2: 
        if parent_2 == parent_2.upper():
            messagebox.showinfo(title="Monohybrid cross", message="50% of the children will be heterozygous and 50% will be homozygous Dominant")
            print("50% of the children will be heterozygous and 50% will be homozygous Dominant")
        elif parent_2 == parent_2.lower():
            messagebox.showinfo(title="Monohybrid cross", message="50% of the children will be heterozygous and 50% will be homozygous Ressecive")
            print("50% of the children will be heterozygous and 50% will be homozygous Ressecive")
        else:
            messagebox.showinfo(title="Monohybrid cross", message="50% of the children will be heterozygous, 25% will hetrozygous dominant and 25% will heterozygous ressecive")
            print("50% of the children will be heterozygous, 25% will hetrozygous dominat and 25% will heterozygous ressecive")



window = Tk()
####
window.geometry("500x500")
####
window.title("Monohybrid cross")
####
window.config(background = "#D1C6F3")
###################################

label = Label(window, text = "Monohybrid cross", bg = "#D1C6F3", font = ("Arial", 35, "bold", "italic"), fg = "black")
label.pack(pady=25)
##################################
label2 = Label(window, text = "Mother's genotype:", bg = "#D1C6F3", font = ("Arial", 10, "bold", "italic"), fg = "black")
label2.pack(pady=20)
##
entry1 = Entry(window, font = ("Arial", 15))
entry1.pack(pady=15)
######
label3 = Label(window, text = "Father's genotype:", bg = "#D1C6F3", font = ("Arial", 10, "bold", "italic"), fg = "black")
label3.pack(pady=20)
##
entry2 = Entry(window, font = ("Arial", 15))
entry2.pack(pady = 15)
##################################

button = Button(window, text = "Cross", bg = "white", font = ("Arial", 20), fg = "black", command = crossing)
button.pack(pady = 30)

window.mainloop()
