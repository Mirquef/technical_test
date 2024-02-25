Event Scheduler App
===================

The Event Scheduler App is a command-line application built in Python for managing events, providing features for event creation, updating, deletion, and sharing. The app includes background notifications for upcoming events and user role management.

Features
--------

*   **Event Management:** Create, update, delete, and share events.
*   **User Roles:** Admin and Member roles with specific permissions.
*   **Background Notifications:** Receive notifications for upcoming events.
*   **Role Management:** Admins can view all users and promote users to admin.
*   **Custom Views:** The user logged into the app can only see his own events or those shared with him

Getting Started
---------------

### Prerequisites

*   Python 3.11
*   Required libraries: cmd, datetime, getpass, time, threading

### Installation

Clone the repository:

bashCopy code

`git clone https://github.com/Mirquef/technical_test.git`

Navigate to the project directory:

bashCopy code

`cd technical_test`

### Usage

Run the application:

bashCopy code

`python main.py`

To run automated tests:

bashCopy code

`python -m unittest test_project.py`

Usage Instructions
------------------

1.  Log in with an existing account or create a new one.
2.  Access various functionalities based on your user role (Admin or Member).
3.  Manage events, share them, and receive notifications for upcoming events.

Testing
-------

The project includes unit tests using the `unittest` module. Run the tests with:

bashCopy code

`python -m unittest test_project.py`

Contributors
------------

*   \[Juan Mirque\] - \[Mirquef\]


* * *
