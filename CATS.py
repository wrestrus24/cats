from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response= requests.get(url)
        response.raise_for_status()
        image_data= BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def open_new_window():
    img= load_image(url)
    if img:
        new_window=TopLevel()
        new_window.title("Picture CAT")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img

def exit():
    window.destroy()

window=Tk()
window.title("Cats!")
window.geometry("600x600")



url= "https://cataas.com/cat"
img= load_image(url)

if img:
    label.config(image=img)
    label.image=img
#update_button=Button(text="Обновить", command=set_image)
#update_button.pack()
menu_bar=Menu(window)
window.config(menu=menu_bar)

file_menu= Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Load Photo", command=open_new_window)
file_menu.add_command(label="Exit", command=exit)

set_image()

window.mainloop()
