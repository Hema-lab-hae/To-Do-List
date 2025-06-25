# 📝 To-Do List (Python Console App)

A simple console-based To-Do List application built with **Python**. 
This project allows users to **view**, **add**, and **remove** tasks interactively from the terminal.

🔷 Objective
The primary objective of this project is to build a simple command-line based To-Do List application using Python. It allows users to:
Add new tasks
View existing tasks
Remove completed or unwanted tasks

This project demonstrates the use of basic Python concepts, including:
Lists
Loops
Functions
User input handling

🔷 Tools & Technologies Used
Tool/Technology	Purpose
Python 3.x	Core programming language
VS Code	Code editor (for development)
Git & GitHub	Version control and hosting (optional)

🔷 Working of the Application
When the application is run, it displays a menu:

pgsql
Copy
Edit
--- TO-DO LIST MENU ---
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
Choose an option (1-4):
🔹 Features:
View Tasks
Lists all current tasks in numbered order.
If no tasks exist, a message is displayed.

Add Task
Prompts the user to enter a task description.
Adds the new task to the list.
Remove Task

Displays the list of tasks with numbers.
User can enter the task number to remove it from the list.
Exit
Terminates the program.

🔹 Program Flow:
The menu is displayed in a loop.
The user makes a choice (1–4).
Appropriate functions are called for each choice.
The loop continues until the user selects option 4 to exit.

🔷 Code Structure
Functions used:
show_menu() – Displays the main menu
view_tasks() – Shows all current tasks
add_task() – Adds a new task to the list
remove_task() – Removes a task by its number

Data structure:
A simple Python list named tasks[] is used to store all task entries.

🔷 Sample Code Snippet
python
Copy
Edit
tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
 
🔷 Conclusion
This project provides a practical introduction to basic Python programming, especially how to use lists, functions, and input/output in a real-world use case.
While simple, it lays the foundation for more advanced features such as:
Saving tasks to a file
Loading tasks from a file
Building a GUI using Tkinter or PyQt

🔷 Future Improvements
Save tasks to a file (e.g., .txt or .json)
Add a task due date or priority
Create a GUI interface
Store data in a SQLite database
