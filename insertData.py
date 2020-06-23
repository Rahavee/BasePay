import psycopg2
import pdf

try:
    conn = psycopg2.connect("postgres://tmxeeauqfrlstr:1518f47c30734fc27d98f98dc6eb598af9d770e903129ebf42da6dbf483bfed7@ec2-52-20-248-222.compute-1.amazonaws.com:5432/d12i5f8utg6508")
except:
    print("I am unable to connect to the database")

conn.set_client_encoding('UTF8')

cur = conn.cursor()
names= pdf.main()

# for i in range(len(jobs)):
#     cur.execute(
#         "INSERT INTO job_title (position) "
#         "VALUES (%s)",
#         (jobs[i],))

for i in range(len(names[0])):
    cur.execute(
        'INSERT INTO names ("first_name", "last_name") '
        'VALUES (%s,%s)',
        (names[0][i], names[1][i])
    )

# for i in range(len(pay)):
#     jobID = 0
#     for j in range(len(jobs)):
#         if jobsList[i]==jobs[j]:
#             jobID= j+1
#     cur.execute(
#         'INSERT INTO salary(user_id, job_id, pay, year)'
#         'VALUES (%s,%s,%s,%s)',
#         (i+1, jobID, pay[i], 2019)
#     )





conn.commit()
cur.close()
conn.close()


