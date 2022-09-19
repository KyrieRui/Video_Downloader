## Video Downloader
### Author: Ray
### Date: 20/09/2022
### Refrence: https://www.bilibili.com/video/BV1rg411D7Vb?vd_source=9fa62e123b591fe30734493ac73e11b1


This is a simple video downloader that uses youtube-dl to download videos from youtube and other sites.

![outlook](/Users/zwang/Desktop/OffSchool/python_offschool/vedioDownloader/outlook.png)
![Screenshot](/Users/zwang/Desktop/OffSchool/python_offschool/vedioDownloader/downloading.png)
![Screenshot](/Users/zwang/Desktop/OffSchool/python_offschool/vedioDownloader/Kapture 2022-09-20 at 10.59.36.gif)

## Pakages:
### 1. you-get
```bash
pip install you-get
```
To use you-get just open a terminal on the folder where you want to download the video and type:
```bash
you-get [url]
```
 
### 2. py2app 
#### (optional, for mac users. I used this package for to make standalone application bundles and plugins from Python scripts)
```bash
pip install py2app
```

### 3. tkinter
```bash
pip install tkinter
```

## Program:

### import tinker, to give a GUI to the program
```python
root = tk.Tk()
root.title("Vedoi Downloader")  ## UI_Name
root.geometry("550x100+400+150") ## UI_Size and UI_Position
```

### Set the basic Button and Text Input Box layout of the program
```python
## Text
txt = tk.Label(root, text="Vedio URL: ", font=("Arial", 20))
txt.grid(row=1, column=0)
## Input Box
entry = tk.Entry(root, textvariable=key_url)
entry.grid(row=1, column=1)
## Download Button
bt = tk.Button(root, text="Download", command=download)
bt.grid(row=1, column=2)
```

### def the Download function
```python
def download():
    link = f'you-get -o vedio {key_url.get()}' ## you-get -o vedio is the download path
    print("Download Clicked")
    subprocess.run(link, shell=True)
```

## Summary:
### The download speed is quite slow, but it works. I will try to improve it in the future.
### If you wana have a try plz choice the short vedio, otherwise it will take a long time to download.

## For MAC users:
### You can use py2app to make a standalone application bundle from the python script.
### use in terminal:
```bash
py2applet --make-setup main.py 
python setup.py py2app -A
```


