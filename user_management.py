import getpass


class UserManagement:
    def __init__(self):
        self.users = {'juan': {'password': '12345', 'is_admin': True}}
        self.events = {}
        self.logged_user = None
        self.is_admin_logged_user = None
    
    def check_user(self):
        """
        Check if the user exists in our database.
        """
        newuser = input("Do you want to log in? (Yes/No): ").strip()
        if newuser.lower() == 'yes':
            username = input("Enter username: ").strip()
            if username in self.users:
                self.log_in(username)
            else:
                createaccount = input("User not found. Do you want to create an account? (Yes/No): ")
                if createaccount.lower() == 'yes':
                    self.create_account(username)
                else:
                    print("Exiting...")
        else:
            print("Create an account ")
            username = input("Enter username: ").strip()
            self.create_account(username)

        
    def log_in(self, username):
        """
        Log in to an existing user. Usage: log_in <username>
        """
        password = getpass.getpass("Enter password: ")
        if password == self.users[username]['password']:
            print(f"Logged in as {username} {'(Admin)' if self.users[username]['is_admin'] else '(Member)'}.")
            self.logged_user = username
            self.is_admin_logged_user = self.users[username]['is_admin']
            self.print_user_menu(username)
        else:
            print("Incorrect password. Please try again.")
            self.log_in(username)

        
    def create_account(self,username):
        """
        Add a new user by using this funtion: add_user <username>
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
        return self.logged_user, self.is_admin_logged_user 
    
    def print_user_menu(self,username):
        
        if self.users[username]['is_admin']:
            message_admin = """
            1. Add new user : add_user <username>
            2. View all users : view_users
            3. Create event : create_event <event_name> <date> <time>
            """
            print(message_admin)
        else: 
            message_member = """
            1. Create event : create_event <event_name> <date> <time>
            """
            print(message_member)