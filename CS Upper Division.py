# Niftalem Kassa
# Project for Upper division Program

from datetime import datetime


class TaskBook:
    def __init__(self, name):
        self.reminders = {}  # Dictionary to store reminders, that will be accessed all over.

        self.reminder = None  # Variables to store individual reminder and its time
        self.time_reminder = None

        self.name = name  # Name of the ToDoList
        now = datetime.now()
        self.time = now.strftime("%H:%M")  # Formats the present time

    def TimeNow(self):
        print(self.time)

    def AddaReminder(self, reminder):
        reminder_list = reminder.split(' at ') # Split the reminder text into task and time components

        task, self.time_reminder = map(str.strip, reminder_list) # Extract task and time, and update instance variables

        output_dict = {task: self.time_reminder}  # Create a dictionary entry for the reminder and update reminders dictionary
        self.reminders.update(output_dict)

        # Display a message indicating the task has been added
        print(f'The task {task}, to be done at {self.time_reminder}, has been added.\n')

    def Calculate_Time(self, task):
        if task in self.reminders: # Check if the specified task exists in reminders

            time_int_of_reminder = int(self.reminders[task].replace(":", "")) # Convert reminder time and current time to integers for comparison
            time_int_of_currentTime = int(self.time.replace(":", ""))

            diff = (time_int_of_reminder - time_int_of_currentTime)  # Calculate the time difference

            if diff > 0: # Display time left or a messaxge indicating the deadline has passed
                print(f'You have {diff // 100} hours left for: {task}')
            else:
                print("The Deadline has passed sadly")
        else:
            print(f'Task "{task}" not found in reminders.')

    def DisplayReminder(self):
        if self.reminders:  # Check if there are any reminders to display
            print("Reminders:")

            for task, time_reminder in self.reminders.items(): #Iterate through reminders and display each task with its time
                print(f"{task} at {time_reminder}.")

                self.Calculate_Time(task) # Calculate and display the time left for each task

        else:
            print("No reminders to be Displayed.")  # Display a message if there are no reminders to be displayed

    def RemoveReminder(self):
        if self.reminders:
            for task, time_reminder in self.reminders.items(): # Display a list of reminders for user reference
                print(f" {task} at {time_reminder}.")

                # Prompt the user to choose which task to delete
            remove_this = input("Choose which task you would like to delete by entering the task name:\n")

            if remove_this in self.reminders: # Check if the chosen task exists in reminders
                print(f'Your task {remove_this} to be done at {self.reminders[remove_this]} has been deleted.')

                # Remove the chosen task from reminders
                del self.reminders[remove_this]

        else:  # Display a message if there are no reminders to be deleted
            print('You currently dont have any reminders right now to be deleted.')

    def EditReminder(self):
        # Check if there are any reminders to edit
        if self.reminders:
            for task, time_reminder in self.reminders.items():# Display a list of reminders for user reference
                print(f" {task} at {time_reminder}.")

            edit_this = input("Choose which task you would like to edit by entering the task name:\n") # Prompt the user to choose which task to edit

            # Prompt the user for the new task name and time
            new_task = input("What task would you want to. Enter the task name:\n")
            new_time = (input("Choose what time to do it. Do it in 24-hr format Eg: 03:00:\n"))

            # Check if the chosen task exists in reminders
            if edit_this in self.reminders:
                print(f'Your task {edit_this} has been changed to {new_task}, to be done at {new_time}')

                # Updating the value of an existing key
                self.reminders[new_task] = new_time

        else:
            # Display a message if there are no reminders to be edited
            print('You currently dont have any reminders right now to be edited.')


if __name__ == "__main__":

    # Get the name of the To-Do list from user input
    name = input("WELCOME \n Please enter the name of the To Do list:")

    # Create an instance of TaskBook with the entered name
    reminders_program = TaskBook(name)

    print("Welcome to the Daily Reminders Program!")

    while True:
        # Display the main menu for the Task List
        print("\nChoose an option for your Task List,",name, ":")
        print("1. Add a Reminder")
        print("2. Display Reminders")
        print("3. Remove a Reminder")
        print("4. Edit a Reminder")
        print("5. Exit")

        # Get user's choice
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            reminder_text = input("Enter the reminder text. Eg: Meeting at 23:00: ")
            reminders_program.AddaReminder(reminder_text)
        elif choice == '2':
            reminders_program.DisplayReminder()
        elif choice == '3':
            reminders_program.RemoveReminder()
        elif choice == '4':
            reminders_program.EditReminder()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please enter a number between 1 and 5.")

        # Add an option to go back to the main menu
        go_back = input("Do you want to go back to the main menu? (y/n): ")
        if go_back.lower() != 'y':
            print("Goodbye!")
            break
