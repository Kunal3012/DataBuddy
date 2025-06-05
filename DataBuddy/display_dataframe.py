import tkinter as tk
from tkinter import ttk
import pandas as pd
import random
def display_dataframe(df):
    root=tk.Tk()
    root.title("DataFrame Viewer")
    root.geometry("1200x600")
    root.configure(bg="#001100")  # Background set to black

    # Create canvas for animated digits
    canvas=tk.Canvas(root,bg="#001100",highlightthickness=0)
    canvas.pack(fill="both",expand=True)

    def animate_numbers():
        canvas.delete("numbers")  # Clear previous numbers
        width=root.winfo_width()
        height=root.winfo_height()
        columns=width//30
        rows=height//30
        for col in range(columns):
            x=col*30+15
            for row in range(rows):
                y=row*30+random.randint(-5,5)
                number=random.randint(0,9)
                canvas.create_text(x,y,text=str(number),fill="#00FF00",font=("Courier",14),tags="numbers")
        root.after(100,animate_numbers)

    animate_numbers()

    # Create scrollable canvas for the dataframe
    scroll_canvas=tk.Canvas(canvas,bg="#001100",highlightthickness=2,highlightbackground="#00FF00")  # Green border
    scroll_canvas.place(relx=0.5,rely=0.5,anchor="center",relwidth=0.8,relheight=0.8)

    scrollbar=tk.Scrollbar(canvas,orient="vertical",command=scroll_canvas.yview,bg="#00FF00")  # Green scrollbar
    scrollbar.place(relx=0.9,rely=0.5,anchor="center",relheight=0.8)

    scroll_frame=tk.Frame(scroll_canvas,bg="#001100")
    scroll_canvas.create_window((0,0),window=scroll_frame,anchor="nw")
    scroll_canvas.configure(yscrollcommand=scrollbar.set)

    def on_frame_configure(event):
        scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all"))

    scroll_frame.bind("<Configure>",on_frame_configure)

    # Create a Treeview to display the dataframe
    tree=ttk.Treeview(scroll_frame,columns=list(df.columns),show="headings",style="Custom.Treeview")
    for col in df.columns:
        tree.heading(col,text=col)
        tree.column(col,width=150,anchor="center")
    for _,row in df.iterrows():
        tree.insert("", "end",values=list(row))
    tree.pack(fill="both",expand=True)

    # Apply custom style for Treeview
    style=ttk.Style()
    style.configure("Custom.Treeview",background="#001100",foreground="#00FF00",fieldbackground="#001100",font=("Courier",12))
    style.configure("Custom.Treeview.Heading",background="#001100",foreground="#00FF00",font=("Courier",14,"bold"))
    style.map("Custom.Treeview",background=[("selected","#00FF00")],foreground=[("selected","#001100")])

    root.mainloop()

if __name__=="__main__":
    sample_data={"Column1":[1,2,3,4,5],"Column2":["A","B","C","D","E"],"Column3":[10.5,20.3,30.2,40.1,50.0]}
    df=pd.DataFrame(sample_data)
    display_dataframe(df)
