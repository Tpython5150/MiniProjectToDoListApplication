'''
To Do List Project

Introduction
In this project, you will apply your Python programming skills to create a functional To-Do List Application from scratch. The objective of this project is to reinforce your understanding of Python syntax, data types, control structures, functions, and error handling while building a practical and interactive application.

Project Requirements

1. User Interface (UI):
   Create a command-line interface (CLI) for the To-Do List Application.
   Display a welcoming message and a menu with the following options:
        Welcome to the To-Do List App!

        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
2. To-Do List Features:

   Implement the following features for the To-Do List:
   Adding a task with a title (by default “Incomplete”).
   Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
   Marking a task as complete.
   Deleting a task.
   Quitting the application.
   
3. User Interaction:

   Allow users to interact with the application by selecting menu options using input().
   Implement input validation to handle unexpected user input gracefully.
   
4. Error Handling:

   Implement error handling using try, except, else, and finally blocks to handle potential issues.
   
5. Code Organization:

   Organize your code into functions to promote modularity and readability.
   Use meaningful function names with appropriate comments and docstrings for clarity.
   
6. Testing and Debugging:

   Thoroughly test your application to identify and fix any bugs.
   Consider edge cases, such as empty task lists or incorrect user input
   .
7. Documentation:

   Include a README file that explains how to run the application and provides a brief overview of its features.
8.Optional Features (Bonus):

  If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.
  
9.GitHub Repository:

  Create a GitHub repository for your project.
  Commit your code to the repository regularly.
  Include a link to your GitHub repository in your project documentation.

'''

tasks = []

def display_menu():
  
  print("Welcome to the To-Do List App!")
  print("Menu:")
  print("1. Add a task")
  print("2. View task")
  print("3. Mark a task as complete")
  print("4. Delete a task")
  print("5. Quit")
  
def add_tasks():
  title_task =  input("Enter the task: ")
  priority = input("Enter task priority: (high/medium/low): ").lower()
  #Added a priority and color coding here (matplotlib)
  tasks.append({"title_task": title_task, "status": "r", "priority": priority })
  print(f"Task: {title_task} added successfully!")
  
def view_task():
  if not tasks:
    print("No tasks")
  else:
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
      #added color coding here 'r' = red and 'g' = green ((marplotlib))
      status_color = 'r' if task["status"] != "Complete" else 'g'
      print(f"{i}. {task['title_task']} ({task['status']})")
      
def mark_complete():
  view_task()
  try:
    task_i = int(input("Enter the task number to mark as complete: ")) -1
    #added color coding "g" means complete (matpl0tlib)
    tasks[task_i]["status"] = "g"
  except (ValueError, IndexError):
    print(f"Task '{tasks[task_i]['title_task']} marked complete!")
    
def delete_task():
  view_task()
  try:
    task_i = int(input("Enter the number to delete: ")) -1
    deleted_task = tasks.pop(task_i)
    print(f"Task '{deleted_task['title_task']}' deleted successfully!")
  except (ValueError, IndexError):
    print("Invalid input. Please try again!")
    #added a finally to try block
  finally:
    print('Cleanup: Task list updated.')
    
while True:
  display_menu()
  choice = input("\nEnter your choice (1-5): ")
  if choice == "1" :
    add_tasks()
  elif choice == "2":
    view_task()
  elif choice == "3":
    mark_complete()
  elif choice == "4":
    delete_task()
  elif choice == "5":
    print("Thanks for using the To-Do List App! Have a nice day!")
    break
  else:
    print("Invalid choice. Please select a valid option.")