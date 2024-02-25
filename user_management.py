import getpass


class UserManagement:
    def __init__(self):
        """
        Initialize the EventScheduler class.

        Attributes:
        - users (dict): Dictionary to store user information.
        - events (dict): Dictionary to store event information.
        - logged_user (str): Username of the logged-in user.
        - is_admin_logged_user (bool): Admin status of the logged-in user.
        """
        self.users = {'juan': {'password': '1', 'is_admin': True},
                      'maria': {'password': '2', 'is_admin': False},
                      'pedro': {'password': '3', 'is_admin': False}}
        self.events = {}
        self.logged_user = None
        self.is_admin_logged_user = None
    
    def check_user(self):
        """
        Check if the user exists in the database and handle user login or account creation.

        Returns:
        tuple: Tuple containing the logged-in username and admin status if successful, otherwise returns True.

        This method prompts the user to log in or create an account and handles the respective actions.
        """
        newuser = input("Do you want to log in? (Yes/No): ").strip()
        if newuser.lower() == 'yes':
            username = input("Enter username: ").strip()
            if username in self.users:
                
                self.logged_user = username
                self.is_admin_logged_user = self.users[username]['is_admin']
                self.log_in(username)
                return self.logged_user, self.is_admin_logged_user
            else:
                createaccount = input("User not found. Do you want to create an account? (Yes/No): ")
                if createaccount.lower() == 'yes':
                    self.create_account(username)
                else:
                    print("Exiting...")
                    return True
        else:
            print("Create an account ")
            username = input("Enter username: ").strip()
            self.create_account(username)

        
    def log_in(self, username):
        """
        Log in to an existing user.

        Parameters:
        - username (str): Username of the user attempting to log in.

        Returns:
        None

        This method prompts the user for a password and logs them in if the password is correct.
        """
        password = getpass.getpass("Enter password: ")
        if password == self.users[username]['password']:
            print(f"Logged in as {username} {'(Admin)' if self.users[username]['is_admin'] else '(Member)'}.")
            self.logged_user = username
            self.print_user_menu(username)
            
        else:
            print("Incorrect password. Please try again.")
            self.log_in(username)

        
    def create_account(self,username):
        """
        Create a new user account.

        Parameters:
        - username (str): Username of the user to be created.

        Returns:
        None

        This method prompts the user for a password and creates a new user account.
        """
        if username:
            if username in self.users:
                print(f"User '{username}' already exists.")
                self.log_in(username)
            else:
                self.users[username] = {}
                
                password = getpass.getpass(f"Enter password for user '{username}': ")
                self.users[username]['password'] = password
                self.users[username]['is_admin'] = False
                print(f"User '{username}' added successfully.")
                self.log_in(username)
        else:
            print("Usage: add_user <username>")
            
    def get_logged_user(self):
        """
        Get the username of the currently logged-in user.

        Returns:
        str: Username of the logged-in user.
        """
        username = self.logged_user
        return username
    def print_user_menu(self,username):
        """
        Print the menu options based on user roles (admin or member).

        Parameters:
        - username (str): Username of the logged-in user.

        Returns:
        None

        This method prints the menu options available to the user based on their admin status.
        """
        if self.users[username]['is_admin']:
            message_admin = """
            1. Add new user : add_user <username>
            2. View all users : view_users
            3. Create event : create_event <event_name> <description> <start time YY-MM-DD %H:%M> <duration "HH:MM"> <reminder_time_minutes>
            4. View events : view_my_events
            5. Share event : share_event <event_id> <username_to_share> <permission>
            6. Update event : update_event <event_id> <field_to_update> <new_value>
            7. Delete event : delete_event <event_id>
            8. Log out: log_out
            """
            print(message_admin)
        else: 
            message_member = """
            3. Create event : create_event <event_name> <description> <start time YY-MM-DD %H:%M> <duration "HH:MM"> <reminder_time_minutes>
            4. View events : view_my_events
            5. Share event : share_event <event_id> <username_to_share> <permission>
            6. Update event : update_event <event_id> <field_to_update> <new_value>
            7. Delete event : delete_event <event_id>
            8. Log out: log_out
            """
            print(message_member)