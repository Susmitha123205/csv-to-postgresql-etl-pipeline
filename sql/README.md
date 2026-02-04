# CSV to PostgreSQL ETL Pipeline (Python)

from pypandoc import convert_text

readme = """
# CSV to PostgreSQL ETL Pipeline (Python)

## 📌 Project Overview
This project demonstrates a complete **end-to-end ETL (Extract, Transform, Load) pipeline** built using **Python, Pandas, and PostgreSQL**.  
It reads raw sales data from a CSV file, processes and cleans the data, and loads it into a PostgreSQL database for analysis.

This project is designed for **beginners in Data Engineering** and reflects real-world workflows.

---

## 🎯 Project Goal
- Extract raw sales data from a CSV file
- Transform the data into a clean, analytics-ready format
- Load the processed data into a PostgreSQL database
- Validate the loaded data using SQL

---

## 🏗️ Architecture

CSV File  
↓  
Extract (Pandas)  
↓  
Transform (Data Cleaning & Calculations)  
↓  
Load (PostgreSQL using psycopg2)  
↓  
Sales Table in Database

---

## 📂 Project Structure
data-engineering-etl-project/
│
├── data/
│ └── raw_sales.csv
│
├── etl/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── main.py
│
├── sql/
│
└── README.md

---

## 🛠️ Tools & Technologies

- Python 3
- Pandas
- PostgreSQL
- psycopg2
- pgAdmin 4
- VS Code
- Windows OS

---

## 🔄 ETL Process Explained

### 1️⃣ Extract
- Reads data from `raw_sales.csv`
- Uses Pandas `read_csv()`
- Loads data into a DataFrame

### 2️⃣ Transform
- Removes invalid or missing records
- Converts data types
- Creates a derived column:
  - `total_price = price * quantity`

### 3️⃣ Load
- Connects Python to PostgreSQL using psycopg2
- Inserts transformed data into the `sales` table
- Commits the transaction safely

### 4️⃣ Orchestration
- `main.py` controls the full ETL flow:
  - Extract → Transform → Load
  - Prints success message after execution

---

## 🗄️ Database Schema

**Table Name:** `sales`

| Column Name  | Data Type |
|-------------|-----------|
| order_id    | INT |
| customer    | VARCHAR(50) |
| product     | VARCHAR(50) |
| price       | INT |
| quantity    | INT |
| order_date  | DATE |
| total_price | INT |

---

## ▶️ How to Run the Project

### 1. Install Python Libraries
pip install pandas psycopg2

### 2. Start PostgreSQL
- Port: 5432
- Database: postgres

### 3. Create Table (pgAdmin)
CREATE TABLE sales (
order_id INT,
customer VARCHAR(50),
product VARCHAR(50),
price INT,
quantity INT,
order_date DATE,
total_price INT
);

### 4. Run ETL Pipeline
cd etl
python main.py

---

## ✅ Expected Output
ETL Pipeline executed successfully
## Verify:
SELECT * FROM sales;

---

## 📘 Key Learnings

- Built a real ETL pipeline from scratch
- Integrated Python with PostgreSQL
- Handled file paths and database connections
- Validated data using SQL
- Understood real-world ETL debugging

---

## 🧾 Resume Description

Built an end-to-end ETL pipeline using Python, Pandas, and PostgreSQL to extract CSV sales data, perform data transformations, and load it into a relational database for analytics.

---

## 🚀 Future Improvements

- Add logging
- Use environment variables for credentials
- Handle duplicate records
- Automate pipeline execution
- Integrate with Apache Airflow

