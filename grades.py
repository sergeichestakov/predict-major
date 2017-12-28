import psycopg2

#Queries the database for the id and major of each student
def getStudents(cur):
    sql = "SELECT pidm,admit_major_desc FROM students WHERE admit_major_desc IS NOT NULL LIMIT 100"

    cur.execute(sql)
    rows = cur.fetchall()

    for row in rows:
        pidm = row[0]
        major = row[1]
        print("pidm: ", row[0], "major: ", row[1])
        classes = getClasses(pidm)
        print('Classes: ', classes)

#Queries the database for every class that a student with a certain Id has taken and returns each of them in an array
def getClasses(pidm):
    sql = "SELECT subj,crse FROM courses WHERE reg_status_desc='Registered' AND pidm=" + str(pidm)
    try:
        cur.execute(sql)
    except:
        print("INVALID QUERY")
    courses = cur.fetchall()
    classes = []
    for course in courses:
        name = course[0] + " " + course[1]
        classes.append(name)
    return classes

#Connect to the database and execute queries
if __name__ == "__main__":
    conn = psycopg2.connect("dbname='kys_development' user='Sergei' host='localhost' password=''")
    cur = conn.cursor()
    getStudents(cur)
