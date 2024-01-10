import tkinter as tk
from tkinter import filedialog
import qrcode

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("QR Code Generator")

        self.label = tk.Label(master, text="Enter data:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=30)
        self.entry.pack(pady=10)

        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.save_button = tk.Button(master, text="Save QR Code", command=self.save_qr_code)
        self.save_button.pack(pady=10)

    def generate_qr_code(self):
        data = self.entry.get()
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            self.qr_image = qr.make_image(fill_color="black", back_color="white")
            self.qr_image.show()

    def save_qr_code(self):
        if hasattr(self, 'qr_image'):
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                self.qr_image.save(file_path)
                print(f"QR Code saved as {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
