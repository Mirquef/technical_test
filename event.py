class EventManagement:
    id_event_counter = 4
    def __init__(self):
        self.events_repository = {
            '1': {'id': 1, 'title': 'Event 1', 'description': 'Description 1', 'time': '10:00', 'duration': 60, 'reminder': 1, 'owner': 'juan', 'shared_users': [{'maria': {'permission': 'view', 'response': 'pending'}},{'pedro': {'permission': 'view', 'response': 'pending'}}]},
            '2': {'id': 2, 'title': 'Event 2', 'description': 'Description 2', 'time': '11:00', 'duration': 30, 'reminder': 1, 'owner': 'maria','shared_users': [{'juan': {'permission': 'view', 'response': 'pending'}}]},
            '3': {'id': 3, 'title': 'Event 3', 'description': 'Description 3', 'time': '12:00', 'duration': 45, 'reminder': 1, 'owner': 'pedro','shared_users': [{'maria': {'permission': 'view', 'response': 'pending'}}]}
            }  # Dictionary to store events
        
    def create_event(self, title, description, time, duration, reminder,owner):
        event_id = EventManagement.id_event_counter
        EventManagement.id_event_counter += 1

        new_event = {
            'id': event_id,
            'title': title,
            'description': description,
            'time': time,
            'duration': duration,
            'owner': owner,
            'reminder': reminder,
            'shared_users': []
        }
        try:
            self.events_repository[event_id] = new_event
            print(f"Event '{title}' created successfully with ID: {event_id}.")
        except Exception as e:
            print(f"Error creating event: {e}")
    
    def update_event(self, event_id, field_to_update, new_value):
        if event_id in self.events_repository:
            if field_to_update in self.events_repository[event_id]:
                self.events_repository[event_id][field_to_update] = new_value
                print(f"Event '{event_id}' updated successfully.")
            else:
                print(f"Field '{field_to_update}' not found in event '{event_id}'.")
        else:
            print(f"Event '{event_id}' not found.")
    
    def delete_event(self, event_id):
        if event_id in self.events_repository:
            del self.events_repository[event_id]
            print(f"Event '{event_id}' deleted successfully.")
        else:
            print(f"Event '{event_id}' not found.")
    
    def add_shared_user(self, event_id, username, permission):
        if event_id not in self.events_repository:
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

        print(f"User '{username}' added to event '{event_id}' with permission '{permission}'.")

    def view_owner_events(self, owner):
        
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