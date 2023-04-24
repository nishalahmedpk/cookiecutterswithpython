import mysql.connector as sql

connector = sql.connect(host="localhost",user="root",password="1234567890",database="project")
cursor = connector.cursor()
cursor.execute("Create table if not exists tasks(sno int primary key auto_increment, task varchar(20) not null unique,status varchar(10) not null)") ; cursor.close()
connector.commit()

TaskList = []

class Task:

    id = 1
    def __init__(self,taskname,status):
        self.sno = Task.id
        self.taskname = taskname
        self.status = (status)
        Task.id += 1
        TaskList.append(self)

    def setstatus(self,status):
        self.status = (status)

    def __delattr__(self):
        pass
def deconstruct():
    cursor = connector.cursor()
    cursor.execute("truncate table tasks")
    for row in TaskList : cursor.execute("Insert into tasks(task,status) values('{}','{}')".format(row.taskname,row.status))
    connector.commit() ; cursor.close()

def construct():
    cursor = connector.cursor()
    cursor.execute("Select * from tasks")
    List = cursor.fetchall()
    for tuple in List:
        Task(tuple[1],tuple[2])
