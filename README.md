# Employee Management System

A desktop employee management system developed with Python and Tkinter.

## Description

This project is an employee management system written in Python with a graphical user interface built using Tkinter.

The application provides separate panels for administrators and employees. Administrators can manage employee accounts, monitor attendance records, and communicate with employees through the system. Employees can log in to their own accounts, view messages from the administrator, and mark their attendance.

## Features

### Administrator Features

* Login using administrator credentials
* Register new employees
* Change administrator username and password
* View employee attendance status
* Send messages to employees
* Manage employee information

### Employee Features

* Login using credentials assigned by the administrator
* View messages sent by the administrator
* Mark attendance status
* Access personal employee panel

## Default Administrator Account

For the demonstration version of the application:

* Username: `admin`
* Password: `1234`

After logging in, the administrator can change these credentials through the system settings.

## Technologies Used

* Python
* Tkinter
* Pickle

## Project Structure

```text
Employee-Management-System/
│
├── main.py
└── README.md
```

The application automatically creates the required data files (`admin.txt` and `workers.txt`) during the first run if they do not already exist.

## How to Run

1. Install Python 3.
2. Download or clone the repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

## Author

**Misagh Shariati**

Created as a personal learning project using Python and Tkinter.

