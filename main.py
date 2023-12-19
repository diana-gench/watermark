from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
# ---------------------------- CONSTANTS ------------------------------- #
LIGHT_PURPLE = "#A367B1"
PURPLE = "#5D3587"
DARK_PURPLE = "#392467"
LIGHT_PINK = "#FFD1E3"
FONT_NAME = "Courier"
WATERMARK_FONT = "arial.ttf"
# ---------------------------- CHANGE PICTURE ------------------------------- #
def update_image(new_image):
   canvas.itemconfig(images,image=new_image)

# ---------------------------- START PROGRAMM ------------------------------- #
def start_program():
    start_button.config(state=DISABLED)  # Disable the button after clicking
    canvas.itemconfig(title_text, text="")
    update_image(new_image=icon_image)  # Change the image

    upload_button.grid(column=1, row=2)  # Consider placing widgets only once
    title_label = Label(text="Add Your Watermark!", fg=DARK_PURPLE, bg=LIGHT_PURPLE, font=(FONT_NAME, 40, "bold"))
    title_label.grid(column=1, row=0)


# ---------------------------- UPLOADING IMAGE ------------------------------- #
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        add_watermark(file_path)

# ---------------------------- ADDING THE WATERMARK ------------------------------- #
def add_watermark(image_path):
    watermark_text = "Your Watermark Here!"
    original_image = Image.open(image_path)
    width, height = original_image.size
    base = original_image.copy()
    
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    fnt = ImageFont.truetype(WATERMARK_FONT, 40)
    
    d = ImageDraw.Draw(txt)

    d.text((100, 100), watermark_text, font=fnt, fill=(255, 255, 255, 128))

    base = base.convert("RGBA")
    txt = txt.convert("RGBA")
    
    watermarked_img = Image.alpha_composite(base, txt)

    watermarked_img.show()
    watermarked_img.save("watermarked.png")

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        watermarked_img.save(save_path)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("WATERMARK")
window.config(padx=50, pady=50, bg=LIGHT_PURPLE)

canvas = Canvas(window, width=400, height=300, bg=LIGHT_PURPLE, highlightthickness=0)


image1 = (Image.open("welcome.png"))
image2 = (Image.open("icon.png"))

welcome_resized = image1.resize((400, 280), resample=Image.Resampling.BILINEAR)
welcome_image = ImageTk.PhotoImage(welcome_resized)

icon_resized = image2.resize((300, 200), resample=Image.Resampling.BILINEAR)
icon_image = ImageTk.PhotoImage(icon_resized)

images = canvas.create_image(200, 150, anchor=CENTER, image=welcome_image)
title_text = canvas.create_text(200, 150, text="Welcome!", fill = DARK_PURPLE, font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)





start_button = Button(
    text="START",
    command=start_program,
    font=("Roboto", 18),
    fg=DARK_PURPLE,
    bg=LIGHT_PINK,
    relief=RIDGE
)

start_button.grid(column=1, row=2)

upload_button = Button(
    text="Upload Image",
    command=open_file_dialog,
    font=("Roboto", 18),  
    fg=DARK_PURPLE,            
    bg=LIGHT_PINK,                        
    relief=RIDGE        
)


window.mainloop()
