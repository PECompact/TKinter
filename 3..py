import tkinter as tk
from tkinter import messagebox
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("标题")
        self.root.geometry("400x300+200+100")
        self.cr()
    def cr(self):
        self.v1=tk.StringVar()
        self.c1=tk.Checkbutton(self.root,text="学习",onvalue=1,offvalue=0,variable=self.v1)
        self.c1.pack()
        self.v2 = tk.StringVar()
        self.c2 = tk.Checkbutton(self.root, text="打游戏", onvalue=1, offvalue=0, variable=self.v2)
        self.c2.pack()
        self.btn = tk.Button(self.root, text="返回文本", command=self.printVale)
        self.btn.pack()
    def printVale(self):
        if self.v1.get()==1 and self.v2.get()==1:
            tk.messagebox.showinfo("确认框","你选择的是学习和打游戏")
        elif self.v1.get()==1 and self.v2.get()==0:
            tk.messagebox.showinfo("确认框","你选择的是学习")
        elif self.v1.get()==0 and self.v2.get()==1:
            tk.messagebox.showinfo("确认框","你选择的是打游戏")
        else:
            tk.messagebox.showinfo("确认框","你没有选择")
        '''self.text = tk.Text(self.root,width=20,height=5,fg="red",bg="blue")
        self.text.insert(1.0,"a\n12345")
        self.text.insert(2.2,"asonconidjsnijn")
        self.text.pack()
        self.btn = tk.Button(self.root, text="返回文本", command=return_text)
        self.btn.pack()
    def return_text(self):
        tk.messagebox.showinfo("换回文本",self.text.get(1.0,2.5))'''
    def run(self):
        self.root.mainloop()
app = App()
app.run()