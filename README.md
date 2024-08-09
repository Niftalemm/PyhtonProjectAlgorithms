## TaskBook - A Simple Task Reminder Program

### Overview

TaskBook is a Python-based console application designed to help you manage daily reminders. With this program, you can easily add, display, edit, and remove reminders. It calculates the time left for each task and alerts you if the deadline has passed. The program operates through a simple text-based menu, making it easy to navigate and use.

### Features

- **Add a Reminder:** Create reminders with a specific task and time (24-hour format).
- **Display Reminders:** View all your reminders along with the time left to complete each task.
- **Edit a Reminder:** Modify existing reminders by changing the task name or time.
- **Remove a Reminder:** Delete a reminder from your list when it's no longer needed.
- **Calculate Time Left:** Automatically calculates and displays how much time is left for each task.
- **User-Friendly Interface:** A simple menu-driven interface that is easy to use.

### Usage

1. **Run the Program:**
   - Execute the script to start the program.
   - You will be prompted to enter the name of your To-Do list.

2. **Main Menu:**
   - The main menu presents five options:
     1. **Add a Reminder** - Add a new reminder with a task and time.
     2. **Display Reminders** - Display all reminders and the time left for each.
     3. **Remove a Reminder** - Remove an existing reminder.
     4. **Edit a Reminder** - Edit the details of an existing reminder.
     5. **Exit** - Exit the program.

3. **Adding a Reminder:**
   - Enter the reminder text in the format "Task at HH:MM".
   - The reminder is then stored and a confirmation message is displayed.

4. **Displaying Reminders:**
   - All reminders will be listed with their associated times.
   - The program will also calculate and display the time left for each task.

5. **Editing a Reminder:**
   - Choose the reminder you want to edit.
   - Provide the new task name and time.
   - The reminder is updated, and a confirmation message is shown.

6. **Removing a Reminder:**
   - Select the reminder you wish to delete.
   - The program removes the reminder and displays a confirmation message.

7. **Exiting the Program:**
   - Choose the "Exit" option from the main menu to terminate the program.

8. **Returning to the Main Menu:**
   - After completing an action, you can choose to return to the main menu or exit the program.

### Example

```python
# Sample interaction with the program

WELCOME 
Please enter the name of the To Do list: Daily Tasks
Welcome to the Daily Reminders Program!

Choose an option for your Task List, Daily Tasks :
1. Add a Reminder
2. Display Reminders
3. Remove a Reminder
4. Edit a Reminder
5. Exit

Enter the number of your choice: 1
Enter the reminder text. Eg: Meeting at 23:00: Study session at 15:00
The task Study session, to be done at 15:00, has been added.

Do you want to go back to the main menu? (y/n): y

# After adding several reminders, you can display them:

Choose an option for your Task List, Daily Tasks :
1. Add a Reminder
2. Display Reminders
3. Remove a Reminder
4. Edit a Reminder
5. Exit

Enter the number of your choice: 2
Reminders:
Study session at 15:00.
You have 2 hours left for: Study session

Do you want to go back to the main menu? (y/n): y
```

### Installation

To run this program, you need Python installed on your system. No additional libraries are required.

### Running the Program

1. Save the script as `taskbook.py`.
2. Run the script using the command:

   ```bash
   python taskbook.py
   ```

3. Follow the prompts to manage your reminders.

### Contributions

Feel free to contribute to this project by forking the repository and submitting pull requests. Suggestions for improvement are always welcome.

### License

This project is open-source and available under the MIT License.
