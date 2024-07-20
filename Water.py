import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Application")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.watermark_text_entry = tk.Entry(root)
        self.watermark_text_entry.pack()

        self.add_watermark_button = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_button.pack()

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack()

        self.image = None
        self.watermarked_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def display_image(self, image):
        img = ImageTk.PhotoImage(image)
        self.image_label.config(image=img)
        self.image_label.image = img

    def add_watermark(self):
        if self.image:
            watermark_text = self.watermark_text_entry.get()
            self.watermarked_image = self.image.copy()
            draw = ImageDraw.Draw(self.watermarked_image)
            font = ImageFont.load_default()
            text_width, text_height = draw.textsize(watermark_text, font)
            width, height = self.watermarked_image.size
            x, y = width - text_width - 10, height - text_height - 10
            draw.text((x, y), watermark_text, font=font, fill="white")
            self.display_image(self.watermarked_image)

    def save_image(self):
        if self.watermarked_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                self.watermarked_image.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
