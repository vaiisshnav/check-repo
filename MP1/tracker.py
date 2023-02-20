from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    print("My UCID is ar2565 and today's  date is 18-02-2023")
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")
        print("My UCID is ar2565 and today's  date is 18-02-2023")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    # update lastActivity with the current datetime value
    # set the name, description, and due date (all must be provided)
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    # output a message confirming the new task was added or if the addition was rejected due to missing data
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
   
    #My UCID is ar2565 and today's  date is 18-02-2023
    #in the below code we are giving the values of name,description and due date to a dictionary named task.
    #if all the values are given, this shows a message that the task is added successfully orelse it displays a failure message
    if name and description and due:  #if all the inputs are provided to add a task
      try:
          datetime_obj = str_to_datetime(due)
          task['name'] = name
          task['description'] = description
          task['due'] = str_to_datetime(due)
          task['lastActivity'] = datetime.now()
          tasks.append(task)  #appends the name,description,due date to tasks
          print("My UCID is ar2565 and today's  date is 18-02-2023")
          print(f'Task "{name}" added successfully!')
      except:  #if the data provided is not in a valid format
        print("Please provide a valid datetime format: mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss") 
        print(f'Task "{name}" addition failed!')
        print("My UCID is ar2565 and today's  date is 18-02-2023")
    else:  #if there is any missing data, this statement is printed
      print("task not added succesfully")
      print("My UCID is ar2565 and today's  date is 18-02-2023")
    save()

    

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #My UCID is ar2565 and today's  date is 18-02-2023
    #this code gets the task by index, it checks whether the index is out of bonds.If yes it prints a statement of the same.
    #Otherwise, the code takes the inputs of task name, description and due date.After this, these patameters are passed to update_task()
    try:
      task=tasks[index]
    except IndexError:
      print("Invalid task index.")
      print("My UCID is ar2565 and today's  date is 18-02-2023")
      return
    # these lines show the existing value of each property where the TODOs are marked in the text of the inputs, while taking the inputs from user
    name = input(f"What's the name of this task? ({task['name']}) \n").strip() or task['name']
    desc = input(f"What's a brief description of this task? ({task['description']}) \n").strip() or task['description']
    due = input(f"When is this task due (format: m/d/y H:M:S) ({task['due']}) \n").strip() or task['due']

    #the above inputs are passed to update_task()
    update_task(index, name=name, description=desc, due=due)

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My UCID is ar2565 and today's  date is 18-02-2023 
    # this code finds the task by index. If there is any index out of bonds,it displays the error message.
    # this code takes the values from the previous function process_update() and updates the task if any inputs are provided
    # if inputs are not provided, it displays a print statement regarding the same.It also updates the last activity to the current datetime 
      # Check if index is out of bounds
    if index < 0 or index >= len(tasks):
        print(f"Invalid index. Please enter an index between 0 and {len(tasks) - 1}.")
        return
    # Get the task by index
    task = tasks[index]
    #check if any properties are changed
    if name is None:
      name = task['name']
    if description is None:
      description = task['description']
    if due is None:
      due=task['due']
    
    if task['name'] != name or task['description'] != description or task['due'] != due:
        task['name'] = name
        task['description'] = description
        task['due'] = due
        print(f"Task {name} was updated.")  #task is updated with the latest values
        print("My UCID is ar2565 and today's  date is 18-02-2023")
    else:
        print(f"No changes were made to task {name}.")  #this is printed if no changes were made
        print("My UCID is ar2565 and today's  date is 18-02-2023")
    
    # Update the lastActivity property
    task['lastActivity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    
    # Save the tasks to the file
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not done, record the current datetime as the value
    # if it is done, print a message saying it's already completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My UCID is ar2565 and today's  date is 18-02-2023 
    # this code checks the index out of bonds and finds the task from list by index
    # if the task is already marked done, it displays a print statemetn saying that the task is already marked as done
    # if the task is not marked as done, then this code updates the status to done and prints the statement as "test marked as done"
    try:
        task = tasks[index]
    except IndexError:
        print(f"Invalid index '{index}'. Please provide a valid index.")

        return
    #if the task is alredy marked as done, then this print statement is displayed
    if task["done"]:
        print("Task is already marked as done.")
        print("My UCID is ar2565 and today's  date is 18-02-2023")
        return
    
    task["done"] = True
    task["completed_at"] = datetime.now()  # it records the current datetime
    print("Task marked as done.")
    save()

    

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My UCID is ar2565 and today's  date is 17-02-2023
    # this code check whether there are any index out of bonds and finds task from list
    # it uses the given print statement to display task name,description,last activity,due date and completion status
    task = {}

    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if index < 0 or index >= len(tasks):
        print("task is not found as the Index is invalid")
        
        return
    
    # Get the task by index
    task = tasks[index]
    print("My UCID is ar2565 and today's  date is 18-02-2023")
     # print task information
    print(f"[{'x' if task['done'] else ' '}] Task: {task['name']}\n"
          f"Description: {task['description']}\n"
          f"Last Activity: {task['lastActivity']}\n"
          f"Due: {task['due']}\n"
          f"Completed: {task['done'] if task['done'] else '-'}\n")
    
    
    
   


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My UCID is ar2565 and today's  date is 18-02-2023
    # this code check whether there are any index out of bonds and deletes task from the list
    if index < 0 or index >= len(tasks):
        print(f"Error: index {index} is out of bounds.")

        return
    #deletes the task at index using delete keyword
    del tasks[index]
    print(f"Task at index {index} has been successfully deleted.")
    print("My UCID is ar2565 and today's  date is 18-02-2023")
    #saves the program
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # My UCID is ar2565 and today's  date is 18-02-2023
    # this code takes all the tasks that not marked as done and appends them to the list incomplete_tasks and 
    # prints all the tasks that are not done by calling the function list_tasks()
    _tasks = []
    
    incomplete_tasks=[]
    for task in tasks:
        if not task['done']:
            incomplete_tasks.append(task)
    
    # print the list of incomplete tasks
    list_tasks(incomplete_tasks)


def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    # My UCID is ar2565 and today's  date is 18-02-2023
    #this code creates an empty list overdue_tasks and check whether there are any due tasks which are older than now
    # if yes, it calls the function list_tasks() and print all those overdue tasks  
    _tasks = []
    overdue_tasks = []
    now = datetime.now()
    #checks whether the task is not done and due date is older than now 
    
    for task in tasks:
        if not task['done'] and datetime.strptime(task['due'], '%Y-%m-%d %H:%M:%S') < now:
            overdue_tasks.append(task)
    list_tasks(overdue_tasks) #function call to list_tasks()



def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    # My UCID is ar2565 and today's  date is 17-02-2023
    # this code checks whether the index is out of bonds and gets the task by index.
    # later, it calculates the difference between the due date and current datetime
    #if the task is overdue, it calculates the overdue datetime
    task = {}
    # Check if the index is valid
    if index < 0 or index >= len(tasks):
        print("Invalid index.")
        return

    # Get the due date of the task
    task = tasks[index]
    due_date = task["due"]
    due_date=str_to_datetime(due_date)
    # Calculate the time remaining or overdue
    now = datetime.now()
    time_diff = due_date - now
    print("My UCID is ar2565 and today's  date is 18-02-2023")
    # Check if the task is overdue
    if time_diff.total_seconds() < 0:
        time_diff = now - due_date
        print("Task is overdue by:")
    else:
        print("Time remaining:")
    # Calculate days, hours, minutes, and seconds
    days = time_diff.days
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds % 3600) // 60
    seconds = time_diff.seconds % 60
    # Display the remaining time or overdue time
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            break
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()