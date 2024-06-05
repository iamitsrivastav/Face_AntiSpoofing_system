import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os
import signal

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Anti-Spoofing System")
        self.root.geometry("500x400")

        self.process = None  # Attribute to store the process

        # Load background image
        self.background_image = Image.open("background.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a canvas for the background image
        self.canvas = tk.Canvas(root, width=500, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        # Create a title label with custom font and color
        self.title_label = tk.Label(root, text="Face Anti-Spoofing System", font=("Comic Sans MS", 24, "bold"), bg='lightblue', fg='darkblue')
        self.title_label.place(relx=0.5, rely=0.2, anchor="center")

        # Create a label with custom font and color
        self.label = tk.Label(root, text="Click the button to run", font=("Comic Sans MS", 16), bg='lightgreen', fg='darkgreen')
        self.label.place(relx=0.5, rely=0.4, anchor="center")

        # Create a styled Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_script, font=("Comic Sans MS", 14, "bold"), bg='purple', fg='white', activebackground='darkorchid', activeforeground='white')
        self.start_button.place(relx=0.4, rely=0.6, anchor="center")

        # Create a styled Stop button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_script, font=("Comic Sans MS", 14, "bold"), bg='red', fg='white', activebackground='darkred', activeforeground='white')
        self.stop_button.place(relx=0.6, rely=0.6, anchor="center")

    def start_script(self):
        script_path = os.path.join(os.path.dirname(__file__), 'main.py')
        try:
            self.process = subprocess.Popen(['python', script_path])
            messagebox.showinfo("Success", "Started successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start: {e}")

    def stop_script(self):
        if self.process and self.process.poll() is None:  # Check if process is running
            self.process.terminate()
            self.process.wait()  # Wait for process to terminate
            messagebox.showinfo("Success", "Stopped successfully.")
        else:
            messagebox.showwarning("Warning", "No running process found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
