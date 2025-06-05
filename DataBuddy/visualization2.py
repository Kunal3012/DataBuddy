import tkinter as tk
from tkinter import ttk
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import random

def load_dataset():
    dataset_file = "/home/sky/Desktop/DataBuddy/temp_dataset.pkl"
    with open(dataset_file, "rb") as f:
        return pickle.load(f)

def create_visualization_window():
    df=load_dataset()
    root=tk.Tk()
    root.title("Interactive Dashboard")
    root.geometry("1600x800")
    root.configure(bg="#001100")
    canvas=tk.Canvas(root,bg="#001100",highlightthickness=0)
    canvas.pack(fill="both",expand=True)
    def animate_numbers():
        canvas.delete("numbers")
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
    style=ttk.Style()
    style.configure("Custom.Treeview",background="#001100",foreground="#00FF00",fieldbackground="#001100",font=("Courier",12))
    style.configure("Custom.Treeview.Heading",background="#001100",foreground="#00FF00",font=("Courier",14,"bold"))
    style.map("Custom.Treeview",background=[("selected","#00FF00")],foreground=[("selected","#001100")])
    style.configure("Custom.TButton",background="#00FF00",foreground="#001100",font=("Courier",12),borderwidth=2,relief="solid")
    style.map("Custom.TButton",background=[("active","#001100"),("pressed","#001100")],foreground=[("active","#00FF00"),("pressed","#00FF00")])
    notebook=ttk.Notebook(canvas)
    notebook.pack(fill="both",expand=True)
    def create_scrollable_tab(notebook,title):
        tab=tk.Frame(notebook,bg="#001100")
        notebook.add(tab,text=title)
        scroll_canvas=tk.Canvas(tab,bg="#001100",highlightthickness=2,highlightbackground="#00FF00")
        scroll_canvas.pack(fill="both",expand=True)
        scrollbar=tk.Scrollbar(tab,orient="vertical",command=scroll_canvas.yview)
        scrollbar.pack(side="right",fill="y")
        scroll_frame=tk.Frame(scroll_canvas,bg="#001100")
        scroll_canvas.create_window((0,0),window=scroll_frame,anchor="nw")
        scroll_canvas.configure(yscrollcommand=scrollbar.set)
        def on_frame_configure(event):
            scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all"))
        scroll_frame.bind("<Configure>",on_frame_configure)
        return scroll_frame
    histogram_tab=create_scrollable_tab(notebook,"Histogram")
    boxplot_tab=create_scrollable_tab(notebook,"Box Plot")
    bar_chart_tab=create_scrollable_tab(notebook,"Bar Chart")
    pie_chart_tab=create_scrollable_tab(notebook,"Pie Chart")
    countplot_tab=create_scrollable_tab(notebook,"Count Plot")
    def create_zoom_window(plot_function,column):
        zoom_window=tk.Toplevel()
        zoom_window.title("Zoomed Visualization")
        zoom_window.geometry("800x600")
        zoom_window.configure(bg="#001100")
        fig=plot_function(column)
        canvas=FigureCanvasTkAgg(fig,master=zoom_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both",expand=True)
    def render_plot_with_dropdown(tab,plot_function,column_options,default_column):
        frame=tk.Frame(tab,bg="#001100",relief="sunken",borderwidth=2,highlightbackground="#00FF00")
        frame.pack(fill="both",expand=True,padx=10,pady=10)
        dropdown_var=tk.StringVar(value=default_column)
        def update_plot(*args):
            for widget in frame.winfo_children():
                if isinstance(widget,FigureCanvasTkAgg):
                    widget.get_tk_widget().destroy()
            fig=plot_function(dropdown_var.get())
            canvas=FigureCanvasTkAgg(fig,master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both",expand=True)
        dropdown=ttk.Combobox(frame,values=column_options,textvariable=dropdown_var,state="readonly")
        dropdown.pack(fill="x",pady=5)
        dropdown.bind("<<ComboboxSelected>>",update_plot)
        fig=plot_function(default_column)
        canvas=FigureCanvasTkAgg(fig,master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both",expand=True)
        button_frame=tk.Frame(frame,bg="#001100")
        button_frame.pack(fill="x",pady=5)
        zoom_button=ttk.Button(button_frame,text="🔍 Zoom",command=lambda:create_zoom_window(plot_function,dropdown_var.get()),style="Custom.TButton")
        zoom_button.pack(side="left",padx=5)
        new_window_button=ttk.Button(button_frame,text="🖼️ Open in New Window",command=lambda:create_zoom_window(plot_function,dropdown_var.get()),style="Custom.TButton")
        new_window_button.pack(side="left",padx=5)
    def plot_histogram(column):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(df[column], bins=20, color="green", edgecolor="black")
        ax.set_title(f"Histogram of {column}", fontsize=10)
        ax.set_xlabel(column, fontsize=8)
        ax.set_ylabel("Frequency", fontsize=8)
        plt.close(fig)
        return fig
    def plot_boxplot(column):
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(data=df, x=column, ax=ax, color="green")
        ax.set_title(f"Box Plot of {column}", fontsize=10)
        plt.close(fig)
        return fig
    def plot_bar_chart(column):
        fig, ax = plt.subplots(figsize=(6, 4))
        df[column].value_counts().plot(kind="bar", ax=ax, color="green", edgecolor="black")
        ax.set_title(f"Bar Chart of {column}", fontsize=10)
        ax.set_xlabel(column, fontsize=8)
        ax.set_ylabel("Frequency", fontsize=8)
        plt.close(fig)
        return fig
    def plot_pie_chart(column):
        fig, ax = plt.subplots(figsize=(6, 4))
        df[column].value_counts().plot(kind="pie", ax=ax, autopct="%1.1f%%", colors=sns.color_palette("pastel"))
        ax.set_title(f"Pie Chart of {column}", fontsize=10)
        ax.set_ylabel("")
        plt.close(fig)
        return fig
    def plot_countplot(column):
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.countplot(data=df, x=column, ax=ax, palette="Greens")
        ax.set_title(f"Count Plot of {column}", fontsize=10)
        plt.close(fig)
        return fig
    numerical_columns=df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns=df.select_dtypes(include=["object","category"]).columns.tolist()
    if numerical_columns:
        render_plot_with_dropdown(histogram_tab,plot_histogram,numerical_columns,numerical_columns[0])
    if len(numerical_columns)>1:
        render_plot_with_dropdown(boxplot_tab,plot_boxplot,numerical_columns,numerical_columns[1])
    if categorical_columns:
        render_plot_with_dropdown(bar_chart_tab,plot_bar_chart,categorical_columns,categorical_columns[0])
        render_plot_with_dropdown(pie_chart_tab,plot_pie_chart,categorical_columns,categorical_columns[0])
        render_plot_with_dropdown(countplot_tab,plot_countplot,categorical_columns,categorical_columns[0])
    navigation_frame=tk.Frame(root,bg="#001100")
    navigation_frame.pack(fill="x",pady=10)
    proceed_button=ttk.Button(navigation_frame,text="▶️ Proceed",style="Custom.TButton",command=lambda:print("Proceed clicked"))
    reset_button=ttk.Button(navigation_frame,text="🔄 Reset",style="Custom.TButton",command=lambda:print("Reset clicked"))
    back_button=ttk.Button(navigation_frame,text="⬅️ Back",style="Custom.TButton",command=root.destroy)
    proceed_button.pack(side="left",padx=10)
    reset_button.pack(side="left",padx=10)
    back_button.pack(side="left",padx=10)
    root.mainloop()
if __name__=="__main__":
    create_visualization_window()
