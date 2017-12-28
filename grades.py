import psycopg2
import psycopg2.extras

def getStudents(cur):
    sql = "SELECT pidm,admit_major_desc FROM students WHERE admit_major_desc IS NOT NULL LIMIT 100"

    cur.execute(sql)
    rows = cur.fetchall()

    for row in rows:
        pidm = row[0]
        major = row[1]
        print("pidm: ", row[0], "major: ", row[1])
        getClasses(pidm)

def getClasses(pidm):
    sql = "SELECT * FROM courses WHERE pidm=" + str(pidm)
    try:
        cur.execute(sql)
    except:
        print("INVALID QUERY")
    classes = cur.fetchall()
    print("Student's classes: ", classes)


if __name__ == "__main__":
    conn = psycopg2.connect("dbname='kys_development' user='Sergei' host='localhost' password=''")
    cur = conn.cursor()
    getStudents(cur)
