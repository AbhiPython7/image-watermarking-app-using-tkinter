from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk,ImageDraw,ImageFont
def open_files():
    window.filename=filedialog.askopenfilename(initialdir="/c",title="Add File")
    global filename
    filename=window.filename
    # photo=ImageTk.PhotoImage(Image.open(window.filename))
    # label_image=Label(image=photo).place(x=100,y=100)
def edit_image():

    image=Image.open(filename)
    width,height=image.size
    print(width,height)
    font = ImageFont.truetype("arial.ttf", 50)

    draw=ImageDraw.Draw(image)
    y=height-66
    draw.text((190,y),text="watermarker",font=font,fill=(255, 255, 255, 128))
    image.save("modified.png")

def display_image():
    photo =PhotoImage(file="modified.png")
    canvas=Canvas(width=800,height=1000)
    canvas.create_image(200,250,image=photo)
    canvas.place(x=0,y=0)
    window.mainloop()


window=Tk()
window.title("Watermarking any image")
window.minsize(width=400,height=400)

button=Button(text="Add file",command=open_files)
button.place(x=170,y=110)
button2=Button(text="Add watermark to image",command=edit_image).place(x=120,y=150)
button_display=Button(text="display image",command=display_image).place(x=140,y=190)

window.mainloop()








