Task Tracker CLI
A simple command-line interface (CLI) tool to manage your tasks, track progress, and ensure data persistence using a JSON backend.
🚀 Features
Add Tasks: Create new tasks with a description.
List Tasks: View all tasks or filter them by status (todo, in-progress, done).
Data Persistence: All tasks are automatically saved to a tasks.json file using Python's json module and context managers.
Automatic ID Generation: Each task is assigned a unique, incrementing ID.
Timestamps: Automatically tracks when tasks are createdAt and updatedAt.
🛠️ Installation
Ensure you have Python 3.x installed.
Clone this repository or download the taskCLI.py file.
No external libraries are required (uses standard library only).
📖 Usage
Run the script from your terminal using the following commands:
Add a New Task
bash
python taskCLI.py add "Buy groceries"
Use code with caution.

List All Tasks
bash
python taskCLI.py list
Use code with caution.

List Tasks by Status
bash
python taskCLI.py list done
python taskCLI.py list in-progress
python taskCLI.py list todo
Use code with caution.

Update or Delete (Future Commands)
bash
python taskCLI.py update <id> "New Description"
python taskCLI.py delete <id>
Use code with caution.

📂 Project Structure
taskCLI.py: The main script containing the CLI logic and task management functions.
tasks.json: (Auto-generated) The persistent storage file where your tasks are kept.
🧠 Concepts Learned
Data Persistence: Saving data to non-volatile storage.
Context Managers: Using the with statement for safe file handling.
CLI Arguments: Using sys.argv to capture user input from the terminal.
JSON Serialization: Converting Python dictionaries into a readable file format.
