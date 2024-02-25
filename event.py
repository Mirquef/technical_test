from datetime import datetime, time, timedelta
class EventManagement:
    id_event_counter = 4
    def __init__(self):
        """
        Initialize the EventManagement class.

        Parameters:
        None

        Returns:
        None

        This method initializes the EventManagement class, creating an events repository.
        """
        self.events_repository = {
            1: {'id': 1, 'title': 'Event 1', 'description': 'Description 1', 'time': '2024-02-24 12:17', 'duration': "00:30", 'reminder': 1, 'owner': 'juan', 'shared_users': [{'maria': {'permission': 'edit', 'response': 'pending'}},{'pedro': {'permission': 'view', 'response': 'pending'}}]},
            2: {'id': 2, 'title': 'Event 2', 'description': 'Description 2', 'time': '2024-02-24 12:18', 'duration': "00:15", 'reminder': 1, 'owner': 'maria','shared_users': [{'juan': {'permission': 'view', 'response': 'pending'}}]},
            3: {'id': 3, 'title': 'Event 3', 'description': 'Description 3', 'time': '2024-02-24 12:19', 'duration': "00:45", 'reminder': 1, 'owner': 'pedro','shared_users': [{'maria': {'permission': 'view', 'response': 'pending'}}]}
            }  # Dictionary to store events
        
    def create_event(self, title, description, time, duration, reminder,owner):
        """
        Create a new event.

        Parameters:
        - title (str): Title of the event.
        - description (str): Description of the event.
        - time (str): Date and time of the event.
        - duration (str): Duration of the event.
        - reminder (int): Reminder setting for the event.
        - owner (str): Owner of the event.

        Returns:
        bool: True if the event is created successfully, False otherwise.

        This method creates a new event and adds it to the events repository.
        """
        event_id = EventManagement.id_event_counter
        EventManagement.id_event_counter += 1

        new_event = {
            'id': event_id,
            'title': title,
            'description': description,
            'time': time,
            'duration': datetime.strptime(duration,"%H:%M").time(),
            'owner': owner,
            'reminder': reminder,
            'shared_users': []
        }
        try:
            self.events_repository[event_id] = new_event
            print(f"Event '{title}' created successfully with ID: {event_id}.")
            return True
        except Exception as e:
            print(f"Error creating event: {e}")
    
    def update_event(self, event_id, field_to_update, new_value, username):
        """
        Update an event.

        Parameters:
        - event_id (str): ID of the event to update.
        - field_to_update (str): Field to update in the event.
        - new_value (str): New value for the specified field.
        - username (str): Username initiating the update.

        Returns:
        None

        This method updates a specific field in the event with the provided ID.
        """
        owner_events = [event for event in self.events_repository.values() if event['owner'] == username]
        id_valid = list({owner_events['id'] for owner_events in owner_events})
        shared_events = [
            event for event in self.events_repository.values()
            if username in [user for user_dict in event.get('shared_users', []) for user in user_dict.keys()] 
        ]
        
        for event in shared_events:
            for user_dict in event.get('shared_users', []):
                try:
                    if user_dict[username].get('permission') == 'edit':
                        id_valid.append(event['id'])
                except KeyError:
                    pass
                
        print(f'You can update these events ID: {id_valid}')      
        event_id = int(event_id)
        if event_id in id_valid:
            if field_to_update in self.events_repository[event_id]:
                self.events_repository[event_id][field_to_update] = new_value
                print(f"Event '{event_id}' updated successfully.")
            else:
                print(f"Field '{field_to_update}' not found in event '{event_id}'.")
        else:
            print(f"Event '{event_id}' not found.")
    
    def respond_to_event(self, event_id, new_value, username):
        """
        Respond to a shared event invitation.

        Parameters:
        - event_id (str): ID of the event to respond to.
        - new_value (str): New value for the response ('accept' or 'decline').
        - username (str): Username responding to the invitation.

        Returns:
        None

        This method updates the response field for the specified user in a shared event.
        """
        id_valid = []
        shared_events = [
            event for event in self.events_repository.values()
            if username in [user for user_dict in event.get('shared_users', []) for user in user_dict.keys()] 
        ]
        print(f'You can respond to these events ID: {id_valid}')  
        for event in shared_events:
            for user_dict in event.get('shared_users', []):
                try:
                    id_valid.append(event['id'])
                    event_id = int(event_id)
                    if event_id in id_valid:
                        user_dict[username]['response'] = new_value
                        print(f"Event '{event_id}' updated successfully.")
                except KeyError:
                    print(f"Event '{event_id}' not found.")
                
            

    
    def delete_event(self, event_id, username):
        """
        Delete an event.

        Parameters:
        - event_id (str): ID of the event to delete.
        - username (str): Username initiating the deletion.

        Returns:
        None

        This method deletes an event with the provided ID.
        """
        owner_events = [event for event in self.events_repository.values() if event['owner'] == username]
        id_valid = list({owner_events['id'] for owner_events in owner_events})
        shared_events = [
            event for event in self.events_repository.values()
            if username in [user for user_dict in event.get('shared_users', []) for user in user_dict.keys()] 
        ]
        
        for event in shared_events:
            for user_dict in event.get('shared_users', []):
                try:
                    if user_dict[username].get('permission') == 'edit':
                        id_valid.append(event['id'])
                except KeyError:
                    pass
                
        print(f'You can delete these events ID: {id_valid}')      
        event_id = int(event_id)
        if event_id in id_valid:
            del self.events_repository[event_id]
            print(f"Event '{event_id}' deleted successfully.")
        else:
            print(f"Event '{event_id}' not found.")
    
    def add_shared_user(self, event_id, username, permission, users, current_user):
        """
        Add a shared user to an event.

        Parameters:
        - event_id (str): ID of the event to share.
        - username (str): Username of the user to add.
        - permission (str): Permission level for the shared user.
        - users (list): List of all users in the system.
        - current_user (str): Username initiating the sharing.

        Returns:
        None

        This method adds a shared user to an event with the specified permission level.
        """
        owner_events = [event for event in self.events_repository.values() if event['owner'] == current_user]
        id_valid = list({owner_events['id'] for owner_events in owner_events})

        shared_events = [
            event for event in self.events_repository.values()
            if current_user in [user for user_dict in event.get('shared_users', []) for user in user_dict.keys()] 
        ]
        
        if username in users:
            for event in shared_events:
                for user_dict in event.get('shared_users', []):
                    try:
                        if user_dict[current_user].get('permission') == 'edit':
                            id_valid.append(event['id'])
                    except KeyError:
                        pass
            print(f'You can add a new user in these events ID: {id_valid}')      
            event_id = int(event_id) 
            
            if event_id not in id_valid:
                print(f"Error: Event with ID {event_id} not found.")
                return

            shared_users_list = self.events_repository[event_id]['shared_users']
            existing_user_dict = next((user_dict for user_dict in shared_users_list if username in user_dict), None)
            # This return the first match or None
            
            if existing_user_dict is None:
                # If the user doesn't exist, add a new dictionary for the user
                new_user_dict = {username: {'permission': permission, 'response': 'pending'}}
                shared_users_list.append(new_user_dict)
            else:
                # If the user already exists, update their permission
                existing_user_dict[username]['permission'] = permission

            print(f"User '{username}' added to the event '{event_id}' with permission '{permission}'.")
        else:
            print('The user does not exist in the database')
    def view_owner_events(self, owner):
        """
        View events owned and shared with a user.

        Parameters:
        - owner (str): Username of the user to view events for.

        Returns:
        None

        This method displays events owned and shared with the specified user.
        """
        owner_events = [event for event in self.events_repository.values() if event['owner'] == owner]
        shared_events = [
            event for event in self.events_repository.values()
            if owner in [user for user_dict in event.get('shared_users', []) for user in user_dict.keys()]
        ]
        if owner_events:
            print(f"Events owned by '{owner}':")
            for event in owner_events:
                print(f"Event ID: {event['id']}, Title: {event['title']}, Description: {event['description']}, Username invited: {event['shared_users']}")

        if shared_events:
            print(f"Events shared with '{owner}':")
            for event in shared_events:
                for user_dict in event.get('shared_users', []):
                    try:
                        response = user_dict[owner].get('response', 'pending')
                        print(f"Event ID: {event['id']}, Title: {event['title']}, Description: {event['description']}, My response: {response}")
                    except KeyError:
                        pass
        else:
            print(f"No events found for the user '{owner}'.")
    
    def get_all_events(self):
        return self.events_repository.values()