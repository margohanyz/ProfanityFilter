import tkinter as tk

class App(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.lift() # always on the top

        # WINDOW SIZE
        sheight, swidth = self.root.winfo_screenheight(), self.root.winfo_screenwidth()
        self.root.geometry('{}x{}'.format(swidth,sheight))

        # BUTTONS
        self.button1 = tk.Button(self.root, fg='red', text='button 1')
        self.button1.grid(row = 0, column = 0, sticky='NSEW')

        self.button2 = tk.Button(self.root, fg='blue', text='button 2')
        self.button2.grid(row = 0, column = 1, sticky='NSEW')

        self.button3 = tk.Button(self.root, fg='green', text='button 3')
        self.button3.grid(row = 0, column = 2, sticky='NSEW')

        # TEXT BLOCK
        self.infotext = tk.Text(self.root, height=1, width=3)
        self.infotext.insert(tk.INSERT, 'INFO')
        self.infotext.config(state='disabled')
        self.infotext.grid(row=0,column=6,sticky='NSEW')

        # CANVAS
        self.website = tk.Canvas(self.root, bg='black')
        self.website.grid(row=1,columnspan=6, sticky='NSEW')

        self.info = tk.Canvas(self.root, bg='white')
        self.info.grid(row=1, column=6, sticky='NSEW')

        # AUTORESIZE ELEMENTS
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.grid_columnconfigure(5, weight=1)
        self.root.grid_columnconfigure(6, weight=1)
        #self.root.grid_columnconfigure(3, weight=1)
        #self.root.grid_columnconfigure(4, weight=1)
        #self.root.grid_columnconfigure(5, weight=1)
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)

        self.root.mainloop()

if __name__ == '__main__':
    App()