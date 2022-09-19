import tkinter as tk
import subprocess

root = tk.Tk()
root.title("Vedoi Downloader")
root.geometry("550x100+400+150")

def download():
    link = f'you-get -o vedio {key_url.get()}'
    print("Download Clicked")
    subprocess.run(link, shell=True)


def clear():
    entry.delete(0, 'end')
    print("Clear Clicked")

txt = tk.Label(root, text="Vedio URL: ", font=("Arial", 20))
txt.grid(row=1, column=0)

key_url = tk.StringVar()

entry = tk.Entry(root, textvariable=key_url)
entry.grid(row=1, column=1)


bt = tk.Button(root, text="Download", command=download)
bt.grid(row=1, column=2)

bt = tk.Button(root, text="Clear", command=clear)
bt.grid(row=1, column=3)
root.mainloop()
