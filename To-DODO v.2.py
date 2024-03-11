from tkinter import *

root = Tk()
root.title("To-DODO V.2")
root.config(background="#CAABE3")
root.geometry("750x600")

 
list_item = list()

def add_item():

	while True:

		item_get = text_field.get()

		def add_itempara(): 
			list_item.append(item_get)
			new_list = [x for x in list_item if x != '']
			list_display="\n".join(new_list)
			item = Label(frame_2, text=list_display, bg="#CAABE3", font=("informal", 13))
			r_p = 0
			while r_p <30:
				item.grid(row=r_p, column=1)
				r_p += 1
			
		add_itempara()
		text_field.delete(0, END)
		#def del_item():

		break

def del_item():
	list_item.pop(0)
	list_display="\n".join(list_item)
	item = Label(frame_2, text=list_display, bg="#CAABE3", font=("informal", 13))
	r_p = 0
	while r_p <30:
		item.grid(row=r_p, column=1)
		r_p += 1
	print(list_item)


# defining items
top_label = Label(root, text="To-DODO", bg="#251745", fg="#E8F7F7", font=("informal", 35), padx=265)
frame_1 = LabelFrame(root, padx=25, pady=15, bg="#CAABE3", borderwidth=0)
text_field = Entry(frame_1, font=("informal", 18), borderwidth=0)
lbl = Label(frame_1, text="Type your ToDo", font=(15), fg="#E8F7F7", bg="#251745", pady=15)
button_1= Button(frame_1, text="Add item", fg="#E8F7F7", bg="#251745", pady=20, padx=21, command=add_item)
button_2= Button(frame_1, text="Delete item", fg="#E8F7F7", bg="#251745", pady=20, command=del_item)

# ==========================================================================
frame_2 = LabelFrame(root,  padx=25, pady=15, bg="#CAABE3", borderwidth=0)


# Placing items
top_label.grid(row=0, column=0, columnspan=5)
frame_1.grid(row=1, column=0, sticky=W)
lbl.grid(row=2, column=0)
text_field.grid(row=3, column=0, pady=40)
button_1.grid(row=4, column=0, pady=68)
button_2.grid(row=5, column=0, pady=40)
# =============================================================================
frame_2.grid(row=1, column=1,sticky=E)


root.mainloop()