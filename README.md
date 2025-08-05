 Student Attendance Analyzer

This project analyzes and visualizes attendance data to help identify trends, highlight low attendance, and support academic interventions.

---

Project Files

- `attendance_analyzer.py` — Main Python script for analyzing attendance
- `sample_data.csv` — Example attendance data
- `README.md` — Project documentation

---

 Features

- Calculates monthly attendance rates per class
- Flags classes with low attendance (<90%)
- Visualizes attendance using bar charts

---

 How to Use

 Option 1: Run Locally

#### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/student-attendance-analyzer.git
cd student-attendance-analyzer
```

#### Step 2: Install Required Packages

```bash
pip install pandas matplotlib seaborn
```

#### Step 3: Run the Script

```bash
python attendance_analyzer.py
```

📊 The script will print a summary and show a bar chart of attendance rates.

---

Option 2: Run on Google Colab

1. Open [Google Colab](https://colab.research.google.com)
2. Paste and run the following code:

```python
!git clone https://github.com/yourusername/student-attendance-analyzer.git
%cd student-attendance-analyzer
!pip install seaborn
!python attendance_analyzer.py
```

The script will execute and the plot will appear in the output.

---

 Sample Output

A bar chart showing attendance percentage by class and month, with a red line indicating the 90% threshold.

---

 Project Goal

To support academic decisions through clear, actionable attendance insights.

