"""
This program uses sql database to store tasks and retrieve task based on the initail mapping of the words.
it should handle most of the errors without abruptly stopping.

"""


import mysql.connector as mysql;
import datetime
import tabulate

class function_of_ToDoList:
    
    def create(self):
        task = input("Enter the task: ")
        dead_Line = input("Enter the deadline \" formate should be yyyy-mm-dd \" : ")
        
        curr_date = datetime.datetime.now()
        try:
            cursor.execute("INSERT INTO  todolist VALUES (%s, %s, %s);",(task, curr_date, dead_Line))
            mycon.commit()
        except Exception as e:
            print("An Error Occured: ",e)

    def read(self):
        cursor.execute("SELECT * FROM todolist")
        self.data = cursor.fetchall()
        headers = ["Task", "Modified_Date", "DeadLine"]
        print(tabulate.tabulate(self.data, headers = headers, tablefmt = "grid"))

    def update(self):
        self.read()
        taskName = input("Enter the few words of task or whole task which you want to update: ")
        taskExist = False
        for line in self.data:
            index = line[0].find(taskName)

            if index != -1:
                taskExist = True
                break

        if taskExist:
            task = input("Enter the new task: ")
            deadLine = input("Enter the new deadline \" formate should be yyyy-mm-dd \" : ")
            curr_date = datetime.datetime.now()

            try:
                cursor.execute("UPDATE todolist set Task = %s, Modified_Date = %s, DeadLine = %s WHERE Task like %s;",(task, curr_date, deadLine,"%"+taskName+"%"))
                mycon.commit()
                print("Updated Successfully...")
            except Exception as e:
                print("An Error Occured: ",e)
        else:
            print("Task not Found")

    def delete(self):
        self.read()
        taskName = input("Enter the few words of task or whole task which you want to delete: ")
        taskExist = False
        
        for line in self.data:
            index = line[0].find(taskName)

            if index != -1:
                taskExist = True
                break

        if taskExist:
            cursor.execute("DELETE FROM todolist WHERE Task LIKE %s;",("%"+taskName+"%",))
            mycon.commit()
            print("Deleted Successfully...")
        else:
            print("Task not Found")



#_main_    
print("__________Input the login information__________\n")
usr = input("Enter the user name: ")
passwrd = input("Enter the password: ")
try:
    mycon = mysql.connect(host = 'localhost', user = usr, password = passwrd, database = 'todolist', auth_plugin="mysql_native_password")

except Exception as e:
    print("You enter the wrong Username or Password")
    exit(0)
    
if (mycon.is_connected()):
    print("\n__________Signed in Successfully_________")
    
cursor = mycon.cursor()
obj = function_of_ToDoList()
while True:
    print("1. Add Task 2. Read Task 3. Update Task 4. Delete Task 5. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("__________ Adding Task __________")
        obj.create()

    elif ch == 2:
        print("__________ Reading Task __________")
        obj.read()

    elif ch == 3:
        print("__________ Updating Task __________")
        obj.update()

    elif ch == 4:
        print("__________ Deleting Task __________")
        obj.delete()

    elif ch == 5:
        print("__________Exiting__________")
        break

    else:
        print("__________Invalid Choice__________")
    
    print()
mycon.close()