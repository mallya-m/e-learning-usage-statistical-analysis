#  Statistical Analysis of E-Learning Platform Usage

##  Overview

This project presents a comprehensive statistical analysis of student interaction data from an E-Learning platform. It aims to uncover patterns between student engagement and academic performance using statistical techniques, data visualization, and predictive modeling.

The project is implemented as a complete data pipeline, starting from data generation to an interactive web-based dashboard.

---

##  Objectives

* Analyze student engagement metrics such as login frequency, session duration, and course completion
* Identify correlations between platform usage and academic performance
* Perform hypothesis testing to validate insights
* Build predictive models to detect at-risk students
* Develop an interactive dashboard for visualization

---

##  Project Architecture

### 🔹 Data Layer

* Synthetic data generation using Faker (or Kaggle datasets)
* Storage using SQLite database

### 🔹 Processing Layer

* Data cleaning and preprocessing using Pandas
* Feature engineering (Engagement Score, Completion Rate)

### 🔹 Statistical Analysis

* Correlation Analysis (Pearson)
* Hypothesis Testing (T-test)
* Regression Analysis (OLS using Statsmodels)

### 🔹 Machine Learning

* Student clustering (K-Means)
* Performance prediction (Linear Regression)

### 🔹 Visualization Layer

* Static plots: Matplotlib, Seaborn
* Interactive charts: Plotly

### 🔹 Deployment

* Streamlit dashboard for real-time interaction

---

##  Tech Stack

| Category         | Tools Used                  |
| ---------------- | --------------------------- |
| Language         | Python 3.x                  |
| Data Analysis    | Pandas, NumPy               |
| Statistics       | SciPy, Statsmodels          |
| Machine Learning | Scikit-learn                |
| Visualization    | Matplotlib, Seaborn, Plotly |
| Database         | SQLite                      |
| Deployment       | Streamlit                   |
| IDE              | Jupyter Notebook, VS Code   |

---

##  Key Features

*  Correlation Heatmaps
*  Distribution Analysis (Histograms)
*  Regression Modeling with Statistical Output
*  Student Segmentation (Clustering)
*  Interactive Dashboard (Streamlit)

---

##  Screenshots (To be added)

* Dashboard Overview
* Correlation Heatmap
* Session Duration Distribution
* Regression Output Summary
* Student Segmentation Visualization

---

##  Methodology

### 1. Data Generation & Storage

Synthetic datasets were generated to simulate real-world student activity and stored in SQLite.

### 2. Data Processing

Data was cleaned, normalized, and transformed into meaningful features such as Engagement Score.

### 3. Statistical Analysis

Hypothesis testing and regression analysis were conducted to evaluate relationships between engagement and performance.

### 4. Predictive Modeling

Machine learning techniques were used to classify student behavior and predict outcomes.

### 5. Visualization & Deployment

Insights were presented through visualizations and deployed using Streamlit for interactive exploration.

---

##  Individual Contribution

* Designed complete system architecture
* Implemented statistical models (T-test, regression)
* Built engagement scoring system
* Developed interactive Streamlit dashboard
* Integrated visualization components

---

##  How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/e-learning-usage-statistical-analysis.git

# Navigate into the project
cd e-learning-usage-statistical-analysis

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---

##  Future Enhancements

* Dropout prediction system
* Recommendation engine for learning content
* Real-time data integration
* Advanced ML models

---

##  Conclusion

This project demonstrates how data analytics and statistical modeling can provide actionable insights into student learning behavior, enabling better decision-making in educational platforms.

---

##  License

This project is for academic and educational purposes.
