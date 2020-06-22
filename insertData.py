import psycopg2
import pdf

try:
    conn = psycopg2.connect("postgres://tmxeeauqfrlstr:1518f47c30734fc27d98f98dc6eb598af9d770e903129ebf42da6dbf483bfed7@ec2-52-20-248-222.compute-1.amazonaws.com:5432/d12i5f8utg6508")
except:
    print("I am unable to connect to the database")

conn.set_client_encoding('UTF8')

cur = conn.cursor()
jobs = pdf.main()

for i in range(len(jobs)):
    cur.execute(
        "INSERT INTO job_title (position) "
        "VALUES (%s)",
        (jobs[i],))

conn.commit()
cur.close()
conn.close()


