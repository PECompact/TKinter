import tkinter as tk
class Application:
    def __init__(self):
        self.root = tk.tk()
        self.root.title("练习")
        self.root.geomrtry("魏宇轩最帅")
        self.createWidefet()
    def createWidefet(self):
        self.value = tk.StringVar()
        self.value.set("text")
        self.entry = tk.Entry(self.root,textvariable=self.v)
        self.entry.pack()
        '''self.label = tk.Label(self.root,text = "魏宇轩",width=8,height = 4,font=("宋体",16))
        self.label.pack()#布局方式


        self.btn = tk.Button(self.root,text="确认",command=self.print)
        global photo
        photo = tk.PhotoImage(file=".gif")
        self.label_02 = tk.Label(self.root, image=photo)'''
        self.btn = tk.Button(self.root,text = "确认",command=self.print)
        self.btn.pack()
    def print(self):
        tk.Messagebox.showinfo("回应",self.value.get())

    def run(self):
        self.root.mainloop()
app = Application()
app.run()