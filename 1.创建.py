import tkinter as t
from tkinter import messagebox

class Application:
    def __init__(self):
        self.root=t.Tk()
        self.root.title("练习")
        self.root.geometry("魏宇轩最帅")
        self.createWidget()

    def run(self):
        self.root.mainloop()
    def createWidget(self):
        self.label = t.Label(self.root,text="标签")
        self.label.pack()
        self.button = t.Button(self.root,text="按钮",command=hello)
        self.button.pack()
        self.entry = t.Entry(self.root)
        self.entry.pack()
    def run(self):
        self.root.mainloop()
app =Application()
app.run()
'''
def hello():
    t.messagebox.showinfo("响应","hello")
label = t.Label(root,text="标签")
label.pack()
button = t.Button(root,text="按钮",command=hello)
button.pack()
entry = t.Entry(root)
entry.pack()

root.mainloop()'''