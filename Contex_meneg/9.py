import time
import tkinter as tk
from tkinter import ttk

class Progress:
    def __enter__(self):
        self.root = tk.Tk()
        self.root.title("Progress")
        
        self.progress = ttk.Progressbar(self.root, length=300, mode='indeterminate')
        self.progress.pack(pady=20)
        
        self.label = tk.Label(self.root, text="Working...")
        self.label.pack()
        
        self.root.update()
        self.progress.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.progress.stop()
        self.label.config(text="Done!")
        self.root.update()
        time.sleep(1)
        self.root.destroy()


with Progress():
    time.sleep(3)