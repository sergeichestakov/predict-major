import psycopg2
import tensorflow as tf
import numpy as np

#Queries the database for the ID and major of each student
def getStudents(cur):
    sql = "SELECT pidm,admit_major_desc FROM students WHERE admit_major_desc IS NOT NULL LIMIT 1000"

    cur.execute(sql)
    rows = cur.fetchall()

    majors = []
    classes = []

    students = {}
    for row in rows:
        pidm = row[0]
        major = row[1]
        majors.append(major)
        classes.append(getClasses(pidm))

    return majors, classes

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

#Trains the data
def trainData(majors, classes):
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": np.array(classes)},
    y=np.array(majors),
    num_epochs=None,
    shuffle=True)

#Connect to the database and execute queries
if __name__ == "__main__":
    conn = psycopg2.connect("dbname='kys_development' user='Sergei' host='localhost' password=''")
    cur = conn.cursor()
    majors, classes = getStudents(cur)
    trainData(majors, classes)
