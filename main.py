import cmd
from user_management import UserManagement
from event import EventManagement
from notification import NotificationManagement

class EventScheduler(cmd.Cmd):
    def __init__(self):
        """
        Initialize the EventScheduler class.
        Initialize the class with instances of UserManagement, EventManagement, and NotificationManagement. 
        Set up the users, confirm_creation, current_user, is_admin, and prompt attributes. 
        Start the notification manager in a separate thread using Python's threading module.
        """
        super().__init__()
        self.user_management = UserManagement()
        self.event_management = EventManagement()
        self.notification_management = NotificationManagement(self.event_management, self.user_management)
        self.users = self.user_management.users
        self.confirm_creation = False
        self.current_user, self.is_admin = self.user_management.check_user()
        self.prompt = ">> :"
        
        # Start the notification manager in a separate thread
        import threading
        notification_thread = threading.Thread(target=self.notification_management.check_upcoming_notifications)
        notification_thread.daemon = True  # Daemonize the thread so it terminates when the main program exits
        notification_thread.start()

    def do_log_out(self, line):
        """
        Log out the current user.

        Parameters:
        - line (str): This parameter is ignored.

        Returns:
        None

        This method logs out the current user by setting the current_user attribute to None.
        It then calls the check_user method of the user_management object to update the current_user and is_admin attributes.
        This allows the user to log in again.

        Example:
        >> : log_out
        """
        print("Logging out...")
        self.current_user = None
        self.current_user, self.is_admin = self.user_management.check_user()
    
    def do_create_event(self, line):
        """
        Create a new event.

        Parameters:
        - line (str): A string containing space-separated arguments for creating an event.
                    The expected format is "create_event <id> <title> <description> <time> <duration> <reminder>".

        Returns:
        None

        This method parses the input line to extract information for creating a new event.
        It then calls the create_event method of the event_management object to create the event.

        Example:
        >> : create_event 1 EventTitle EventDescription 2024-02-24 10:00 60
        """
        args = line.split()
        owner = self.current_user
        self.confirm_creation = self.event_management.create_event(args[0], args[1], args[2] + " " + args[3],args[4],int(args[5]),owner)
    
        
    def do_update_event(self, line):
        """
        Update an existing event.

        Parameters:
        - line (str): A string containing the command-line input with event details.

        Returns:
        None

        This method updates an existing event identified by the provided event_id with new information.
        The command-line input should follow the format: "update_event <event_id> <field_to_update> <new_value>".

        Example:
        >> : update_event 1 title NewTitle
        """
        args = line.split()
        self.event_management.update_event(args[0], args[1], args[2], self.current_user)
    
    def do_delete_event(self, line):
        """
        Delete an existing event.

        Parameters:
        - line (str): A string containing the command-line input with the event_id to delete.

        Returns:
        None

        This method deletes an existing event identified by the provided event_id.
        The command-line input should follow the format: "delete_event <event_id>".

        Example:
        >> : delete_event 1
        """
        self.event_management.delete_event(line,self.current_user)
    def do_view_my_events(self,line):
        """
        View events owned by the current user.

        Parameters:
        - line (str): A string containing the command-line input.

        Returns:
        None

        This method displays the events owned by the current user.

        Example:
        >> : view_my_events
        """    
        self.event_management.view_owner_events(self.current_user)
        
    def do_share_event(self, line):
        """
        Share an event with other users.

        Parameters:
        - line (str): A string containing the command-line input with event details.

        Returns:
        None

        This method allows the current user to share an event with other users by providing
        the event ID, username, and permission level. The available permissions are 'view' and 'edit'.

        Example:
        >> : share_event 1 maria view
        """
        args = line.split()
        self.event_management.add_shared_user(args[0], args[1], args[2], list(self.users.keys()), current_user=self.current_user)
    
    def do_respond_to_event(self, line):
        """
        Respond to a shared event invitation.

        Parameters:
        - line (str): A string containing the command-line input with event details.

        Returns:
        None

        This method allows the current user to respond to a shared event invitation by providing
        the event ID and the response (either 'accept' or 'decline').

        Example:
        >> : respond_to_event 1 accept
        """
        args = line.split()
        self.event_management.respond_to_event(args[0], args[1], self.current_user)
    
    def do_view_users(self, line):
        """
        View all users.

        Parameters:
        - line (str): Unused parameter.

        Returns:
        None

        This method displays the usernames of all registered users if the current user is an admin.

        Example:
        >> : view_users
        """
        is_admin = self.is_admin
        if is_admin:
            """
            View all users.
            """
            if self.users:
                print("Existing users:")
                for username in self.users:
                    print(f"- {username}")
            else:
                print("No users found.")
        else:
            print("You don't have permission to view users.")
    
    def do_admin_permission(self, line):
        """
        Grant admin permissions to a user.

        Parameters:
        - line (str): A string containing the command-line input with the username.

        Returns:
        None

        This method allows an admin to grant admin permissions to another user.

        Example:
        >> : admin_permission maria
        """
        is_admin = self.is_admin
        username = line.strip()
        if is_admin:
            self.users[username]['is_admin'] = True
            print(f"{username} is now an admin.")
        else:
            print("You don't have permission to change admin permissions.")

    def do_exit(self, line):
        """
        Exit the application.

        Parameters:
        - line (str): Unused parameter.

        Returns:
        bool: True to exit the application.

        This method exits the application.

        Example:
        >> : exit
        """
        print("Exiting...")
        return True

if __name__ == "__main__":
    app = EventScheduler()
    app.cmdloop("Welcome to the Event Scheduler App! by Juan Mirque")
