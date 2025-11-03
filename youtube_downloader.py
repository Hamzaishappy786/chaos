import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Base working directory
WORKING_DIR = r"C:\Users\gamer"
DOWNLOAD_FOLDER = os.path.join(WORKING_DIR, r"dist\downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def download_video():
    url = entry.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Please enter a YouTube URL.")
        return

    try:
        # yt-dlp command
        command = f'yt-dlp "{url}" -o "{DOWNLOAD_FOLDER}/%(title)s.%(ext)s"'

        # Open CMD in the working directory and run yt-dlp
        subprocess.Popen(
            f'start cmd /k "cd /d {WORKING_DIR} && {command}"',
            shell=True
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI setup
root = tk.Tk()
root.title("YouTube Downloader Bot")
root.geometry("400x180")
root.resizable(False, False)

tk.Label(root, text="Enter YouTube Video URL:", font=("Segoe UI", 11)).pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Download", command=download_video, bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold")).pack(
    pady=15)

root.mainloop()