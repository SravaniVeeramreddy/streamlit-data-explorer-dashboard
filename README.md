# 📊 Streamlit Data Explorer & COVID-19 Dashboard

An interactive web application built using **Python and Streamlit** that allows users to explore datasets, perform basic data analysis, visualize information, and monitor sample COVID-19 case trends through an interactive dashboard.

## 🚀 Project Overview

This project demonstrates how Python can be used to build interactive data applications without requiring extensive frontend development.

It combines a general-purpose Data Explorer with a COVID-19 Dashboard to make data exploration and visualization simple and accessible.

## ✨ Features

### 1. Data Explorer
- Upload CSV and Excel files.
- Preview uploaded datasets.
- Display dataset dimensions (rows and columns).
- Identify missing values.
- View column names and data types.
- Generate descriptive statistics.
- Filter datasets using interactive dropdowns.
- Visualize numerical data using histograms.

### 2. COVID-19 Dashboard
- View COVID-19 case trends over time.
- Filter data by state.
- Display total reported cases.
- Calculate average and highest cases.
- Generate interactive line charts using Plotly.
- View filtered COVID-19 records.
- Download filtered data as a CSV file.

### 3. Interactive Interface
- Simple and user-friendly interface.
- Interactive widgets and dropdowns.
- Multiple application sections using tabs.
- Responsive data visualizations.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | Web application development |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Plotly | Interactive charts |
| OpenPyXL | Excel file processing |

## 📂 Project Structure

```text
streamlit-data-explorer-dashboard/
│
├── app.py
├── covid_data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites
- Python 3.10 or later
- Git
- VS Code (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/SravaniVeeramreddy/streamlit-data-explorer-dashboard.git
```

### Step 2: Navigate to the Project Folder

```bash
cd streamlit-data-explorer-dashboard
```

### Step 3: Create a Virtual Environment

```bash
python -m venv myenv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
myenv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python -m streamlit run app.py
```

Open the following URL in your browser:

```text
http://localhost:8501
```

## 📊 Dataset Information

The project uses a sample COVID-19 dataset containing the following columns:

| Column | Description |
|---|---|
| Date | Date of reported cases |
| Cases | Number of reported cases |
| State | State name |

**Note:** The included COVID-19 dataset is sample data created for learning and demonstration purposes. It does not represent official historical or real-time statistics.

The Data Explorer also allows users to upload their own CSV and Excel datasets.

## 📸 Application Screenshots

Add screenshots of your application here after running it.

Example:

```markdown
![Data Explorer](screenshots/data-explorer.png)

![COVID Dashboard](screenshots/covid-dashboard.png)
```

## 🎯 Learning Outcomes

Through this project, I practised:

- Building interactive applications using Streamlit.
- Uploading and processing datasets using Pandas.
- Performing exploratory data analysis.
- Creating interactive visualizations using Plotly.
- Displaying metrics and descriptive statistics.
- Managing Python dependencies.
- Using Git and GitHub for version control.

## 🔮 Future Enhancements

- Add more interactive chart types.
- Include additional statistical analysis.
- Add date-range filters.
- Integrate real-time data sources.
- Deploy the application using Streamlit Community Cloud.

## 👩‍💻 Author

**Sravani Veeramreddy**

GitHub: [SravaniVeeramreddy](https://github.com/SravaniVeeramreddy)

---

⭐ If you find this project useful, feel free to explore and contribute!

