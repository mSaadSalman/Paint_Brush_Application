from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog  
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import PIL
from tkinter import messagebox 

root = Tk() #this is a window (sort of class)
root.title('Paint Program')
root.geometry("800x800")

brush_colour= "black"
def paint(event):
	#brush parameters
	brush_width = '%0.0f'% float (my_slider.get())
		#brush type: BUTT, ROUND, PROJECTING
	brush_type2 = brush_type.get()

	#start pos
	x1=event.x-1 
	y1=event.y-1

	#end pos
	x2= event.x +1
	y2= event.y+1

	#now drawing on canvas
	my_canvas.create_line(x1, y1, x2, y2, fill=brush_colour, width=brush_width, capstyle=brush_type2, smooth=True)

#change size of brush
def change_brush_size(event): #created a brush size function here cause slider ttk function requires command of function
	slider_label.config(text='%0.0f'% float (my_slider.get())) #config updates the label by using my_slider value to display

#change brush colour
def change_brush_colour():
	global brush_colour #used variable globally
	brush_colour= "black"
	brush_colour = colorchooser.askcolor(color=brush_colour)[1] #color chooser syntax, where request 
	#first item in list for colour number(weird jus memoirze)
	
#change canvas colour
def change_canvas_colour():
	global bg_colour #used variable globally
	bg_colour= "black"
	bg_colour = colorchooser.askcolor(color=bg_colour)[1] #color chooser syntax, where request 
	#first item in list for colour number(weird jus memoirze)
	my_canvas.config(bg=bg_colour)

def clear_screen():
	my_canvas.delete(ALL)
	my_canvas.config(bg="white")

#save image
def save_as_png():
	result = filedialog.asksaveasfilename(initialdir="c:/paint",filetypes=(("png files", "*.png"),("all files","*.*")))
	

	if result.endswith('.png'):
		pass
	else:
		result = result + '.png' 

	if result:
		x=root.winfo_rootx()+my_canvas.winfo_x()
		y=root.winfo_rooty()+my_canvas.winfo_y()
		x1=x+my_canvas.winfo_width()
		y1=y+my_canvas.winfo_height()
		ImageGrab.grab().crop((x,y,x1,y1)).save(result)

		# Pop up success message
		messagebox.showinfo("Image Saved","Your image has been saved!")
		


#create canvas size
w=600
h=400

my_canvas = Canvas(root,width=w, height=h, bg="white")
my_canvas.pack(pady=20)

my_canvas.bind('<B1-Motion>', paint)

#Create brush options frame
brush_options_frame = Frame(root)
brush_options_frame.pack (pady=20)

#brush size
brush_size_frame= LabelFrame(brush_options_frame, text="Brush Size")
brush_size_frame.grid(row=0, column=0,padx=50)

#brush slider
my_slider = ttk.Scale(brush_size_frame,from_=1, to=100, command=change_brush_size,orient=VERTICAL,value=10)
my_slider.pack(pady=10,padx=10)

#brush slider label
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)

#brush type
brush_type_frame = LabelFrame(brush_options_frame, text="Brush Type",height=400)
brush_type_frame.grid(row=0,column=1,padx=50)


brush_type= StringVar()
brush_type.set("round")

#creating Radio Buttons for Brush type
brush_type_radio1= Radiobutton(brush_type_frame, text="Round",variable=brush_type, value="round")
brush_type_radio2=Radiobutton(brush_type_frame, text="Slash",variable=brush_type, value="butt")
brush_type_radio3=Radiobutton(brush_type_frame, text="Diamond",variable=brush_type, value="projecting")

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

#change colours
change_colours_frame = LabelFrame(brush_options_frame,text="Change Colours")
change_colours_frame.grid(row=0, column=2) 

#change brush color button 
brush_colour_button = Button(change_colours_frame,text="Brush Colour", command=change_brush_colour)
brush_colour_button.pack(pady=10,padx=10)

#change canvas background colour
canvas_colour_button = Button(change_colours_frame,text="Canvas Colour", command=change_canvas_colour)
canvas_colour_button.pack(pady=10,padx=10)

#program options frame
options_frame= LabelFrame(brush_options_frame, text="Program Options")
options_frame.grid(row=0,column=3,padx=50)

#clear screen button
clear_button= Button(options_frame, text="Clear Screen",command=clear_screen)
clear_button.pack(padx=10,pady=10)

#save image
save_image_button=Button(options_frame, text="Save to PNG",command=save_as_png)
save_image_button.pack(padx=10,pady=10)


root.mainloop()