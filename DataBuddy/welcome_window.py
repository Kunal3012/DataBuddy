import tkinter as tk
from tkinter import ttk
import subprocess  # To launch the new file
import random  # For generating random numbers

def create_welcome_window():
    # Initialize the main window
    root = tk.Tk()
    root.title("AutoDataAnalyzer – Welcome Screen")
    root.attributes("-fullscreen", True)
    root.configure(bg="#001100")  # Background set to black

    # Create canvas for background animation
    canvas = tk.Canvas(root, bg="#001100", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    def animate_numbers():
        canvas.delete("numbers")  # Clear previous numbers
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
                    fill="#00FF00",  # Text color set to green
                    font=("Courier", 14),
                    tags="numbers"
                )
        root.after(100, animate_numbers)

    animate_numbers()

    # Application Title
    title_label = tk.Label(
        root,
        text="AutoDataAnalyzer – Your AI-Powered\nNo-Code Data Science Tool",
        font=("Courier", 28, "bold"),
        fg="#00FF00",  # Text color set to green
        bg="#001100"  # Background set to black
    )
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # Tagline
    tagline_label = tk.Label(
        root,
        text='"From Dataset to Decision – All in One Click!"',
        font=("Courier", 20, "italic"),
        fg="#00FF00",  # Text color set to green
        bg="#001100"  # Background set to black
    )
    tagline_label.place(relx=0.5, rely=0.2, anchor="center")

    # Key Features
    features_frame = tk.Frame(root, bg="#001100")  # Background set to black
    features_frame.place(relx=0.5, rely=0.4, anchor="center")
    features = [
        "✅ Import data from file or URL",
        "✅ Perform automatic data cleaning and preprocessing",
        "✅ Visualize your data with charts and plots",
        "✅ Train machine learning models (classification & regression)",
        "✅ Generate comprehensive EDA and ML reports",
        "✅ No coding required – fully GUI-based",
        "✅ Save models and analysis for future use"
    ]
    for feature in features:
        feature_label = tk.Label(
            features_frame,
            text=feature,
            font=("Courier", 16),
            fg="#00FF00",  # Text color set to green
            bg="#001100"  # Background set to black
        )
        feature_label.pack(anchor="w", pady=5)

    # Navigation Buttons
    nav_frame = tk.Frame(root, bg="#001100")  # Background set to black
    nav_frame.place(relx=0.5, rely=0.7, anchor="center")
    style = ttk.Style()
    style.configure(
        "Custom.TButton",
        background="#00FF00",  # Button background set to green
        foreground="#001100",  # Button text set to black
        font=("Courier", 16),
        borderwidth=2,
        relief="solid"
    )
    style.map(
        "Custom.TButton",
        background=[("active", "#001100"), ("pressed", "#001100")],
        foreground=[("active", "#00FF00"), ("pressed", "#00FF00")]
    )

    start_analysis_button = ttk.Button(
        nav_frame, text="🔍 Start Analysis", width=35, command=lambda: subprocess.Popen(["python3", "/home/sky/Desktop/DataBuddy/data_input.py"]), style="Custom.TButton"
    )
    start_analysis_button.grid(row=0, column=0, padx=30, pady=15)

    help_button = ttk.Button(nav_frame, text="❓ Help / User Guide", width=35, style="Custom.TButton")
    help_button.grid(row=0, column=1, padx=30, pady=15)

    exit_button = ttk.Button(nav_frame, text="🚪 Exit", width=35, command=root.destroy, style="Custom.TButton")
    exit_button.grid(row=0, column=2, padx=30, pady=15)

    # Footer Info
    footer_label = tk.Label(
        root,
        text="Developed by: Kunal Yadav\nVersion: 1.0.0\nLast Updated: May 2025\n© 2025 AutoDataAnalyzer",
        font=("Courier", 14),
        fg="#00FF00",  # Text color set to green
        bg="#001100",  # Background set to black
        justify="center"
    )
    footer_label.place(relx=0.5, rely=0.9, anchor="center")

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    create_welcome_window()
