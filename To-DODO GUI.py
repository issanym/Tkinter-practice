from tkinter import *

root = Tk()
root.title("To-DODO")
root.config(background="#CAABE3")

list_item = []

def add_item():

	while True:

		item_get = text_field.get()

		def add_itempara(): 
			list_item.append(item_get)
			list_display="\n".join(list_item)
			item = Label(root, text=list_display, bg="#CAABE3", font=("informal", 10))
			r_p = 4
			while r_p <30:
				item.grid(row=r_p, column=2)
				r_p += 1
			
		add_itempara()
		text_field.delete(0, END)
		#def del_item():

		break

#Defining widget
top_label = Label(root, text="To-DODO", bg="#251745", fg="#E8F7F7", font=("informal", 35), padx=76)
text_field = Entry(root, font=("informal", 15), borderwidth=0)
add_button = Button(root,text="+", borderwidth=0, command=add_item)

#===================================================================================================

space_1 = Label(root, text="", bg="#CAABE3")
space_2 = Label(root, text="", bg="#CAABE3", width=4)
space_3 = Label(root, text="", bg="#CAABE3", width=4)
space_4 = Label(root, text="", bg="#CAABE3")

#Placing widget
top_label.grid(row=0, column=0, columnspan=5)
text_field.grid(row=2, column=1, columnspan=2)
add_button.grid(row=2, column=3)

#================================================
space_1.grid(row=1, column=0, columnspan=5)
space_2.grid(row=2, column=0)
space_3.grid(row=2, column=4)
space_4.grid(row=3, column=0, columnspan=5)


root.mainloop()