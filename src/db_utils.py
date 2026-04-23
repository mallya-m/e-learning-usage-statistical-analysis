"""
db_utils.py - SQLite query helper functions
Author: Nandana Raghunath
Project: Statistical Analysis of E-Learning Platform Usage
"""

import sqlite3
import pandas as pd

DB_PATH = "data/elearning.db"


def get_connection():
    """Return a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)


def load_all():
    """Load the entire students table as a DataFrame."""
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM students", conn)
    conn.close()
    return df


def filter_by_course(course_name):
    """Return all students enrolled in a specific course."""
    conn = get_connection()
    df = pd.read_sql_query(
        "SELECT * FROM students WHERE course = ?",
        conn, params=(course_name,)
    )
    conn.close()
    return df


def filter_by_gender(gender):
    """Return all students of a specific gender."""
    conn = get_connection()
    df = pd.read_sql_query(
        "SELECT * FROM students WHERE gender = ?",
        conn, params=(gender,)
    )
    conn.close()
    return df


def get_completed_students():
    """Return only students who completed their course."""
    conn = get_connection()
    df = pd.read_sql_query(
        "SELECT * FROM students WHERE course_completed = 1", conn
    )
    conn.close()
    return df


def get_avg_score_by_course():
    """Return average quiz score grouped by course."""
    conn = get_connection()
    df = pd.read_sql_query(
        """
        SELECT course,
               ROUND(AVG(quiz_score), 2)      AS avg_quiz_score,
               ROUND(AVG(logins_per_week), 2) AS avg_logins,
               COUNT(*) AS student_count
        FROM students
        GROUP BY course
        ORDER BY avg_quiz_score DESC
        """,
        conn
    )
    conn.close()
    return df


def get_score_range(min_score, max_score):
    """Return students with quiz_score between min and max."""
    conn = get_connection()
    df = pd.read_sql_query(
        "SELECT * FROM students WHERE quiz_score BETWEEN ? AND ?",
        conn, params=(min_score, max_score)
    )
    conn.close()
    return df


if __name__ == "__main__":
    df = load_all()
    print(f"Total students: {len(df)}")
    print(df.head(3))