import ttkbootstrap as tb
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

class Main():
    def __init__(self, root):

        style = tb.Style()
        style.configure('TButton', font=('Franklin Gothic Bold', 12))

        self.count = 1
        self.count2 = 0
        self.root = root
        self.root.geometry("500x600")
        self.root.title("Graphilator")

        frm = tb.Frame(self.root)
        frm.pack()

        tb.Label(text="Graphilator", font=('Franklin Gothic Bold', 20)).pack(pady=20)

        nb = tb.Notebook(self.root, width=500, height=500)
        nb.pack(expand=True, padx=5, pady=10)

        frame = tb.Frame(nb, width=500, height=600)
        frame.grid(sticky="news")

        nb.add(frame, text="2D Function")

        self.entryFrame = tb.Frame(frame)
        self.entryFrame.grid(row=1, column=0)

        self.functions = tb.Entry(self.entryFrame)
        self.functions.grid(row=0, column=0, padx=5, pady=5)

        self.btnFrame = tb.Frame(frame)
        self.btnFrame.grid(row=0, column=0)

        self.addBtn = tb.Button(self.btnFrame, text="+", command=self.addFunction)
        self.addBtn.grid(row=2, column=1, pady=5, padx=10)

        btn = tb.Button(self.btnFrame, text="Show Graph", command=self.show)
        btn.grid(row=2, column=0, pady=5, padx=10) 

        self.rangeFrame = tb.Frame(self.btnFrame)
        self.rangeFrame.grid(row=2, column=2, pady=10, padx=(50, 10))

        self.rangeLabel = tb.Label(self.rangeFrame, text="Range (x) : ", font=("Franklin Gothic Bold", 12))
        self.rangeLabel.grid(row=0, column=0, padx=10)
        self.rangeX1 = tb.Entry(self.rangeFrame, width=5)
        self.rangeX2 = tb.Entry(self.rangeFrame, width=5)
        self.rangeX1.grid(row=0, column=1, padx=5)
        self.rangeX2.grid(row=0, column=2, padx=5)

        self.legendV = tb.IntVar()
        self.yFuncV = tb.IntVar()
        self.legend = tb.Checkbutton(self.btnFrame, text="Include Legend", style="primary.Roundtoggle.Toolbutton", onvalue=1, offvalue=0, variable=self.legendV)
        self.legend.grid()
        self.yFunc = tb.Checkbutton(self.btnFrame, text="f(y)", style="primary.Roundtoggle.Toolbutton", onvalue=1, offvalue=0, variable=self.yFuncV, command=self.changeRange)
        self.yFunc.grid(row=3, column=1)

        frame2 = tb.Frame(nb, width=500, height=600)
        frame2.grid(sticky="news")

        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------

        nb.add(frame2, text="3D Function")

        self.entryFrame2 = tb.Frame(frame2)
        self.entryFrame2.grid(row=1, column=0)

        self.btnFrame2 = tb.Frame(frame2)
        self.btnFrame2.grid(row=0, column=0)

        btn2 = tb.Button(self.btnFrame2, text="Show Graph", command=self.show3D)
        btn2.grid(row=0, column=0, pady=5, padx=(10,80)) 

        self.rangeFrame2 = tb.Frame(self.btnFrame2)
        self.rangeFrame2.grid(row=0, column=2, pady=10, padx=(35, 10))

        self.rangeLabel2 = tb.Label(self.rangeFrame2, text="Range : ", font=("Franklin Gothic Bold", 12))
        self.rangeLabel2.grid(row=0, column=0, padx=(30,10))
        self.rangeX12 = tb.Entry(self.rangeFrame2, width=5)
        self.rangeX22 = tb.Entry(self.rangeFrame2, width=5)
        self.rangeX12.grid(row=0, column=1, padx=5)
        self.rangeX22.grid(row=0, column=2, padx=5)

        self.toggleFrame = tb.Frame(self.btnFrame2)
        self.toggleFrame.grid(row=1, column=0, columnspan=2)

        self.wireframeV = tb.IntVar()
        self.wireframe = tb.Checkbutton(self.toggleFrame, text="Wireframe", style="primary.Roundtoggle.Toolbutton", onvalue=1, offvalue=0, variable=self.wireframeV, command=self.toggle1)
        self.wireframe.grid(padx=(10, 0), row=0, column=1)

        self.triangulationV = tb.IntVar()
        self.triangulation = tb.Checkbutton(self.toggleFrame, text="Triangulate", style="primary.Roundtoggle.Toolbutton", onvalue=1, offvalue=0, variable=self.triangulationV, command=self.toggle2)
        self.triangulation.grid(padx=(0), row=0, column=0)

        tb.Label(self.entryFrame2, text="Function", font=("Franklin Gothic Bold", 13)).grid(row=0, column=0, padx=(5), pady=5)
        self.function = tb.Entry(self.entryFrame2)
        self.function.grid(row=0, column=1, padx=5, pady=5)
        self.functionFormat = tb.Menubutton(self.entryFrame2, text='Function Formats', bootstyle='outline-primary')
        self.functionFormat.grid(row=0, column=2, padx=(65, 5), pady=5)
        self.options = tb.Menu(self.functionFormat)
        self.functionFormat['menu'] = self.options

        self.selectedVar = tb.IntVar()

        self.options.add_radiobutton(label="z = ax+by+c", value=0, variable=self.selectedVar)
        self.options.add_radiobutton(label="y = ax+bz+c", value=1, variable=self.selectedVar)
        self.options.add_radiobutton(label="x = az+by+c", value=2, variable=self.selectedVar)

        tb.Separator(frame2, bootstyle="primary").grid(row=2, column=0)
        
        self.styleFrame = tb.LabelFrame(frame2, text="Style")
        self.styleFrame.grid(row=3, column=0, pady=1, padx=(0,5), ipady=2)

        tb.Label(self.styleFrame, text="Theme", font=("Franklin Gothic", 12)).grid(row=0, column=0, padx=(15,15), pady=5)
        self.colorOpts = tb.Combobox(self.styleFrame, values=plt.colormaps(), width=15)
        self.colorOpts.grid(row=0, column=1, padx=(20, 5), pady=5)

        self.opacityFrame = tb.Frame(self.styleFrame)
        self.opacityFrame.grid(row=0, column=2, padx=(0, 5))

        tb.Label(self.opacityFrame, text="Opacity", font=("Franklin Gothic", 12)).grid(row=0, column=0, padx=(55,5), pady=5)
        self.alphaOpts = tb.Spinbox(self.opacityFrame, from_=0.0, to=10.0, format="%.1f", width=5)
        self.alphaOpts.set(10.0)
        self.alphaOpts.grid(row=0, column=1, padx=(5,15), pady=5)
        
        tb.Label(self.styleFrame, text="E-Color", font=("Franklin Gothic", 12)).grid(row=1, column=0, padx=(5,15), pady=5)
        self.edgeOpts = tb.Entry(self.styleFrame, width=17)
        self.edgeOpts.grid(row=1, column=1, padx=(20, 5), pady=5)

        self.fineFrame = tb.Frame(self.styleFrame)
        self.fineFrame.grid(row=1, column=2, padx=(0, 5))

        tb.Label(self.fineFrame, text="Fineness", font=("Franklin Gothic", 12)).grid(row=0, column=0, padx=(55,10), pady=5)
        self.fineOpts = tb.Spinbox(self.fineFrame, from_=10.0, to=1000.0, width=5)
        self.fineOpts.set(10)
        self.fineOpts.grid(row=0, column=1, padx=(0,25), pady=5)

        for widget in frame.winfo_children():
            widget.grid_configure(pady=5, padx=20)

        for widget in frame2.winfo_children():
            widget.grid_configure(pady=5, padx=20)


    def addFunction(self):
        if self.count == 9 and self.count2 == 2:
            self.addBtn.config(bootstyle="secondary")
            self.functions = tb.Entry(self.entryFrame)
            self.functions.grid(row=self.count, column=self.count2, padx=5, pady=5)
            self.count += 1
        elif self.count == 10 and self.count2 == 2:
            messagebox.showerror(message="Max Functions Reached!", title="Error")
        else:
            self.functions = tb.Entry(self.entryFrame)
            self.functions.grid(row=self.count, column=self.count2, padx=5, pady=5)
            if self.count == 9:
                self.count2 += 1
                self.count = 0
            else:
                self.count += 1

    def changeRange(self):
        if self.yFuncV.get():
            self.rangeLabel.config(text="Range (y) : ")
        else:
            self.rangeLabel.config(text="Range (x) : ")

    def show(self):
        plt.clf()

        for entry in self.entryFrame.winfo_children():
            if len(entry.get()) == 0:
                continue
            expr = entry.get()
            vexpr = expr

            
            if len(self.rangeX1.get()) == 0 or len(self.rangeX2.get()) == 0: 
                messagebox.showerror(title='Missing Range', message=f"Please Provide a Range")
                return
            x = np.linspace(eval(self.rangeX1.get()), eval(self.rangeX2.get()), 10000)
            
            expr = expr.replace("^", "**", expr.count("^"))
            c = 0
            while c != len(expr)-1:
                if expr[c].isnumeric() and (expr[c+1] == 'x' or expr[c+1] == 'y'):
                    expr = expr[:c+1] + "*" + expr[c+1:]
                c += 1
            
            for _ in range(expr.count("sec") + expr.count("cosec") + expr.count("cot")):
                if expr.count("cosec") != 0:
                    expr = expr[:expr.index("cosec")] + "1/" + expr[expr.index("cosec"):]
                    expr = expr.replace("cosec", "cos")
                elif expr.count("sec") != 0:
                    expr = expr[:expr.index("sec")] + "1/" + expr[expr.index("sec"):]
                    expr = expr.replace("sec", "sin")
                elif expr.count("cot") != 0:
                    expr = expr[:expr.index("cot")] + "1/" + expr[expr.index("cot"):]
                    expr = expr.replace("cot", "tan")

            try:
                if not(self.yFuncV.get()):
                    y = eval(expr, {
                        "x": x, 
                        "e": np.e, 
                        "np": np, 
                        "sin": np.sin,
                        "cos": np.cos,
                        "tan": np.tan,
                        "sqrt": np.sqrt,
                        "log": np.log,
                        "__builtins__": {}
                        })
                else:
                    y = eval(expr, {
                        "y":x,
                        "e": np.e, 
                        "np": np, 
                        "sin": np.sin,
                        "cos": np.cos,
                        "tan": np.tan,
                        "sqrt": np.sqrt,
                        "log": np.log,
                        "__builtins__": {}
                        })
                
            except Exception as e:
                messagebox.showerror(title='Function Parsing Error', message=f"Error evaluating function: {e}")
                return
            
            plt.plot(x, y, label=f'{vexpr}') if not(self.yFuncV.get()) else plt.plot(y, x, label=f'{vexpr}')

        plt.xlabel('X')
        plt.ylabel('Y')
        if self.legendV.get(): plt.legend()
        plt.ylim(eval(self.rangeX1.get())*4, eval(self.rangeX2.get())*4)
        plt.grid(True)
        plt.show()

    def show3D(self):
        plt.clf()
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        expr = self.function.get()
        if len(expr) == 0:
            messagebox.showerror(title='Invalid Function', message="Please Provide a Function")
            return
        alpha = self.alphaOpts.get()
        if len(alpha) == 0 :
            alpha = 10.0
        else:
            alpha = alpha.replace(',', '.')
            alpha = float(alpha)
        colormap = self.colorOpts.get()
        colormap = 'viridis' if len(colormap) == 0 else colormap
        edgecolor = self.edgeOpts.get()
        edgecolor = 'forestgreen' if len(edgecolor) == 0 else edgecolor
        fineness = self.fineOpts.get()
        fineness = 10 if len(fineness) == 0 else int(fineness)

        
        if len(self.rangeX12.get()) == 0 or len(self.rangeX22.get()) == 0: 
            messagebox.showerror(title='Missing Range', message=f"Please Provide a Range")
            return
        x = np.outer(np.linspace(eval(self.rangeX12.get()), eval(self.rangeX22.get()), fineness), np.ones(fineness))
        y = x.copy().T
        
        expr = expr.replace("^", "**", expr.count("^"))
        for var in ['x', 'y', 'z']:
            expr = expr.replace(f'0{var}', f'0*{var}')
            for d in '123456789':
                expr = expr.replace(f'{d}{var}', f'{d}*{var}')
                
        for _ in range(expr.count("sec") + expr.count("cosec") + expr.count("cot")):
            if expr.count("cosec") != 0:
                expr = expr[:expr.index("cosec")] + "1/" + expr[expr.index("cosec"):]
                expr = expr.replace("cosec", "cos")
            elif expr.count("sec") != 0:
                expr = expr[:expr.index("sec")] + "1/" + expr[expr.index("sec"):]
                expr = expr.replace("sec", "sin")
            elif expr.count("cot") != 0:
                expr = expr[:expr.index("cot")] + "1/" + expr[expr.index("cot"):]
                expr = expr.replace("cot", "tan")

        fFrmt = self.selectedVar.get()

        try:
            if fFrmt == 0:
                z = eval(expr, {
                    "x": x,
                    "y": y, 
                    "np": np, 
                    "sin": np.sin, 
                    "cos": np.cos, 
                    "tan": np.tan, 
                    "sqrt": np.sqrt, 
                    "log": np.log, 
                    "e": np.e, 
                    "__builtins__": {}
                })
            elif fFrmt == 1:
                z = eval(expr, {
                    "x": x,
                    "z": y, 
                    "np": np, 
                    "sin": np.sin, 
                    "cos": np.cos, 
                    "tan": np.tan, 
                    "sqrt": np.sqrt, 
                    "log": np.log, 
                    "e": np.e, 
                    "__builtins__": {}
                })
            else:
                z = eval(expr, {
                    "z": x,
                    "y": y, 
                    "np": np, 
                    "sin": np.sin, 
                    "cos": np.cos, 
                    "tan": np.tan, 
                    "sqrt": np.sqrt, 
                    "log": np.log, 
                    "e": np.e, 
                    "__builtins__": {}
                })
                
        except Exception as e:
            messagebox.showerror(title='Function Parsing Error', message=f"Error evaluating function: {e}")
            return

        if self.wireframeV.get():
            ax.plot_wireframe(x, y, z, color=edgecolor, alpha=alpha/10)
        elif self.triangulationV.get():
            x = np.linspace(eval(self.rangeX12.get()), eval(self.rangeX22.get()), fineness)
            y = np.linspace(eval(self.rangeX12.get()), eval(self.rangeX22.get()), fineness)
            X, Y = np.meshgrid(x, y)
            expr = expr.replace('x', 'X', expr.count("x"))
            expr = expr.replace('y', 'Y', expr.count("y"))
            expr = expr.replace('z', 'Z', expr.count("z"))

            if fFrmt == 0:
                z = eval(expr, {
                    "X": X,
                    "Y": Y, 
                    "np": np, 
                    "sin": np.sin, 
                    "cos": np.cos, 
                    "tan": np.tan, 
                    "sqrt": np.sqrt, 
                    "log": np.log, 
                    "e": np.e, 
                    "__builtins__": {}
                })
            elif fFrmt == 1:
                z = eval(expr, {
                    "X": X,
                    "Z": Y, 
                    "np": np, 
                    "sin": np.sin, 
                    "cos": np.cos, 
                    "tan": np.tan, 
                    "sqrt": np.sqrt, 
                    "log": np.log, 
                    "e": np.e, 
                    "__builtins__": {}
                })
            else:
                z = eval(expr, {
                    "Z": X,
                    "Y": Y, 
                    "np": np, 
                    "sin": np.sin, 
                    "cos": np.cos, 
                    "tan": np.tan, 
                    "sqrt": np.sqrt, 
                    "log": np.log, 
                    "e": np.e, 
                    "__builtins__": {}
                })

            tri = Triangulation(X.ravel(), Y.ravel())

            ax.plot_trisurf(tri, z.ravel(), cmap=colormap, edgecolor=edgecolor, alpha=alpha/10)
        else:
            ax.plot_surface(x, y, z, cmap=colormap, edgecolor=edgecolor, alpha=alpha/10)
            
        plt.show()
    
    def toggle1(self):
        self.triangulationV.set(0)
    
    def toggle2(self):
        self.wireframeV.set(0)
    

root = tb.Window(themename="darkly", maxsize=(500,600), minsize=(500,600))
Main(root)
root.mainloop()
