import cmd
from user_management import UserManagement


class EventScheduler(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.user_management = UserManagement()
        self.users = self.user_management.users
        
        self.prompt = ">> :"
        
        self.user_management.check_user()
        
        current_user, is_admin = self.user_management.get_logged_user()
        is_admin = self.users[current_user]['is_admin']

                # is_admin = input(f"Is '{username}' an admin? (Yes/No): ")
                
                # if is_admin.lower() == "yes":
                #     self.users[username]['is_admin'] = True
                # else:
                #     self.users[username]['is_admin'] = False
    def do_view_users(self, line):
        """
        View all users.
        """
        if self.users:
            print("Existing users:")
            for username in self.users:
                print(f"- {username}")
        else:
            print("No users found.")

    def do_add_data(self, line):
        """
        Add data for a user. Usage: add_data <username> <data>
        """
        args = line.split()
        if len(args) >= 2:
            username, data = args[0], ' '.join(args[1:])
            if username in self.users:
                self.users[username]['data'] = data
                print(f"Data added for user '{username}'.")
            else:
                print(f"User '{username}' not found.")
        else:
            print("Usage: add_data <username> <data>")

    def do_view_data(self, line):
        """
        View data for a user. Usage: view_data <username>
        """
        username = line.strip()
        if username in self.users and 'password' in self.users[username]:
            print(f"Data for user '{username}': {self.users[username]['password']}")
        else:
            print(f"No data found for user '{username}'.")

    def do_exit(self, line):
        """
        Exit the application.
        """
        print("Exiting...")
        return True

if __name__ == "__main__":
    app = EventScheduler()
    app.cmdloop("Welcome to the Event Scheduler App!")
