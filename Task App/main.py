from task import *

def printrow(sno,taskname,status):
    print('|','%3s'%sno,'|','%-20s'%taskname,'|','%-11s'%status,'|')
    
construct()
while True:
    print("""1. New Task
2. Set Done
3. Show Tasks
4. Delete Task""")
    choice = input("Choice: ")
    if choice == '1':
        taskname = input("Enter Task Name: ")
        Task(taskname,"Not Done")
    elif choice == '2':
        id = int(input("Enter Task Id: "))
        TaskList[id-1].setstatus("Done")
    elif choice == '3':
        print(('_'*44))
        printrow("Sno","Task Name","Status")
        print(('⎻'*44))
        for row in TaskList : printrow(TaskList.index(row)+1,row.taskname,row.status)
        print(('⎻'*44))
    elif choice == '4':
        id = input("Enter Task Id: ")
        del TaskList[int(id)-1]
    else:
        deconstruct()
        break
    
