# Statistical Analysis of E-Learning Platform Usage
### 22CS49 — 4th Semester Mini Project | 2025–26

A comprehensive statistical data science project analysing student engagement,
learning behaviour, and academic performance on an e-learning platform.

---

## Team

| Name | Role |
|------|------|
| **Mallya Moni** *(Team Lead)* | End-to-end system architecture, statistical inference engine (OLS / hypothesis testing), predictive modelling for at-risk student patterns |
| **Nandana Raghunath** | Automated synthetic data generation (Faker), SQLite database schema design and management |
| **Pari Tirthwani** | Exploratory data analysis (EDA), interactive visual components (Plotly, Seaborn) |

---

## Objectives

- Analyse student engagement metrics: login frequency, video watch %, assignments, forum activity
- Identify correlations between platform usage and quiz performance
- Perform hypothesis testing (t-test, ANOVA, chi-square) to validate insights statistically
- Build predictive models to detect at-risk students early
- Deliver findings through an interactive Streamlit dashboard

---

## Repository Structure

```
e-learning-usage-statistical-analysis/
├── notebooks/
│   ├── 01_data_generation.ipynb       <- Nandana: synthetic data + SQLite
│   ├── 02_eda_visualisation.ipynb     <- Pari: EDA + interactive charts
│   ├── 03_statistical_inference.ipynb <- Mallya: hypothesis tests + OLS
│   └── 04_predictive_modelling.ipynb  <- Mallya: regression + clustering
├── data/
│   └── elearning_data.csv             <- Clean dataset (1200 students, 11 features)
├── src/
│   └── db_utils.py                    <- SQLite query helper functions
├── outputs/
│   ├── figures/                       <- Saved chart images
│   └── reports/                       <- Exported analysis reports
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Dataset

Synthetic dataset of **1200 student records**, 11 features, seed=42 for reproducibility.

| Column | Type | Description |
|--------|------|-------------|
| student_id | str | Unique ID (STU1000-STU2199) |
| name | str | Student name (Faker, en_IN locale) |
| age | int | Age 18-30 |
| gender | str | Male / Female / Non-binary |
| course | str | One of 6 course types |
| logins_per_week | float | Avg weekly platform logins |
| video_watch_pct | float | Percentage of video content watched (0-100) |
| forum_posts | int | Forum contributions count |
| assignments_submitted | int | Assignments submitted out of 10 |
| quiz_score | float | Final quiz score (0-100) — main outcome variable |
| course_completed | int | Binary: 1 = completed, 0 = not completed |

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Data generation | Python, Faker |
| Storage | CSV, SQLite |
| Processing | Pandas, NumPy |
| Statistical analysis | SciPy, Statsmodels |
| Machine learning | scikit-learn |
| Visualisation | Seaborn, Matplotlib, Plotly |
| Dashboard | Streamlit |
| Version control | Git, GitHub |

---

## Progress Tracker

- [x] Week 1, Day 1 — Project scaffold, README, dataset generation
- [ ] Week 1, Day 2 — Data cleaning, SQLite setup, EDA start
- [ ] Week 1, Day 3 — Full EDA, feature engineering
- [ ] Week 1, Day 4 — Hypothesis testing, correlation analysis
- [ ] Week 1, Day 5 — OLS baseline, review prep
- [ ] Week 2 — Full inference + predictive modelling
- [ ] Week 3 — Streamlit dashboard
- [ ] Week 4 — Final polish + submission

---

## How to Run

```bash
git clone https://github.com/mallya-m/e-learning-usage-statistical-analysis.git
cd e-learning-usage-statistical-analysis
pip install -r requirements.txt
jupyter notebook
```

---

*Department of Computer Science and Engineering | 2025-26*