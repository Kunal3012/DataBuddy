# DataBuddy Project

DataBuddy is a comprehensive, user-friendly data analysis and machine learning application designed to simplify the workflow of data processing, visualization, model training, and evaluation. It provides an intuitive graphical user interface (GUI) for users to interact with their data and perform advanced machine learning tasks without requiring extensive coding knowledge.

## Key Features

### 1. **User Interface**
- A visually appealing and interactive GUI built using `tkinter`.
- Animated background elements for an engaging user experience.
- Easy navigation between different modules such as data input, visualization, and model training.

### 2. **Data Loading**
- Load datasets from local files (CSV, Excel) or directly from URLs.
- Preview datasets with scrollable tables to inspect data before processing.
- Handle large datasets efficiently with optimized memory usage.

### 3. **Data Preprocessing**
- Automatically clean and preprocess raw data.
- Handle missing values by dropping or imputing them.
- Encode categorical variables using one-hot encoding or label encoding.
- Generate summary statistics and null value counts for better data understanding.

### 4. **Exploratory Data Analysis (EDA)**
- Visualize data distributions using histograms, box plots, bar charts, pie charts, and count plots.
- Interactive dropdowns to select columns for visualization.
- Zoom and open visualizations in new windows for detailed analysis.

### 5. **Feature Engineering**
- Create new features based on existing data to improve model performance.
- Select specific columns for model training using checkboxes.

### 6. **Model Selection**
- Choose from a variety of machine learning models, including:
  - Random Forest Classifier
  - Logistic Regression
  - Support Vector Machines (SVM)
  - Gradient Boosting Models
- Dropdown menus to select the desired model type.

### 7. **Model Training**
- Split data into training and testing sets with customizable train-test ratios.
- Train models on the selected dataset with a single click.
- Save trained models for future use.

### 8. **Model Evaluation**
- Evaluate model performance using metrics such as accuracy, precision, recall, and F1-score.
- Display evaluation results in a clear and concise format.

### 9. **Report Generation**
- Generate comprehensive reports summarizing the data analysis, model training, and evaluation results.
- Export reports in PDF or HTML format for sharing and documentation.

## Project Structure

```
DataBuddy/
├── DataBuddy/
│   ├── main.py                # Entry point for the application
│   ├── welcome_window.py      # Welcome screen module
│   ├── data_input.py          # Data input and preprocessing module
│   ├── visualization.py       # Data visualization module
│   ├── trainermodule.py       # Model training module
│   ├── temp_dataset.pkl       # Temporary dataset storage
│   ├── README.md              # Project documentation
│   └── LICENSE                # License file
├── requirements.txt           # Python dependencies
└── .venv/                     # Virtual environment (optional)
```

## Installation

### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DataBuddy.git
   ```
2. Navigate to the project directory:
   ```bash
   cd DataBuddy
   ```
3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Follow the GUI prompts to:
   - Load and preprocess your dataset.
   - Visualize data distributions and relationships.
   - Train machine learning models.
   - Evaluate model performance and generate reports.

## Contributing

We welcome contributions to enhance DataBuddy! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Libraries Used**:
  - `tkinter` for GUI development.
  - `pandas` for data manipulation.
  - `matplotlib` and `seaborn` for data visualization.
  - `scikit-learn` for machine learning model training and evaluation.
- **Inspiration**: Simplifying data science workflows for non-programmers.

## Future Enhancements

- Add support for deep learning models using TensorFlow or PyTorch.
- Integrate additional visualization libraries like Plotly for interactive plots.
- Enable cloud-based data storage and processing.
- Add a feature for automated hyperparameter tuning.