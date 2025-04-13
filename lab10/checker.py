import psycopg2
try:
    conn = psycopg2.connect(
        dbname = "phoneB",
        user = "postgres",
        password = "qwerty178wifi",
        host = "localhost",
        port = "5432"
    )
    print("OK!")
    conn.close()
except Exception as e:
    print(e)