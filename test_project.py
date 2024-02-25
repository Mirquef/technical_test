import unittest
from unittest.mock import patch
from main import EventScheduler  

class TestEventScheduler(unittest.TestCase):
    
    """
    Test case class for the EventScheduler application.

    Each test method simulates user input using the @patch decorator
    and tests specific functionalities of the EventScheduler.

    Test Methods:
    - test_create_update_share_view_delete_event: Test event creation,
      updating, sharing, viewing, and deletion.
    - test_view_and_accept_events: Test viewing and accepting events.
    - test_admin_permission: Test admin permission functionality.
    """
    
    @patch("builtins.input", side_effect=["Yes", "juan"])
    @patch("getpass.getpass", return_value="1")
    # @patch("builtins.input", side_effect=["create_event d Event1 Desc1 2024-02-24 10:00 00:30 60"])
    def test_A_event_class(self, mock_input, mock_getpass):

            app = EventScheduler()
            print("--- Creation of an event ---")
            app.onecmd("create_event Event1 Desc1 2024-02-24 10:00 00:30 60")
            print("_____________________________")
            print("--- Update of an event ---")
            app.onecmd("update_event 4 reminder 60")
            print("_____________________________")
            print("--- Sharing of an event ---")
            app.onecmd("share_event 4 maria view") 
            app.onecmd("share_event 4 pedro edit") 
            print("_____________________________")
            print("--- View of my events ---")
            app.onecmd("view_my_events")
            print("_____________________________")
            print("--- Delete of an event ---")
            app.onecmd("delete_event 4")

            response = app.confirm_creation
            self.assertTrue(response)

    @patch("builtins.input", side_effect=["Yes", "maria"])
    @patch("getpass.getpass", return_value="2")
    def test_B_view_and_accept_events(self, mock_input, mock_getpass):
            
            app = EventScheduler()

            print("--- View of my events ---")
            app.onecmd("view_my_events")
            print("_____________________________")
            print("--- Respond to an event ---")
            app.onecmd("respond_to_event 3 accepted")
            print("_____________________________")
            print("--- View of my events (ID 3 accepted)---")
            app.onecmd("view_my_events")
            
            print("--- Denied access to admin features ---")
            app.onecmd("view_users")
            
    @patch("builtins.input", side_effect=["Yes", "juan"])
    @patch("getpass.getpass", return_value="1")
    def test_C_admin_permission(self, mock_input, mock_getpass):
            
            app = EventScheduler()
            print("--- ADMIN PERMISSION ---")
            print("--- View all users ---")
            app.onecmd("view_users")
            print("_____________________________")
            print("--- Become an admin ---")
            app.onecmd("admin_permission maria")
            

if __name__ == '__main__':
    unittest.main()
