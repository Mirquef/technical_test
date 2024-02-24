from datetime import datetime,  timedelta
import time
class NotificationManagement:
    def __init__(self, event_management, user_management):
        self.event_manager = event_management
        self.users = user_management

    def check_upcoming_notifications(self):
        
        while True:
            upcoming_events = self.get_upcoming_event()
            current_user = self.users.get_logged_user()
            self.send_reminder(upcoming_events,current_user)
            
            sleep_duration = timedelta(minutes=1)
            time.sleep(sleep_duration.total_seconds())
    
    def get_upcoming_event (self):
        
        current_time = datetime.now()
        upcoming_events = []
        
        for event in self.event_manager.get_all_events():
            start_time = datetime.strptime(event['time'], "%Y-%m-%d %H:%M")
            if ( start_time - current_time) <= timedelta(minutes=event.get('reminder')) and current_time <= start_time:
                upcoming_events.append(event)
                
        return upcoming_events
    
    def send_reminder(self, events,current_user):
        for event in events:

            owners = [event['owner']] + [list(user.keys())[0] for user in event.get('shared_users', [])]
            for owner in owners:
                if owner == current_user:
                # Send notification to the owner
                    print(f"Hey {owner}! You have an upcoming event named {event['title']}, starting at {event['time']}.")
