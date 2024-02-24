import cmd
from user_management import UserManagement
from event import EventManagement

class EventScheduler(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.user_management = UserManagement()
        self.event_management = EventManagement()
        self.users = self.user_management.users
        self.current_user, self.is_admin = self.user_management.check_user()
        self.prompt = ">> :"

    def do_log_out(self, line):
        print("Logging out...")
        self.current_user = None
        self.current_user, self.is_admin = self.user_management.check_user()
    
    def do_create_event(self, line):
        args = line.split()
        owner = self.current_user
        self.event_management.create_event(args[0], args[1], args[2], args[3],args[4],owner)
        
    def do_update_event(self, line):
        args = line.split()
        self.event_management.update_event(args[0], args[1], args[2])
    
    def do_delete_event(self, line):
        self.event_management.delete_event(line)
    def do_view_my_events(self,line):
        self.event_management.view_owner_events(self.current_user)
        
    def do_share_event(self, line):
        args = line.split()
        self.event_management.add_shared_user(args[0], args[1], args[2])
    
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
