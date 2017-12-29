import psycopg2

class Student:
    def __init__(self, major, classes):
        self.major = major
        self.classes = classes

    def __str__(self):
        return self.major + " Major. Classes Taken = " + ', '.join(self.classes)


#Queries the database for the ID and major of each student
def getStudents(cur):
    sql = "SELECT pidm,admit_major_desc FROM students WHERE admit_major_desc IS NOT NULL LIMIT 1000"

    cur.execute(sql)
    rows = cur.fetchall()

    students = {}
    for row in rows:
        pidm = row[0]
        major = row[1]
        student = Student(major, getClasses(pidm))
        students[pidm] = student

    return students

#Queries the database for every class that a student with a certain ID has taken and returns each of them in an array
def getClasses(pidm):
    sql = "SELECT subj,crse FROM courses WHERE reg_status_desc='Registered' AND pidm=" + str(pidm)
    try:
        cur.execute(sql)
    except:
        print("INVALID QUERY")
    courses = cur.fetchall()
    classes = []
    for course in courses:
        name = " ".join(course)
        classes.append(name)
    return classes

#Connect to the database and execute queries
if __name__ == "__main__":
    conn = psycopg2.connect("dbname='kys_development' user='Sergei' host='localhost' password=''")
    cur = conn.cursor()
    students = getStudents(cur)
    for i in students:
        print(students[i])
