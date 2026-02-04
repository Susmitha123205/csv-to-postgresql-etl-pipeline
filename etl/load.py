import psycopg2

def load_to_db(df):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO sales VALUES (%s,%s,%s,%s,%s,%s,%s)",
            tuple(row)
        )

    conn.commit()
    cur.close()
    conn.close()
