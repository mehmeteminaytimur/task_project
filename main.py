class User():
     
    def __init__(self, username, password):
        self.username = username
        self.password = password
     
    def Login(self):
        while True:    
            try:
                usernameInput = input("Enter your username: ").strip()
                passwordInput = input("Enter your password: ").strip()
                
                if (usernameInput, passwordInput) == (self.username, self.password):
                    print("Logged in successfully!")
                    break
                else:
                    raise ValueError("Username or password is wrong. Please try again.")
            except ValueError as e:
                print(f"An error occured: {e}")
  
class Task(User):
    
    def __init__(self, username, password):
        super().__init__(username, password)
        self.taskList = []

    def createTask(self):
        while True:
            try:
                numberOfTasks = int(input("Enter number of tasks that you will create: ")) 
                break
            except ValueError:
                print("Please enter a valid number.")
            
        while numberOfTasks > 0:
            createNewTask = input("Create a new task: ")
            numberOfTasks -= 1
            self.taskList.append(createNewTask)
        print(self.taskList)
    
    def removeTask(self):
        if not self.taskList:
            print("There is no task to be removed.")
            return
          
        while True:
            try:    
                print(f"Here is the current list >>> {self.taskList}")
                removeTaskInput = input("Please enter name of task correctly that you want to remove it: ")
            
                if removeTaskInput in self.taskList:
                    self.taskList.remove(removeTaskInput)
                    print(f"{removeTaskInput} task deleted.")
                    break
                else:
                    print("Task not found.")
                    
            except ValueError:
                print("Enter name of the task correctly.")
                    
    def updateTask(self):
        """
        Which tasks do you want to update?(1,2,3 or ..7,8...) 
        Enter index number of tasks which you want to update.
        """
        
        while True:
            try:    
                if self.taskList:
                    updateRequestNumber = int(input("How many task will you update?: "))
                    if updateRequestNumber <= 0:                                        
 
                        raise ValueError("The number of task updates must be positive.")          
                    if updateRequestNumber > len(self.taskList):
                        raise ValueError("The number of task updates must be equal to or less than the number of task list elements.")
                    break
                else:
                    print("There is no task to be updated.")
                    return
                   
            except ValueError as e:
                print(f"An error occured: {e}")
        
        while updateRequestNumber > 0:
            try:    
                updateRequest = int(input("Enter a index number: "))    
                
                if 0 <= updateRequest < len(self.taskList):
                    task_to_remove = self.taskList.pop(updateRequest)
                    print(f"The {task_to_remove} task has been deleted.")
            
                    print("""
                    If you want to add a new task, enter 'yes'. If not, enter 'no'.
                    """)
                    while True:
                        updateSuggestion = input("Do you want to add a new task? (yes/no): ")
                        
                        if updateSuggestion.lower() == "yes":
                            new_Task = input("Enter a new task: ")
                            self.taskList.insert(updateRequest, new_Task)
                            break
                        elif updateSuggestion.lower() == "no":
                            print("No new task was added.")
                            break
                        
                        else:
                            print("Invalid choice! Please enter 'yes' or 'no'.")

                    updateRequestNumber -= 1
                    print(f"Remaining updates: {updateRequestNumber}")
                    print(f"Current task list: {self.taskList}")
                
                else:
                    print("Invalid index number! Enter a valid index number.")
            
            except ValueError:
                print("Enter a valid number.")                    
                
        if updateRequestNumber == 0:
            print("All updates have been completed.")
            
    def showTaskList(self):
        if self.taskList:
            print(f"Here is the current task list >>> {self.taskList}")
        else:
            print("There is no task yet.")

    def choices(self):
        self.Login()
        
        print("""
        Choices: 
        1 - CREATE NEW TASK
        2 - REMOVE CURRENT TASK
        3 - SHOW TASK LIST
        4 - UPDATE CURRENT TASK
        """)
       
        while True:   
            choice = input("Please choose a process (1,2,3,4) or enter 'q' to quit: ").strip().lower()
        
            if choice == "1":
                self.createTask()        
                
            elif choice == "2":
                self.removeTask()
            
            elif choice == "3":    
                self.showTaskList()
            
            elif choice == "4":
                self.updateTask()
                
            elif choice == "q":
                break
            
            else:
                print("Invalid choice. Please enter 1,2,3,4 or 'q' .")
        
taskExecuter = Task("user1", "123456789")
taskExecuter.choices()