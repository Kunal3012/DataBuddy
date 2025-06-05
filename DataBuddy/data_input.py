import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd
import random
import pickle  # For saving the dataset to a file
import subprocess  # For launching the visualization file

def create_data_input_window():
    def animate_numbers():
        canvas.delete("numbers")
        width = root.winfo_width()
        height = root.winfo_height()
        columns = width // 30
        rows = height // 30
        for col in range(columns):
            x = col * 30 + 15
            for row in range(rows):
                y = row * 30 + random.randint(-5, 5)
                number = random.randint(0, 9)
                canvas.create_text(
                    x, y,
                    text=str(number),
                    fill="#00FF00",
                    font=("Courier", 14),
                    tags="numbers"
                )
        root.after(100, animate_numbers)

    def load_dataset_from_url():
        url = url_entry.get()
        try:
            df = pd.read_csv(url)
            show_preview(df)
            message_label.config(text="Dataset loaded successfully!", fg="green")
        except Exception as e:
            message_label.config(text=f"Error loading dataset: {e}", fg="red")

    def load_dataset_from_file():
        file_path = askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xls;*.xlsx")])
        if file_path:
            selected_file_label.config(text=f"Selected File: {file_path}")
            try:
                if file_path.endswith(".csv"):
                    df = pd.read_csv(file_path)
                elif file_path.endswith((".xls", ".xlsx")):
                    df = pd.read_excel(file_path)
                else:
                    raise ValueError("Unsupported file format.")
                show_preview(df)
                message_label.config(text="Dataset loaded successfully!", fg="green")
            except Exception as e:
                message_label.config(text=f"Error loading dataset: {e}", fg="red")

    def proceed_to_visualization(df):
        visualization_file = "/home/sky/Desktop/DataBuddy/visualization.py"
        dataset_file = "/home/sky/Desktop/DataBuddy/temp_dataset.pkl"
        with open(dataset_file, "wb") as f:
            pickle.dump(df, f)  # Save the dataset to a temporary file
        subprocess.Popen(["python3", visualization_file])  # Launch the visualization file

    def show_preview(df):
        # Clear previous widgets
        for widget in preview_frame.winfo_children():
            widget.destroy()
        for widget in stats_frame.winfo_children():
            widget.destroy()

        # Create scrollable preview section
        preview_canvas = tk.Canvas(preview_frame, bg="#001100", highlightthickness=0)
        preview_canvas.pack(side="left", fill="both", expand=True)

        preview_scrollbar = tk.Scrollbar(preview_frame, orient="vertical", command=preview_canvas.yview)
        preview_scrollbar.pack(side="right", fill="y")

        preview_scroll_frame = tk.Frame(preview_canvas, bg="#001100")
        preview_canvas.create_window((0, 0), window=preview_scroll_frame, anchor="nw")
        preview_canvas.configure(yscrollcommand=preview_scrollbar.set)

        def on_preview_frame_configure(event):
            preview_canvas.configure(scrollregion=preview_canvas.bbox("all"))

        preview_scroll_frame.bind("<Configure>", on_preview_frame_configure)

        # Display preview table
        preview_table = ttk.Treeview(preview_scroll_frame, columns=list(df.columns), show="headings", style="Custom.Treeview")
        for col in df.columns:
            preview_table.heading(col, text=col)
            preview_table.column(col, width=150)
        for _, row in df.head(10).iterrows():
            preview_table.insert("", "end", values=list(row))
        preview_table.pack(fill="both", expand=True)

        # Create scrollable statistics section
        stats_canvas = tk.Canvas(stats_frame, bg="#001100", highlightthickness=0)
        stats_canvas.pack(side="left", fill="both", expand=True)

        stats_scrollbar = tk.Scrollbar(stats_frame, orient="vertical", command=stats_canvas.yview)
        stats_scrollbar.pack(side="right", fill="y")

        stats_scroll_frame = tk.Frame(stats_canvas, bg="#001100")
        stats_canvas.create_window((0, 0), window=stats_scroll_frame, anchor="nw")
        stats_canvas.configure(yscrollcommand=stats_scrollbar.set)

        def on_stats_frame_configure(event):
            stats_canvas.configure(scrollregion=stats_canvas.bbox("all"))

        stats_scroll_frame.bind("<Configure>", on_stats_frame_configure)

        # Display null value counts
        null_counts = df.isnull().sum()
        null_label = tk.Label(stats_scroll_frame, text="Null Value Counts:", font=("Courier", 14), fg="#00FF00", bg="#001100")
        null_label.pack(anchor="w", fill="x")
        null_text = tk.Text(stats_scroll_frame, height=5, bg="#001100", fg="#00FF00", font=("Courier", 12), relief="sunken", borderwidth=2)
        null_text.insert("1.0", null_counts.to_string())
        null_text.config(state="disabled")
        null_text.pack(fill="x", padx=10, pady=5)

        # Display describe table
        describe_label = tk.Label(stats_scroll_frame, text="Describe Function Output:", font=("Courier", 14), fg="#00FF00", bg="#001100")
        describe_label.pack(anchor="w", fill="x")
        describe_table = ttk.Treeview(stats_scroll_frame, columns=["Category"] + list(df.describe().columns), show="headings", style="Custom.Treeview")
        describe_table.heading("Category", text="Category")
        describe_table.column("Category", width=150, anchor="center")
        for col in df.describe().columns:
            describe_table.heading(col, text=col)
            describe_table.column(col, width=150)
        for index, row in df.describe().iterrows():
            describe_table.insert("", "end", values=[index] + list(row))
        describe_table.pack(fill="both", expand=True)

        # Update the Proceed button to pass the dataset
        proceed_button.config(command=lambda: proceed_to_visualization(df))

    def reset_window():
        url_entry.delete(0, tk.END)
        selected_file_label.config(text="")
        message_label.config(text="")
        for widget in preview_frame.winfo_children():
            widget.destroy()
        for widget in stats_frame.winfo_children():
            widget.destroy()

    # Initialize the main window
    root = tk.Tk()
    root.title("Data Input – Upload or Link Your Dataset")
    root.attributes("-fullscreen", True)
    root.configure(bg="#001100")

    # Create canvas for background animation
    canvas = tk.Canvas(root, bg="#001100", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    animate_numbers()

    # Apply custom style for Treeview
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#001100", foreground="#00FF00", fieldbackground="#001100", font=("Courier", 12))
    style.configure("Custom.Treeview.Heading", background="#001100", foreground="#00FF00", font=("Courier", 14, "bold"))
    style.map("Custom.Treeview", background=[("selected", "#00FF00")], foreground=[("selected", "#001100")])

    # Apply custom style for buttons
    style.configure("Custom.TButton", background="#00FF00", foreground="#001100", font=("Courier", 12), borderwidth=2, relief="solid")
    style.map("Custom.TButton", background=[("active", "#001100"), ("pressed", "#001100")], foreground=[("active", "#00FF00"), ("pressed", "#00FF00")])

    # Apply custom style for URL entry box
    style.configure("Custom.TEntry", fieldbackground="#00FF00", foreground="#001100", font=("Courier", 12))
    style.map("Custom.TEntry", fieldbackground=[("focus", "#001100")], foreground=[("focus", "#00FF00")])

    # Application Title
    title_label = tk.Label(
        root,
        text="Data Input – Upload or Link Your Dataset",
        font=("Courier", 28, "bold"),
        fg="#00FF00",
        bg="#001100"
    )
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # Section: Input Field
    input_field_frame = tk.Frame(root, bg="#001100")
    input_field_frame.place(relx=0.5, rely=0.3, anchor="center")
    url_entry = ttk.Entry(input_field_frame, width=50, style="Custom.TEntry")
    url_entry.insert(0, "https://datahub.io/...")
    browse_button = ttk.Button(input_field_frame, text="📂 Browse File", command=load_dataset_from_file, style="Custom.TButton")
    selected_file_label = tk.Label(input_field_frame, text="", font=("Courier", 12), fg="#00FF00", bg="#001100")
    load_button = ttk.Button(input_field_frame, text="🔄 Load Dataset", command=lambda: load_dataset_from_url() if url_entry.get() else load_dataset_from_file, style="Custom.TButton")
    url_entry.grid(row=0, column=0, padx=10, pady=5)
    browse_button.grid(row=0, column=1, padx=10, pady=5)
    selected_file_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
    load_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Section: Output Preview
    preview_frame = tk.Frame(root, relief="sunken", borderwidth=1, bg="#001100")
    preview_frame.place(relx=0.5, rely=0.4, anchor="center", relwidth=0.9, height=200)  # Expand to 90% width
    preview_label = tk.Label(preview_frame, text="Preview of Dataset:", font=("Courier", 16), fg="#00FF00", bg="#001100")
    preview_label.pack(anchor="w", fill="x")  # Expand label to full width

    # Section: Statistics (Null Counts and Describe Output)
    stats_frame = tk.Frame(root, relief="sunken", borderwidth=1, bg="#001100")
    stats_frame.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.9, height=300)  # Expand to 90% width

    # Section: Message Area
    message_label = tk.Label(root, text="", font=("Courier", 14), fg="#00FF00", bg="#001100")
    message_label.place(relx=0.5, rely=0.7, anchor="center")

    # Section: Navigation Buttons
    navigation_frame = tk.Frame(root, bg="#001100")
    navigation_frame.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.9)
    proceed_button = ttk.Button(navigation_frame, text="▶️ Proceed to Visualization", style="Custom.TButton")
    reset_button = ttk.Button(navigation_frame, text="🔁 Reset", command=reset_window, style="Custom.TButton")
    back_button = ttk.Button(navigation_frame, text="⬅️ Back to Home", command=root.destroy, style="Custom.TButton")
    proceed_button.grid(row=0, column=0, padx=10, pady=5)
    reset_button.grid(row=0, column=1, padx=10, pady=5)
    back_button.grid(row=0, column=2, padx=10, pady=5)

    root.mainloop()

# Call the function to display the window
if __name__ == "__main__":
    create_data_input_window()
