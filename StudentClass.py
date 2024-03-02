import datetime

class Student:

    def __init__(self,student_id, name, dob, classification):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.classification = classification
        
    def calculate_age(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.dob, '%Y-%m-%d').date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    
    def registration_dates(self):
        if self.classification == 'Sr':
            return "Seniors - 4/1 thru 4/3"
        elif self.classification == 'Jr':
            return "Juniors - 4/4 thru 4/6"
        elif self.classification == 'So':
            return "Sophomores - 4/7 thru 4/9"
        elif self.classification == 'Fr':
            return "Freshmen - 4/10 thru 4/12"
        else:
            return 'Invalid input, please enter "Fr" "So" "Ju" or "Sr"'

    def get_age(self):
        return f"{self.name}'s age is {self.calculate_age()}"

    def get_registration_dates(self):
        return f"{self.name} can register during: {self.registration_dates()}"