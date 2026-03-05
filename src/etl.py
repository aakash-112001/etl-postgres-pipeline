import pandas as pd
from sqlalchemy import text
from src.db import get_engine


def extract():
    return pd.read_csv("data/employees.csv")


def transform(df):
    df["salary"] = df["salary"] * 1.1  # 10% increment
    return df


def load(df):
    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) UNIQUE,
                department VARCHAR(50),
                salary FLOAT
            );
        """))

        df.to_sql(
            "employees",
            con=conn,
            if_exists="append",
            index=False,
            method="multi"
        )
