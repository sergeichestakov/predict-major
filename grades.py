import psycopg2
import tensorflow as tf
import numpy as np

#Queries the database for the ID and major of each student
def getStudents(cur):
    sql = "SELECT pidm,admit_major_desc FROM students WHERE admit_major_desc IS NOT NULL LIMIT 500"

    cur.execute(sql)
    rows = cur.fetchall()

    majors = []
    classes = []

    for row in rows:
        pidm = row[0]
        major = row[1]
        #print(tf.string_to_number(major))
        majors.append(tf.string_to_number(major, tf.int32))
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
        #print(tf.string_to_number(name))
        classes.append(tf.string_to_number(name, tf.int32))
    return classes

#Trains the data
def trainData(majors, classes):
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": np.array(classes)},
    y=np.array(majors),
    num_epochs=None,
    shuffle=True)

    feature_columns = [tf.feature_column.numeric_column("x", shape=[4])]

    # Build 3 layer DNN with 10, 20, 10 units respectively.
    classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10, 20, 10],
                                          n_classes=3)
    #Train the model
    classifier.train(input_fn=train_input_fn, steps=2000)


if __name__ == "__main__":
    conn = psycopg2.connect("dbname='kys_development' user='Sergei' host='localhost' password=''")
    cur = conn.cursor()
    majors, classes = getStudents(cur)
    trainData(majors, classes)
