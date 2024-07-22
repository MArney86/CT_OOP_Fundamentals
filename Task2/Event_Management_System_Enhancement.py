class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0 #added participant count to the class

    def add_participant(self): #added add_participant method
        self.participants += 1 #add one participant to the participant count
    
    def get_participant_count(self): #added get_participant_count method
        return self.participant_count #return the value of participant_count