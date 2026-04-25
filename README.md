# TO-DO-App

## To-Do List CLI Application

A simple command-line To-Do List application written in Python. This project allows users to manage daily tasks efficiently by adding, viewing, deleting, and marking tasks as completed. Tasks are stored locally using file serialization.

## Features

* Add new tasks
* View all tasks
* Delete tasks
* Mark tasks as completed
* Persistent storage using `pickle`
* Easy-to-use command-line interface

## Technologies Used

* Python 3
* Built-in modules :
  * `pickle` (for data storage)
  * `os` (for file handling)

## Project Structure

```
.
├── tasks.pkl        # Stores saved tasks (auto-created)
├── TO-DO-App.py          # Main application file
└── README.md        # Project documentation
```

## How to Run

1. Clone the repository :

   ```bash
   git clone https://github.com/your-username/TO-DO-App.py.git
   cd TO-DO-App.py
   ```

2. Run the script :

   ```bash
   python TO-DO-App.py
   ```

## Usage
Once the program starts, you'll see a menu :

```
--- To-Do List ---
1. View tasks
2. Add task
3. Delete task
4. Mark task as completed
5. Exit
```

* Enter the corresponding number to perform an action.
* Follow the prompts to manage your tasks.

## Data Storage

* Tasks are saved in a file named `tasks.pkl`.
* The file is automatically created when you add your first task.
* Data persists between program runs.

## Notes
* Do not manually edit the `tasks.pkl` file, as it is stored in binary format.
* Ensure Python is installed on your system before running the application.

## Future Improvements
* Add task deadlines and priorities
* Implement task editing feature
* Add GUI version
* Export tasks to text or CSV
* Improve error handling and validation

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.

## License
This project is open-source and available under the MIT License.

## Author
